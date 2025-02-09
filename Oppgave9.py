n = int(input("Number enter here --> "))
divisors = []

for i in range (1, n+1):
    if n % i == 0:
        divisors.append(i)

print(f"Divisors of {n} are: {divisors}")