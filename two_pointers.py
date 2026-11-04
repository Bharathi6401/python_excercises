def move_zero_to_end(numbers):
    write_index=0
    
    for num in numbers:
        if num != 0:
            numbers[write_index] = num
            write_index += 1

    # Step 2: Fill the remaining spots at the end of the list with zeros
    while write_index < len(numbers):
        numbers[write_index] = 0
        write_index += 1
    return numbers


print(move_zero_to_end(numbers = [0, 1, 0, 3, 12, 0, 5]))
# # Move negative numbers to the left
# def move_negative_numbers(numbers):
#     left = 0
#     right = len(numbers) - 1
#     while left < right:
#         if numbers[left] < 0:
#             left +=1
#         elif numbers[right]>=0:
#             right -=1
#         else:
#             numbers[left], numbers[right] = numbers[right], numbers[left]
#             left+=1
#             right-=1
#     return numbers


# print(move_negative_numbers(numbers = [3, -1, 5, -7, 2, -4, 8]))
# def remove_duplicates(numbers):
#     i=0
#     j= 1
#     while j < len(numbers):
#         if numbers[i] == numbers[j]:
#             j+=1
#         else:
#             i+=1
#             numbers[i]= numbers[j]
#             j+=1
#     return numbers[:i+1]


# print(remove_duplicates([1, 1, 2, 2, 3, 4, 4, 5]))
# print(remove_duplicates([1, 1, 1, 1]))
# print(remove_duplicates([1, 2, 3, 4]))


# def merge_sorted_lists(list1, list2):
#     i = 0
#     j = 0
#     result = []

#     while i < len(list1) and j < len(list2):
#         # Compare both values
#         if list1[i]< list2[j]:
#             result.append(list1[i])
#             i+=1
#         else:
#             result.append(list2[j])
#             j+=1
    
#     while i < len(list1):
#         result.append(list1[i])
#         i+=1
#     while j < len(list2):
#         result.append(list2[j])
#         j+=1


#     return result


# print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))
# print(merge_sorted_lists([1, 5, 9], [2, 3]))
# print(merge_sorted_lists([], [2, 4, 6]))
# def two_sum_pointers(numbers,target):
#     left=0
#     right=len(numbers)-1
#     while left < right:
#         total=numbers[left] + numbers[right]
#         if total == target:
#             return [numbers[left], numbers[right]]
#         elif total < target:
#             left+=1
#         else:
#             right-=1

# print(two_sum_pointers([1,2,4,6,8,9], 10))
# def is_palindrome(numbers):
#     left=0
#     right=len(numbers)-1
#     while left < right:
#         if numbers[left] != numbers[right]:
#             return False
#         left+=1
#         right-=1
#     return True

# print(is_palindrome([1, 2, 3, 2, 1]))
# print(is_palindrome([1, 2, 3, 4]))
# print(is_palindrome([5, 5]))


# numbers = [10, 20, 30, 40, 50]
# left=0
# right=len(numbers)-1

# while left< right:
#     numbers[left], numbers[right] = numbers[right], numbers[left]
#     left+=1
#     right-=1


# print(numbers)

# numbers = [5, 10, 15, 20, 25]

# left = 0
# right = len(numbers) - 1

# while left <= right:
#     if left < right:
#         print(numbers[left])
#         print(numbers[right])
#         left +=1
#         right-=1
# if left == right:
#     print(numbers[left])

    

# numbers = [5, 10, 15, 20, 25]

# left = 0
# right = 4

# left += 1
# right -= 1

# print(numbers[left])
# print(numbers[right])

# numbers = [5, 10, 15, 20, 25]

# left = 0
# right = len(numbers) - 1

# print(numbers[left])
# print(numbers[right])