
numbers = []


for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)


largest_number = max(numbers)
print(f"The largest number is: {largest_number}")
