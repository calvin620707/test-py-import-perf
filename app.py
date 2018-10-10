import inner
import top
from time import perf_counter

LOOP = 10000000
DATA = {'key': 'value'}

if __name__ == '__main__':
    start = perf_counter()
    for _ in range(LOOP):
        top.dumps(DATA)
    spent = perf_counter() - start
    print(f"Spent {spent} seconds with import json at top.")

    start = perf_counter()
    for _ in range(LOOP):
        inner.dumps(DATA)
    spent = perf_counter() - start
    print(f"Spent {spent} seconds with import json in function.")
