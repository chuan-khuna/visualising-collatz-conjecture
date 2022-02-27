import numpy as np


def collatz_recursive(n, sequence=[]):

    # TODO: if not pass the sequence argument
    # when calling collatz recursive version, sequence dods not start from []

    sequence.append(int(n))

    # base case, stop if n = 1
    if n == 1:
        return sequence

    if n % 2 == 0:
        return collatz_recursive(n / 2, sequence)
    else:
        return collatz_recursive(3 * n + 1, sequence)


def collatz(n):
    sequence = []
    while n != 1:
        sequence.append(int(n))
        if n % 2 == 0:
            n = n / 2
        else:
            n = (3 * n) + 1
    sequence.append(int(n))
    return sequence


def collatz_with_history(to_n):
    history = {}

    for k in range(1, to_n + 1):
        seq = []
        n = k

        # collatz
        while n != 1:
            if n in history.keys():
                seq = seq + history[n].tolist()
                break
            else:
                seq.append(int(n))
                if n % 2 == 0:
                    n = n / 2
                else:
                    n = n * 3 + 1
                # base case
        if n == 1:
            seq.append(int(n))

        history[k] = np.array(seq, dtype=np.int)

    return history


def collatz_custom_rules(n, odd_func=lambda x: int(3 * x + 1), even_func=lambda x: int(x / 2)):
    sequence = []
    while n != 1:
        # to prevent, infinite loop
        if (len(sequence) >= 10 and n in sequence):
            break
        sequence.append(int(n))
        if n % 2 == 0:
            n = even_func(n)
        else:
            n = odd_func(n)
    sequence.append(int(n))

    return sequence