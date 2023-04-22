def plusMinus(arr):
    positive, negative, zero = 0, 0, 0
    for i in arr:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
        else:
            zero += 1

    n = len(arr)
    print(f"{positive/n:.6f}")
    print(f"{negative/n:.6f}")
    print(f"{zero/n:.6f}")
