"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""
import random

# q = set(range(1, 10))
q = set(range(1, 200))
# q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here
cache = {}
results = {}
sums = {}
diffs = {}
def sumdiff(sorted_list):
    for i in range(len(sorted_list) + 1):
        for j in range((i), len(sorted_list) + 1):
            if isinstance(sorted_list, set):
                sums[(i, j)] = f(i) + f(j)
                sums[(j, i)] = f(j) + f(i)
                diffs[(i, j)] = f(i) - f(j)
                diffs[(j, i)] = f(j) - f(i)
            else:
                sums[(sorted_list[i], sorted_list[j])] = f(sorted_list[i]) + f(sorted_list[j])
                sums[(sorted_list[j], sorted_list[i])] = f(sorted_list[j]) + f(sorted_list[i])
                diffs[(sorted_list[i], sorted_list[j])] = f(sorted_list[i]) - f(sorted_list[j])
                diffs[(sorted_list[j], sorted_list[i])] = f(sorted_list[j]) - f(sorted_list[i])

    for val1 in sums:
        for val2 in diffs:
            if val1 == val2:
                print(f"f({val1[0]}) + f({val1[1]}) = f({val2[1]}) - f({val2[1]})")

    # for val1 in sorted_list:
        # for val2 in sorted_list:
        #     for val3 in sorted_list:
        #         for val4 in sorted_list:
        #             if sums[(val1, val2)] == diffs[(val3, val4)]:
        #                 print(f"f({val1}) + f({val2}) = f({val3}) - f({val4})")



sumdiff(q)