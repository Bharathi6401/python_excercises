def find_largest(numbers):
    largest=float('-inf')
    for num in numbers:
        if not numbers:
            return None

        if num > largest:
            largest=num
    return largest

print(find_largest(numbers = (10, 45, 20, 80, 35)))