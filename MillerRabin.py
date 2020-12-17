import random
import math


def miller_rabin_test(number, amount_rounds):
    if number == 2 or number == 3:
        return True
    if number % 2 == 0:
        return False

    r = 0
    s = number - 1
    while s % 2 == 0:
        r += 1
        s //= 2

    for mr_round in range(amount_rounds):
        # print('Miller-Rabin round #{}/{} for {}'.format(mr_round + 1, amount_rounds, number))
        a = random.randint(2, number - 2)
        x = pow(a, s, number)
        if x == 1 or x == number - 1:
            continue

        # for _ in range(x - 1):
        for _ in range(r - 1):
            x = pow(x, 2, number)
            if x == number - 1:
                break
        else:
            return False

    return True


def new_prime(num_bits, k=40):
    assert num_bits >= 2

    l, h = 2 ** (num_bits - 1), 2 ** num_bits - 1
    while True:
        a = random.randint(l, h)
        if miller_rabin_test(a, k):
            return a


def mul_inv(a, m):
    m0 = m
    x0, x1 = 0, 1
    if m == 1:
        return 1
    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1


def xor_bytes(bytes1, bytes2):
    assert len(bytes1) == len(bytes2)
    return bytes(a ^ b for (a, b) in zip(bytes1, bytes2))


def byte_length(n):
    return math.ceil(n.bit_length() / 8)


def bytes_to_int(b_data):
    return int.from_bytes(b_data, 'big')


def int_to_bytes(n, fill_size=-1):
    bytes_required = fill_size if fill_size != -1 else byte_length(n)
    return n.to_bytes(bytes_required, 'big')


if __name__ == '__main__':
    mr_res = miller_rabin_test(139288917338851014479864761563177272053, 40)
    print('{}'.format('Prime' if mr_res else 'Composite'))

    nw_prm = new_prime(30, 40)
    print('New prime: {}'.format(nw_prm))
