arrSz, rotateN, rotateT = tuple(map(int, input().split()))

arr = list(map(int, input().split()))

if rotateT == 0:
    # left rotate
    arr = [arr[(i + rotateN) % len(arr)] for i, x in enumerate(arr)]
else:
    # right rotate
    arr = [arr[(i - rotateN) % len(arr)] for i, x in enumerate(arr)]

print(" ".join(map(str, arr)))