fileIn = open('input.txt', 'r', encoding='utf-8-sig')
line = fileIn.read().strip().split()
text = dict()
for n in line:
    text[n] = text.get(n, 0) + 1
print(max(sorted(text.keys()), key=lambda x: text[x]))
fileIn.close()
