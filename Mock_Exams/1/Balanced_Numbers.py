result = 0
while True:
    number = input()
    if int(number[1]) != int(number[0]) + int(number[2]):
        break
    result += int(number)

print(result)
