# def find_duplicate_chars(text):
#     duplicate={}
#     for char in text:
#      duplicate[char] = duplicate.get(char, 0) + 1
#     duplicates=[]
#     for char,count in duplicate.items():
#         if count> 1:
#             duplicates.append(char)

#     return duplicates
# print(find_duplicate_chars("aabbcca"))
# print(find_duplicate_chars("python"))
# print(find_duplicate_chars(""))




# def are_anagrams(str1, str2):
#     frequency = {}
#     if len(str1) != len(str2):
#         return False
#     for char in str1:
#         frequency[char]=frequency.get(char,0)+1
#     for char in str2:
#         frequency[char]=frequency.get(char,0)-1
#     return all(value == 0 for value in frequency.values())


# print(are_anagrams("listen", "silent"))  # True
# print(are_anagrams("hello", "world"))    # False
# print(are_anagrams("aab", "ab"))    

# def are_anagrams(str1, str2):
#     frequency1={}
#     frequency2={}
#     for char in str1:
#         frequency1[char] = frequency1.get(char, 0) + 1
#     for char in str2:
#         frequency2[char]=frequency2.get(char,0)+1

#     return frequency1 == frequency2

# print(are_anagrams("listen", "silent"))  # True
# print(are_anagrams("hello", "world"))    # False
# print(are_anagrams("aabb", "abab"))      # True
# print(are_anagrams("aab", "abb"))        # False

# def non_repeating_char(text):
#     frequency = {}

#     for char in text:
#         frequency[char] = frequency.get(char, 0) + 1

#     for char in text:
#         if frequency[char] == 1:
#             return char

#     return None
    
# print(non_repeating_char("aabbcc"))
# print(non_repeating_char("aabbcd"))
# print(non_repeating_char(""))

#character frequency
# def character_frequency(text):
#     frequency={}
#     for char in text:
#         if char in frequency:
#             frequency[char] = frequency.get(char, 0) + 1
#         else:
#             frequency[char]=1
            
#     return frequency


# print(character_frequency("programming"))
 # Reverse a string
# def reverse_string(text):
#     rev=""
#     for char in text:
#         rev=char+rev
#     return rev

# print(reverse_string(text="python"))
# def vowels_count(text):
#     vowels = "aeiou"
#     count = 0

#     for char in text:
#         if char in vowels:
#             count += 1

#     return count

# print(vowels_count("programming"))

# text = "python programming"
# vowels_count = 0
# consonants_count = 0
# for char in text:
#     if char.isalpha():
#         if char in "aeiou":
#             vowels_count += 1
#         else:
#             consonants_count += 1
# print("Vowels:", vowels_count)
# print("Consonants:", consonants_count)

# def is_palindrome(text):
#     text = text.lower()
#     cleaned = ""

#     for char in text:
#         if char.isalnum():
#             cleaned += char

#     rev = ""

#     for char in cleaned:
#         rev = char + rev

#     return cleaned == rev


# print(is_palindrome("A man a plan a canal Panama"))
# print(is_palindrome("A man, a plan, a canal: Panama"))
# print(is_palindrome("hello"))

# def character_frequecy(text):
#     text = text.lower()
#     frequency={}
#     for char in text:
#         frequency[char]=frequency.get(char,0)+1
#     return frequency

# print(character_frequecy("banana"))

# def finde_duplicates(text):
#     duplicate={}
#     for char in text:
#         duplicate[char]=duplicate.get(char,0)+1
#     duplicates=[]
#     for char, count in duplicate.items():
#         if count>1:
#             duplicates.append(char)
#     return duplicates

# print((finde_duplicates("programming")))
# def first_non_repeating_char(text):
#     frequency={}
#     for char in text:
#         frequency[char]=frequency.get(char,0)+1
#     for char in text:
#         if frequency[char]==1:
#             return char

# print(first_non_repeating_char("swiss"))