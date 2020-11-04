from time import time
from Kupyna import Kupyna
from SHA256 import SHA256


def proof_of_work(h_functor, message_prefix, zero_bits):
    mask = int('1' * zero_bits, 2)
    i = 0
    t_before = time()
    while True:
        hex_i = hex(i)[2:]
        hex_i = '0' * (len(hex_i) % 2) + hex_i
        message = message_prefix + hex_i
        res = h_functor(message) & mask
        if res == 0:
            break
        i += 1
    t_after = time()
    return t_after - t_before


def benchmark():
    sha256 = SHA256()
    kupyna256 = Kupyna(256)
    kupyna512 = Kupyna(512)

    prefix = ''.join([hex(ord(c))[2:].zfill(2) for c in 'sometimes I wanna die'])
    print('PREFIX: {}'.format(prefix))

    for zb in range(2, 5):
        t_sha256 = proof_of_work(sha256.hash, prefix, zb)
        t_kupyna256 = proof_of_work(kupyna256.hash, prefix, zb)
        t_kupyna512 = proof_of_work(kupyna512.hash, prefix, zb)

        print('POW: zero bits = {}'.format(zb))
        print('TIME ELAPSED:')
        print('\tSHA-256: {} sec.'.format(t_sha256))
        print('\tKUPYNA-256: {} sec.'.format(t_kupyna256))
        print('\tKUPYNA-512: {} sec.'.format(t_kupyna512))


if __name__ == '__main__':
    benchmark()
