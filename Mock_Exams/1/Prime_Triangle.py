n = int(input())

values_list = []

for number in range(1, n + 1):
    values_list.append(number)

prime_num = []

for number in values_list:
    condition = True
    for i in range(2, number):
        if number % i == 0:
            condition = False
    if condition:
        prime_num.append(number)

for row in range(len(prime_num)):
    for col in range(1, prime_num[row] + 1):
        if col in prime_num:
            col = 1
        else:
            col = 0
        print(col, end="")

    print()
