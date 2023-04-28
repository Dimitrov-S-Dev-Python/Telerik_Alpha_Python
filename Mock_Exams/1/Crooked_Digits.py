number = list(input())

while True:
    result = 0
    result += sum([int(x) for x in number if x.isdigit()])
    if result <= 9:
        print(result)
        break
    else:
        number = str(result)
