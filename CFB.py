from time import time
import numpy as np


class CFB:
    def __init__(self, aes_cipher, n=16):
        self._aes = aes_cipher
        self._n = n
        self._iv = np.random.randint(256, size=(self._n, ), dtype=np.uint8).tolist()

    @staticmethod
    def xor_arrays(a, b):
        return [a[i] ^ b[i] for i, _ in enumerate(b)]

    def encrypt(self, message):
        assert len(message) % self._n == 0
        encrypted = []
        current = self._iv
        for i in range(len(message) // self._n):
            part_message = message[i * self._n: (i + 1) * self._n].tolist()
            part_encrypted = self.xor_arrays(part_message, self._aes.encrypt(current))
            current = part_encrypted
            encrypted.append(part_encrypted)
        return np.concatenate(encrypted).astype(np.uint8)

    def decrypt(self, message):
        assert len(message) % self._n == 0
        decrypted = []
        current = self._iv
        for i in range(len(message) // self._n):
            part_message = message[i * self._n: (i + 1) * self._n].tolist()
            part_decrypted = self.xor_arrays(part_message, self._aes.encrypt(current))
            decrypted.append(part_decrypted)
            current = part_message
        return np.concatenate(decrypted).astype(np.uint8)


def benchmark_CFB():
    from AES import AES, KEY_LENGTH

    key_length = 16
    key_data = np.arange(key_length, dtype=np.uint8).tolist()
    aes_type = KEY_LENGTH.KL_128
    aes = AES(aes_type, key_data)
    encoder_decoder = CFB(aes, 16)

    data_size_powers = [10, 20]
    data_size_headers = ['KB', 'MB', 'GB']

    for idx, dsp in enumerate(data_size_powers):
        message_len = 2 << dsp
        message_data = np.random.randint(256, size=message_len, dtype=np.uint8)

        t_before = time()
        encrypted_data = encoder_decoder.encrypt(message_data)
        decrypted_data = encoder_decoder.decrypt(encrypted_data)
        t_after = time()

        t_delta = t_after - t_before
        print('BENCHMARKING CFB ON:')
        print('\tUSING AES WITH {}'.format(aes_type.value))
        print('\tMESSAGE LENGTH = 1 {}'.format(data_size_headers[idx]))
        print('\tTIME ELAPSED = {} sec'.format(t_delta))
        print('*'.join(['-'] * 20))
        print()

        assert decrypted_data.tolist() == message_data.tolist(), 'Encryption-Decryption failed.'


if __name__ == '__main__':
    benchmark_CFB()
