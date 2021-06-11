text = input("Enter your sudoku: ")

i = True

def check(text, start, end, inc):
    i = True
    count = 0
    for char in range(start, end, inc):
        for test in range(char + 1, 9):
            if text[char] == text[test]:
                return False
    return True

for n in range(0, 9):
    if check(text, 9 * n, 9 * (n + 1), 1) == False:
        i = False
    if check(text, n, len(text), 9) == False:
        i = False

tmp = ""
for x in range(0, 3):
    for n in range(0, 3):
        tmp += text[(3 * n + 27 * x):(3 * (n + 1) + 27 * x)]
        tmp += text[(3 * n + 9 + 27 * x):(3 * (n + 1) + 9 + 27 * x)]
        tmp += text[(3 * n + 18 + 27 * x):(3 * (n + 1) + 18 + 27 * x)]
        if check(tmp, 0, 9, 1) == False:
            i = False

if i:
    print("Yes")
else:
    print("No")
