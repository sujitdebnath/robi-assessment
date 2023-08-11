def reverse_list(arr, start, end, pos):
    while start < end:
        if start == pos-1:
            start +=1
        elif end == pos-1:
            end -= 1
        else:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

test_case = int(input())

for ind in range(test_case):
    arrSz, pos = tuple(map(int, input().split()))
    arr = list(map(int, input().split()))
    
    reverse_list(arr, 0, arrSz-1, pos)
    print(" ".join(map(str, arr)))