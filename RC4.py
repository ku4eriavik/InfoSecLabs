import random
import string


def generate_bytes(size):
    generated = random.choices(string.ascii_letters + string.digits, k=size)
    return bytes(''.join(generated), 'ascii')


class RC4:
    def __init__(self, private_key):
        self.private_key = private_key
        self.key_length = len(self.private_key)
        self.gen_x = 0
        self.gen_y = 0

    def key_scheduling(self):
        pk_len = len(self.private_key)
        s = list(range(256))
        j = 0
        for i in range(256):
            j = (j + s[i] + self.private_key[i % pk_len]) % 256
            s[i], s[j] = s[j], s[i]
        return s

    def generation(self, s, buffer_length):
        key_stream = []
        for _ in range(buffer_length):
            gen_x = (self.gen_x + 1) % 256
            gen_y = (self.gen_y + s[gen_x]) % 256
            s[gen_x], s[gen_y] = s[gen_y], s[gen_x]
            k = s[(s[gen_x] + s[gen_y]) % 256]
            key_stream.append(k)
        return key_stream

    def process(self, data_bytes):
        data_len = len(data_bytes)
        s = self.key_scheduling()
        k = self.generation(s, data_len)
        result = []
        for i in range(data_len):
            result.append(data_bytes[i] ^ k[i])
        return bytes(result)


def benchmark_RC4():
    from time import time

    pr_key_len = 16
    data_size_powers = [10, 20, 30]
    data_size_headers = ['KB', 'MB', 'GB']

    for idx, dsp in enumerate(data_size_powers):
        message_len = 2 << dsp

        pr_key = generate_bytes(pr_key_len)
        message = generate_bytes(message_len)

        alg = RC4(pr_key)

        t_before = time()

        encoded_message = alg.process(message)
        decoded_message = alg.process(encoded_message)

        t_after = time()

        assert message == decoded_message, 'Encryption-Decryption failed.'
        t_delta = t_after - t_before
        print('BENCHMARKING RC4 ON:')
        print('\tKEY LENGTH = {}'.format(pr_key_len))
        print('\tMESSAGE LENGTH = 1 {}'.format(data_size_headers[idx]))
        print('\tTIME ELAPSED = {} sec'.format(t_delta))
        print('*'.join(['-'] * 20))
        print()


if __name__ == '__main__':
    benchmark_RC4()
