def calculate_average(numbers):
    total = 0

    for i in range(len(numbers) + 1):
        total += numbers[i]

    average = total / len(numbers)
    return average


numbers = [10, 20, 30, 40]
result = calculate_average(numbers)

print("Average:", result)
