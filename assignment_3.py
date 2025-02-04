
# Objective: Write a program that takes a list of numbers and prints out the sum, average, and largest number in the list.



# Problem 1: Write a program that takes a list of numbers and prints out the sum of all the numbers in the list.



numbers_list = [1, 2, 4, 9, 10]

print('Numbers to sum: ', numbers_list)

result = sum(numbers_list)

print(f"The sum is: {result}")


# Problem 2: Write a program that takes a list of numbers and prints out the average of all the numbers in the list.

numbers_list = [1, 2, 3, 4, 10]

print('Numbers to average: ', numbers_list)

result = sum(numbers_list)/len(numbers_list)

print(f'The average is: {result}')

# Problem 3: Write a program that takes a list of numbers and prints out the largest number in the list.

numbers_list = [200, 700, 400, 500, 250]

print('Finding the highest number of:', numbers_list)

result = max(numbers_list)

print(f'The highest number in the set is: {result}')

