#This code prompts the user to enter a number and then prints the multiplication table for that number from 1 to 10.
 # Example usage:
# If the user inputs 5, the output will be:
# 5 x 1 = 5
# 5 x 2 = 10



number = int(input('Enter a number to see its multiplication table: '))

for num in range(1, 11):
    result = num * number
    print(f'{number} * {num} = {result}')
