#Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.
count = 0
for i in range(1, 11):
    num = int(input(f"Enter number {i}: "))
    count += 1 if num % 2 == 0 else 0
print(f"\nThere are {count} even numbers")
