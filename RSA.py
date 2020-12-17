import os
import time
import math
import random

from MillerRabin import new_prime, mul_inv, bytes_to_int, int_to_bytes


def encrypt(plaintext, public_key):
    N, e = public_key
    m = bytes_to_int(plaintext)
    assert m < N
    c = pow(m, e, N)
    return int_to_bytes(c)


def decrypt(ciphertext, private_key):
    p, q, d_p, d_q, q_inv = private_key
    c = bytes_to_int(ciphertext)
    m1 = pow(c, d_p, p)
    m2 = pow(c, d_q, q)
    h = (q_inv * (m1 - m2)) % p
    m = (m2 + h * q) % (p * q)
    return int_to_bytes(m)


def new_key_pair(num_bits):
    p = new_prime(num_bits)
    q = new_prime(num_bits)
    N = p * q
    phi_N = (p - 1) * (q - 1)
    e = _choose_e(phi_N)
    d = mul_inv(e, phi_N)
    d_p = d % (p - 1)
    d_q = d % (q - 1)
    q_inv = mul_inv(q, p)
    return (N, e), (p, q, d_p, d_q, q_inv)


def _choose_e(phi_n):
    while True:
        e = random.randint(3, phi_n - 1)
        if math.gcd(e, phi_n) == 1:
            return e


if __name__ == '__main__':
    for bit_length in [384, 512, 1024, 1536]:
        m_len = bit_length // 4 - 66
        plaintext = os.urandom(m_len)
        print('Length of P and Q = {}'.format(bit_length))
        print('Message len (bits) = {}'.format(8 * m_len))

        start = time.time()
        public, private = new_key_pair(bit_length)
        print('Time elapsed for key-gen: {} sec'.format(time.time() - start))

        start = time.time()
        ciphertext = encrypt(plaintext, public)
        print('Time elapsed for encryption: {} sec'.format(time.time() - start))

        start = time.time()
        decrypt(ciphertext, private)
        print('Time elapsed for decryption: {} sec'.format(time.time() - start))
        print()
