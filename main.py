import numpy as np
from time import time

from AES import AES, KEY_LENGTH


def benchmark(aes_type, data_size):
    print('BENCHMARKING {} ALGORITHM FOR {} BYTES OF DATA'.format(aes_type.value, data_size))

    buffer_size = 16
    amount_buffers = data_size // buffer_size

    before_pre = time()

    data = np.split(np.random.randint(0, 255, data_size), amount_buffers)
    crypto_key = np.random.randint(0, 255, buffer_size).tolist()

    after_pre = time()
    delta_init = after_pre - before_pre
    print('Time elapsed for preprocessing: {} sec'.format(delta_init))

    before_exp = time()

    encoder = AES(aes_type, crypto_key)

    after_exp = time()
    delta_init = after_exp - before_exp
    print('Time elapsed for key expansion: {} sec'.format(delta_init))

    encrypted = []
    decrypted = []

    before_enc = time()

    for buffer in data:
        enc_data = encoder.encrypt(buffer)
        encrypted.append(enc_data)

    for enc_data in encrypted:
        dec_data = encoder.decrypt(enc_data)
        decrypted.append(dec_data)

    assert len(data) == len(decrypted)
    for idx in range(len(data)):
        assert data[idx].tolist() == decrypted[idx].tolist()

    after_enc = time()
    delta_crpt = after_enc - before_enc
    print('Time elapsed for encryption-decryption: {} sec'.format(delta_crpt))
    print('-'.join(['*'] * 30))


if __name__ == '__main__':
    d_size = 2 ** 16
    benchmark(KEY_LENGTH.KL_128, d_size)
    benchmark(KEY_LENGTH.KL_192, d_size)
    benchmark(KEY_LENGTH.KL_256, d_size)
