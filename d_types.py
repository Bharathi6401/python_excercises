numbers = [10, 10, 10]

largest = float('-inf')
second_largest = float('-inf')
third_largest = float('-inf')

for num in numbers:
    if num > largest:
        third_largest = second_largest
        second_largest = largest
        largest = num

    elif num > second_largest and num != largest:
        third_largest = second_largest
        second_largest = num

    elif num > third_largest and num != largest and num != second_largest:
        third_largest = num

if third_largest == float('-inf'):
    print("No third-largest distinct number")
else:
    print(third_largest)







# numbers = [10, 5, 20, 5, 2, 8, 2]
# smallest=float('inf')
# second_smallest=float('inf')
# for num in numbers:
#     if num< smallest:
#         second_smallest=smallest
#         smallest=num
        
#     elif num < second_smallest and num != smallest:
#         second_smallest=num

# print(second_smallest)




# matrix = [
#     [10, 20, 30],
#     [5, 15, 25],
#     [2, 40, 6]
# ]
# largest=matrix[0][0]
# second_largest=float('-inf')
# for row in matrix:
#     for num in row:
#         if num >largest:
#             second_largest=largest
#             largest=num
#         elif num >second_largest and num != largest:
#             second_largest=num
# print(second_largest)
# matrix = [
#     [10, 20, 30],
#     [5, 15, 25],
#     [2, 40, 6]
# ]
# smallest=matrix[0][0]
# for row in matrix:
#     for num in row:
#         if num < smallest:
#             smallest=num
# print(smallest)
# list1 = [1, 2, 3, 2, 4, 5, 3]
# list2 = [3, 4, 6, 7]

# result = []
# seen = set()

# for item in list1:
#   if item in list2 and item not in seen:
#     result.append(item)
#     seen.add(item)

# print(result)  # Output: [3, 4]

# def find_first_non_repeating(numbers):
#     frequency = {}

#     for num in numbers:
#         frequency[num] = frequency.get(num, 0) + 1

#     for num in numbers:
#         if frequency[num] == 1:
#             return num

#     return None


# print(find_first_non_repeating(numbers = [1, 1, 2, 2, 3, 3]))
# matrix = [
#     [10, 20, 30],
#     [5, 15, 25],
#     [2, 40, 6]
# ]
# largest=matrix[0][0]
# for row in matrix:
#     for num in row:
#         if num >largest:
#             largest=num
# print(largest)
# matrix = [
#     [10, 20, 30],
#     [5, 15, 25],
#     [2, 4, 6]
# ]
# flat=0
# for row in matrix:
#     for num in row:
#         if num >10:
#             flat += num

# print(flat)
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# odd_squares=[num **2 for row in matrix for num in row if num % 2!=0]
# print(odd_squares)

# odd = []

# for row in matrix:
#     for num in row:
#         if num % 2 != 0:
#             num= num **2
#             odd.append(num)

# print(odd)
# def find_second_largest(numbers):

#     largest=float('-inf')
#     second_largest=float('-inf')
#     for num in numbers:
#         if num > largest:
#             second_largest=largest
#             largest=num
#         elif num >second_largest and num != largest:
#             second_largest=num
#     if second_largest == float('-inf'):
#         return None

#     return second_largest

# print(find_second_largest([10,10,10]))


# numbers = [18, 7, 25, 3, 12]
# smallest=numbers[0]
# for num in numbers:
#     if num<smallest:
#         smallest=num
# print(smallest)


# numbers = [0, 1, 0, 3, 12, 0, 5]

# # This pointer tracks the position where the next non-zero number should go

# write_index = 0

# # Step 1: Move all non-zero elements to the front of the list
# for num in numbers:
#     if num != 0:
#         numbers[write_index] = num
#         write_index += 1

# # Step 2: Fill the remaining spots at the end of the list with zeros
# while write_index < len(numbers):
#     numbers[write_index] = 0
#     write_index += 1

# print(f"Modified list: {numbers}")  # Output:

# def find_duplicates(numbers):
#     seen = []
#     duplicates = []

#     for num in numbers:
#         if num in seen:
#             if num not in duplicates:
#                 duplicates.append(num)
#         else:
#             seen.append(num)

#     return duplicates
# numbers = [1, 2, 3, 2, 4, 5, 1, 6]

# seen = []       
# duplicates = [] 

# for num in numbers:
#     if num in seen:
#         if num not in duplicates:
#             duplicates.append(num)
#     else:
#         seen.append(num)

# print(duplicates)  

# def get_second_largest(numbers):
#     if len(set(numbers)) < 2:
#         return None

#     largest = float('-inf')
#     second_largest = float('-inf')

#     for num in numbers:
#         if num > largest:
#             second_largest = largest
#             largest = num
#         elif num > second_largest and num != largest:
#             second_largest = num

#     return second_largest

# print(get_second_largest([10, 45, 20, 80, 60, 80]))
# print(get_second_largest([10, 10, 10]))
# print(get_second_largest([5, 9]))
# print(get_second_largest([4, 4, 7, 7, 2])) 

# Output: Error: List must contain at least two unique numbers

# numbers = [10, 45, 20, 80, 60, 80]

# largest=float('-inf')
# second_largest=float('-inf')

# for num in numbers:
#     if num>largest:
#         second_largest=largest
#         largest=num
#     elif num > second_largest and num!=largest:
#         second_largest=num


# print(f"Second largest number: {second_largest}") 





# numbers = [1, 2, 3]

# numbers.insert(1, 100)
# print(numbers)

# numbers.remove(2)
# print(numbers)

# removed = numbers.pop()
# print(numbers)
# print(removed)