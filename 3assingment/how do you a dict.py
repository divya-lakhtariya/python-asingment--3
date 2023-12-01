# How Do You Traverse Through A Dictionary Object In Python?

(1) Using a For Loop:
    d = {'a': 1, 'b': 2, 'c': 3}

    for key, value in d.items():
        print(f"Key: {key}, Value: {value}")

(2) Using Keys:
    d = {'a': 1, 'b': 2, 'c': 3}

    for key in d:
        print(f"Key: {key}, Value: {d[key]}")

(3) Using Values:
    d = {'a': 1, 'b': 2, 'c': 3}

    for value in d.values():
        print(f"Value: {value}")
