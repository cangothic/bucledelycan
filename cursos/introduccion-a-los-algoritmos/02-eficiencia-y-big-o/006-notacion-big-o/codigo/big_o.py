import math


def pasos(n):
    return {
        "O(1)": 1,
        "O(log n)": math.log2(n),
        "O(n)": n,
        "O(n log n)": n * math.log2(n),
        "O(n^2)": n ** 2,
        "O(2^n)": 2 ** n,
    }


for n in [10, 100, 1000]:
    print("n =", n)
    for familia, p in pasos(n).items():
        if p < 10 ** 9:
            print(familia, round(p))
        else:
            print(familia, len(str(p)), "cifras")
