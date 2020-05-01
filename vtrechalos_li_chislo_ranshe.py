nums = list(map(int, input().split()))
numSet = set()
for i in nums:
    if i in numSet:
        print('YES')
    else:
        print('NO')
    numSet.add(i)
