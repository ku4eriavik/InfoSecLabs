from time import time


class SHA256:
    CONSTANTS = [
        0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
        0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
        0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
        0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
        0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
        0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
        0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
        0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
    ]
    MASK = 0xffffffff
    INITIAL = [0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19]

    def __init__(self):
        pass

    @staticmethod
    def message_to_blocks(message):
        bytes = [int(message[i * 2: (i + 1) * 2], 16) for i in range(len(message) // 2)]
        binary_message = ''.join(bin(byte)[2:].zfill(8) for byte in bytes)
        l = len(binary_message)
        k = (447 - l) % 512
        padded_message = binary_message + '1' + '0' * k + bin(l)[2:].zfill(64)
        blocks = []
        for i in range(len(padded_message) // 512):
            binary_block = padded_message[i * 512:(i + 1) * 512]
            block = []
            for j in range(16):
                block.append(int(binary_block[j * 32: (j + 1) * 32], 2))
            blocks.append(block)
        return blocks

    @staticmethod
    def sigma0(x):
        return SHA256.rotr(x, 7) ^ SHA256.rotr(x, 18) ^ (x >> 3)

    @staticmethod
    def sigma1(x):
        return SHA256.rotr(x, 17) ^ SHA256.rotr(x, 19) ^ (x >> 10)

    @staticmethod
    def Sigma0(x):
        return SHA256.rotr(x, 2) ^ SHA256.rotr(x, 13) ^ SHA256.rotr(x, 22)

    @staticmethod
    def Sigma1(x):
        return SHA256.rotr(x, 6) ^ SHA256.rotr(x, 11) ^ SHA256.rotr(x, 25)

    @staticmethod
    def rotr(x, n):
        return (x >> n) | (x << (32 - n)) & SHA256.MASK

    @staticmethod
    def Ch(x, y, z):
        return (x & y) ^ ((~x & SHA256.MASK) & z)

    @staticmethod
    def Maj(x, y, z):
        return (x & y) ^ (x & z) ^ (y & z)

    @staticmethod
    def apply_hash(vals, hash_vals):
        res = []
        for idx, hv in enumerate(hash_vals):
            applied = (vals[idx] + hv) & SHA256.MASK
            res.append(applied)
        return res

    def hash(self, message):
        hash_value = SHA256.INITIAL.copy()
        blocks = self.message_to_blocks(message)
        for block in blocks:
            W = [x for x in block]
            for t in range(16, 64):
                new_w = (
                    self.sigma1(W[t - 2]) + W[t - 7]
                    + self.sigma0(W[t - 15]) + W[t - 16]
                ) & self.MASK
                W.append(new_w)

            a, b, c, d, e, f, g, h = hash_value
            for t in range(64):
                T1 = (h + self.Sigma1(e) + self.Ch(e, f, g) + self.CONSTANTS[t] + W[t]) & self.MASK
                T2 = (self.Sigma0(a) + self.Maj(a, b, c)) & self.MASK
                h = g
                g = f
                f = e
                e = (d + T1) & self.MASK
                d = c
                c = b
                b = a
                a = (T1 + T2) & self.MASK

            hash_value = self.apply_hash(
                (a, b, c, d, e, f, g, h),
                hash_value
            )

        return int(''.join([hex(hv)[2:].zfill(8) for hv in hash_value]), 16)


def test():
    pairs = [
        (
            ''.join([hex(ord(c))[2:].zfill(2) for c in 'sometimes I wanna die']),
            75557623967801088860825877678069310390521606103903177392315076235034772596652
        ),
        (
            ''.join([hex(ord(c))[2:].zfill(2) for c in 'but I have to be strong']),
            22641911174741934153219954259322032184825685425594664743061679673310554968489
        ),
        (
            ''.join([hex(ord(c))[2:].zfill(2) for c in 'complete all university tasks']),
            27729367533311819375694117650450200504767231404273010708770715634923856939703
        ),
        (
            ''.join([hex(ord(c))[2:].zfill(2) for c in 'do all my job tasks, resolve issues']),
            73478202363907814835562038626719073427677120479360824107386869084901651780952
        ),
        (
            ''.join([hex(ord(c))[2:].zfill(2) for c in 'write several papers, propose patents, win hackatons']),
            67947402855814706717303030626547300037640164569131558193320906559740077540996
        ),
        (
            ''.join([hex(ord(c))[2:].zfill(2) for c in 'find a wife, have kids, travel the world, develop hobbies']),
            89541483354359075689981101128330909205218514774998676746105352430010607273022
        ),
        (
            ''.join([hex(ord(c))[2:].zfill(2) for c in 'and live life to the full']),
            104205509258226147006569292989996011135140552018761165292655247966372957788834
        )
    ]

    t_before = time()
    sha = SHA256()
    for p_in, p_out in pairs:
        hashed = sha.hash(p_in)
        assert hashed == p_out, 'Wrong!'
    t_after = time()
    print('Time elapsed: {} sec.'.format(t_after - t_before))


if __name__ == '__main__':
    test()
