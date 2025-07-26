# # python_data_structures_tasks.py

# def task_1_sum_of_user_integers():
#     """
#     Task 1: Accepts user input to create a list of integers and computes their sum.
#     """
#     print("\n--- Task 1: Sum of User Integers ---")
#     integer_list = []
#     while True:
#         user_input = input("Enter an integer (or 'done' to finish): ")
#         if user_input.lower() == 'done':
#             break
#         try:
#             number = int(user_input)
#             integer_list.append(number)
#         except ValueError:
#             print("Invalid input. Please enter a whole number or 'done'.")

#     if integer_list:
#         total_sum = sum(integer_list)
#         print(f"\nThe list of integers you entered is: {integer_list}")
#         print(f"The sum of all integers in the list is: {total_sum}")
#     else:
#         print("\nNo integers were entered to sum.")
#     print("------------------------------------")


# def task_2_print_favorite_books():
#     """
#     Task 2: Creates a tuple containing the names of five favorite books and prints each on a separate line.
#     """
#     print("\n--- Task 2: Favorite Books Tuple ---")
#     favorite_books = (
#         "The Lord of the Rings",
#         "Pride and Prejudice",
#         "1984",
#         "To Kill a Mockingbird",
#         "Dune"
#     )

#     print("\nMy Favorite Books:")
#     for book in favorite_books:
#         print(book)
#     print("------------------------------------")


# def task_3_personal_info_dictionary():
#     """
#     Task 3: Uses a dictionary to store information about a person (name, age, favorite color).
#     Asks the user for input and stores the information in the dictionary, then prints it.
#     """
#     print("\n--- Task 3: Personal Info Dictionary ---")
#     person_info = {}

#     name = input("Enter your name: ")
#     age = input("Enter your age: ")
#     fav_color = input("Enter your favorite color: ")

#     person_info['name'] = name
#     person_info['age'] = age
#     person_info['favorite_color'] = fav_color

#     print("\n--- Person Information ---")
#     print(person_info)
#     print(f"Name: {person_info['name']}")
#     print(f"Age: {person_info['age']}")
#     print(f"Favorite Color: {person_info['favorite_color']}")
#     print("------------------------------------")


# def task_4_common_elements_in_sets():
#     """
#     Task 4: Accepts user input to create two sets of integers.
#     Then, creates a new set that contains only the elements common to both sets.
#     """
#     print("\n--- Task 4: Common Elements in Sets ---")

#     def get_integer_set(prompt):
#         """Helper function to get a set of integers from user input."""
#         while True:
#             numbers_str = input(f"Enter integers for {prompt} (comma-separated, e.g., 1,2,3): ")
#             try:
#                 # Filter out empty strings that result from trailing commas or multiple commas
#                 return set(int(num.strip()) for num in numbers_str.split(',') if num.strip())
#             except ValueError:
#                 print("Invalid input. Please enter integers separated by commas only.")
#                 continue # Ask again

#     set1 = get_integer_set("Set 1")
#     set2 = get_integer_set("Set 2")

#     if not set1 and not set2: # Both are empty due to bad input or no input
#         print("\nNo valid sets were created. No common elements to find.")
#     else:
#         common_elements = set1.intersection(set2) # Or set1 & set2

#         print(f"\nSet 1: {set1}")
#         print(f"Set 2: {set2}")
#         print(f"Common elements (intersection): {common_elements}")
#     print("------------------------------------")


# def task_5_words_with_odd_characters():
#     """
#     Task 5: Creates a program that stores a list of words. Then, uses list comprehension
#     to create a new list that contains only the words that have an odd number of characters.
#     """
#     print("\n--- Task 5: Words with Odd Characters ---")
#     word_list = [
#         "apple", "banana", "cat", "dog", "elephant",
#         "tree", "flower", "python", "code", "challenge",
#         "hello", "world", "odd"
#     ]

#     # Use list comprehension to filter words with an odd number of characters
#     odd_length_words = [word for word in word_list if len(word) % 2 != 0]

#     print(f"\nOriginal list of words: {word_list}")
#     print(f"Words with an odd number of characters: {odd_length_words}")
#     print("------------------------------------")


# # Main execution block
# if __name__ == "__main__":
#     print("Running Python Data Structures Tasks:")

#     # Uncomment the function call for the task you want to run.
#     # You can run them one by one, or all sequentially.

#     task_1_sum_of_user_integers()
#     # task_2_print_favorite_books()
#     # task_3_personal_info_dictionary()
#     # task_4_common_elements_in_sets()
#     # task_5_words_with_odd_characters()

#     print("\n--- All selected tasks finished. ---")



# Create an empty list called my_list
my_list = []

# Append the following elements to my_list: 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(f"After appending: {my_list}")

# Insert the value 15 at the second position in the list
my_list.insert(1, 15) # Index 1 is the second position
print(f"After inserting 15: {my_list}")

# Extend my_list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])
print(f"After extending: {my_list}")

# Remove the last element from my_list
my_list.pop() # Removes the last element by default
print(f"After removing last element: {my_list}")

# Sort my_list in ascending order
my_list.sort()
print(f"After sorting: {my_list}")

# Find and print the index of the value 30 in my_list
index_of_30 = my_list.index(30)
print(f"The index of 30 is: {index_of_30}")