#Asking user for input
num = int(input("Please enter any integer: "))

if (num > 1):
    for x in range(2, num // 2):
        if (num % x) == 0:
            print(str(num) + " is not a prime number.")
            break
    else:
            print(str(num) + " is a prime number.")

else:
            print(str(num) + " is not a prime number.")
