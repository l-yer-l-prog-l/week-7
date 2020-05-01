n = int(input())
aSet = set()
bSet = set()
answer = ''
count = 0
while answer != 'HELP':
    nums = set(input().split())
    if 'HELP' in nums:
        break
    answer = str(input())
    if count == 0:
        aSet = aSet | nums
    if answer == 'YES':
        aSet &= nums
    elif answer == 'NO':
        bSet = bSet | nums
    else:
        break
    count += 1
minSet = aSet & bSet
aSet -= minSet
if aSet < {1}:
    print(n)
else:
    print(*sorted(aSet))
