# This program draws a square pattern of asterisks based on user input.


positive_number = int(input('Enter the size of the pattern: '))

row = 0
while row < positive_number:

    for i in range(positive_number):
        print('*', end="")
    print()
    row += 1

    