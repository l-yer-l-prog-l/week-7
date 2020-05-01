nums = int(input())
firstSet = set()
secondSet = set()
for i in range(nums):
    num = int(input())
    lang = {input() for j in range(num)}
    firstSet |= lang
    if i == 1:
        secondSet |= lang
    else:
        secondSet &= lang
print(len(secondSet))
print('\n'.join(sorted(secondSet)))
print(len(firstSet))
print('\n'.join(sorted(firstSet)))
