# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

# 1 for loop (inc 1), 1000 iterations

# 2 for loops (inc 3, inc 5) 1000/3 + 1000/5 = 333 + 200 = 533 iterations

# add multiples to a Set to elminate dupes

# sum all values of the Set

max = 1000
multiples = set()

for i in range(3, max, 3):
    multiples.add(i)

for i in range(5, max, 5):
    multiples.add(i)

sum_of_multiples = sum(multiples)

# THIS WORKS TOO
# potentially higher space complexity due to the creation of lists?
# sum_of_multiples = sum(set(list(range(3, max, 3)) + list(range(5, max, 5))))

print(f'Sum of multiples: {sum_of_multiples}')
