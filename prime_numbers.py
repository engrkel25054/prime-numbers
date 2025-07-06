# Program specification
"""
Write a program that prints the sum of the prime numbers greater than 2 and less than 1000.
Hint: you probably want to use a for loop that is a primality test nested inside a for loop that
iterates over the odd integers between 3 and 999.
"""

# Get the odd numbers between 2 and 1000
odd = []
for number in range(2, 1000):
    if number % 2 != 0:
        odd.append(number)

prime = []
composite = []
# counts number of divisors that gives zero remainder
count = 0

# Take each number from the odd number list
for number in odd:
    # Each number from the odd number list shall be divided by each number from the same list.
    # 3/3, 3/5, 3/7, 3/9, 3/11, etc.
    for divisor in odd:
        if number % divisor == 0:
            count += 1
    # if count > 1, it is a composite number
    if count > 1:
        composite.append(number)

    else:
        # a prime number can only divide by itself, in which count == 1
        prime.append(number)

    # reset divisor count
    count = 0

total = 0
for prime_number in prime:
    total += prime_number

print("The sum of prime numbers greater than 2 and less than 1000 is", total)
