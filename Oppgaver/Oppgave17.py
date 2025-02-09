def is_primtall(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

number = int(input("Enter Number here --> "))
if is_primtall(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

