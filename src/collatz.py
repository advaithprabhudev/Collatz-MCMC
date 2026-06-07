# Collatz Map Computation: Range from Z

# Baseline Collatz Map

def collatz_steps(x: int) -> int:
    while x != 1:
        if x == 1:
            return 0
        elif x % 2 == 0:
            return x // 2
        else:
            return (3 * x + 1) // 2

# Stopping Time for Parity Vector


def stopping_time(n: int) -> int:
    counter = 0
    while n != 1:
        n = collatz_steps(n)
        counter += 1
    return counter


# Stopping Time batches computing stopping times of O(1), O(2), O(3).., O(n)
def stopping_time_batches(N: int):
    arr = []
    for i in range(1, N + 1):
        arr.append(stopping_time(i))
    return arr
