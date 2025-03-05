#Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.
for i in range(1, 11):
    num = int(input(f"Enter number {i}: "))
    first_num = num if i == 1 else first_num - num
print("\nThe result of the first number minus all of the remaining numbers is:", first_num)
