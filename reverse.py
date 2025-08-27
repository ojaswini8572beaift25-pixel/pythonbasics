num = 1342678
reversed_number = 0

while num != 0:
    digit = num % 10
    reversed_number = reversed_number * 10 + digit
    num = num // 10

    print("Reversed number is:", reversed_number)