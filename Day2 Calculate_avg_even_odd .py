import random

sum = 0
odd = 0
even = 0

for i in range (50):
    inp = random.randint(1, 100)
    print(f"Random interger {i+1}: {inp}")
    sum += inp
    if inp % 2 == 0:
        even += 1
    else:
        odd += 1

avg = sum / 50
print(f"Sum: {sum}")
print(f"odd count: {odd}")
print(f"even count: {even}")
print(f"Average: {avg}")