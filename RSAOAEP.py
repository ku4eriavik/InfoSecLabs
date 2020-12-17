import os
import time
import math
import random


from utils import SHA256
from MillerRabin import new_prime, mul_inv, xor_bytes,\
    bytes_to_int, int_to_bytes, byte_length


sha = SHA256()
hsh_fnc = lambda x: int_to_bytes(sha.hash(x))
hash_len = 32


def encrypt(plaintext, public_key, label=b''):
    N, e = public_key
    k = byte_length(N)
    m_len = len(plaintext)
    assert m_len <= k - 2 * hash_len - 2

    label_hash = hsh_fnc(label)
    zero_padding = b'\x00' * (k - m_len - 2 * hash_len - 2)
    db = label_hash + zero_padding + b'\x01' + plaintext
    seed = os.urandom(hash_len)

    db_mask = mgf1(seed, k - hash_len - 1)
    masked_db = xor_bytes(db, db_mask)
    seed_mask = mgf1(masked_db, hash_len)
    masked_seed = xor_bytes(seed, seed_mask)

    em = b'\x00' + masked_seed + masked_db
    m = bytes_to_int(em)
    c = pow(m, e, N)
    return int_to_bytes(c)


def decrypt(ciphertext, private_key, label=b''):
    p, q, d_p, d_q, q_inv = private_key
    N = p * q
    k = byte_length(N)

    c = bytes_to_int(ciphertext)
    m1 = pow(c, d_p, p)
    m2 = pow(c, d_q, q)
    h = (q_inv * (m1 - m2)) % p
    m = (m2 + h * q) % (p * q)
    em = int_to_bytes(m, k)

    label_hash = hsh_fnc(label)
    masked_db = em[-(k - hash_len - 1):]
    masked_seed = em[-(k - 1): -(k - hash_len - 1)]

    seed_mask = mgf1(masked_db, hash_len)
    seed = xor_bytes(masked_seed, seed_mask)
    db_mask = mgf1(seed, k - hash_len - 1)
    db = xor_bytes(masked_db, db_mask)

    decrypted_label_hash = db[:hash_len]
    assert label_hash == decrypted_label_hash

    i = hash_len
    while db[i] == 0:
        i += 1
    plaintext = db[i + 1:]
    return plaintext


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


def mgf1(b_data, length):
    counter = 0
    output = b''
    while len(output) < length:
        input_bytes = b_data + int_to_bytes(counter, 4)
        output += hsh_fnc(input_bytes)
        counter += 1
    return output[:length]


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
