from time import time
import numpy as np


class Salsa20:
    MASK = 0xffffffff

    def __init__(self, key_bytes):
        assert len(key_bytes) == 32
        self._amount_rounds = 20
        self._key = self._convert(np.array(key_bytes, np.uint8), np.uint32).tolist()
        self._nonce = np.random.randint(256, size=(2, ), dtype=np.uint32).tolist()

    def _process(self, message):
        b_len = 4 * 16
        assert len(message) % b_len == 0
        amount_parts = len(message) // b_len
        processed = []

        for pos in range(amount_parts):
            part_message = message[pos * b_len: (pos + 1) * b_len]
            part_message = self._convert(np.array(part_message, np.uint8), np.uint32).tolist()
            b = self._convert(np.array([pos], np.uint64), np.uint32).tolist()

            state = [
                0x61707865,     self._key[0],   self._key[1],   self._key[2],
                self._key[3],   0x3320646e,     self._nonce[0], self._nonce[1],
                b[0],           b[1],           0x79622d32,     self._key[4],
                self._key[5],   self._key[6],   self._key[7],   0x6b206574
            ]

            for _ in range(0, self._amount_rounds, 2):
                self._qr(state, 0, 4, 8, 12)
                self._qr(state, 5, 9, 13, 1)
                self._qr(state, 10, 14, 2, 6)
                self._qr(state, 15, 3, 7, 11)

                self._qr(state, 0, 1, 2, 3)
                self._qr(state, 5, 6, 7, 4)
                self._qr(state, 10, 11, 8, 9)
                self._qr(state, 15, 12, 13, 14)

            part_processed = []
            for j in range(16):
                m = part_message[j]
                s = state[j]
                part_processed.append(m ^ s)
            part_processed = self._convert(np.array(part_processed, np.uint32), np.uint8).tolist()
            processed.append(part_processed)
        return np.concatenate(processed).astype(np.uint8)

    @staticmethod
    def _qr(state, a, b, c, d):
        state[b] ^= Salsa20._rotl32((state[a] + state[d]) & Salsa20.MASK, 7)
        state[c] ^= Salsa20._rotl32((state[b] + state[a]) & Salsa20.MASK, 9)
        state[d] ^= Salsa20._rotl32((state[c] + state[b]) & Salsa20.MASK, 13)
        state[a] ^= Salsa20._rotl32((state[d] + state[c]) & Salsa20.MASK, 18)

    @staticmethod
    def _rotl32(w, r):
        return (
            (w << r) & Salsa20.MASK
        ) | (
            w >> (32 - r)
        )

    @staticmethod
    def _convert(arr, tp):
        return np.frombuffer(bytearray(arr), tp)

    def encrypt(self, message):
        return self._process(message)

    def decrypt(self, message):
        return self._process(message)


def benchmark_Salsa20():
    key_length = 32
    key_data = np.arange(key_length, dtype=np.uint8)
    encoder_decoder = Salsa20(key_data)

    data_size_powers = [10, 20]
    data_size_headers = ['KB', 'MB', 'GB']

    for idx, dsp in enumerate(data_size_powers):
        message_len = 2 << dsp
        message_data = np.random.randint(low=0, high=256, size=message_len, dtype=np.uint8).tolist()

        t_before = time()
        encrypted_data = encoder_decoder.encrypt(message_data)
        decrypted_data = encoder_decoder.encrypt(encrypted_data).tolist()
        t_after = time()

        assert message_data == decrypted_data, 'Encryption-Decryption failed.'
        t_delta = t_after - t_before
        print('BENCHMARKING Salsa20 ON:')
        print('\tKEY LENGTH = {}'.format(key_length))
        print('\tMESSAGE LENGTH = 1 {}'.format(data_size_headers[idx]))
        print('\tTIME ELAPSED = {} sec'.format(t_delta))
        print('*'.join(['-'] * 20))
        print()


if __name__ == '__main__':
    benchmark_Salsa20()
