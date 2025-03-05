#Prog01: Create a program that ask user to input 2 numbers. Print the smaller number.
num_01 = int(input("Enter first number: "))
num_02 = int(input("Enter second number: "))
print("\nThe smaller number is:", num_01 if num_01 < num_02 else num_02 if num_02 < num_01 else " ")
