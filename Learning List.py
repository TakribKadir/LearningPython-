# Creating a List
fruits = ["apple", "banana", "cherry", "mango"]
print("Initial List:", fruits)

#Task 1: Add "orange" to the list and print the updated list
fruits.append("orange")
print ("After adding 'orange':", fruits)

#Accessing List Elements
print ("first fruit:", fruits[0])
print ("Last fruit:", fruits[-1])

# Task 2: Print the second and third fruits using slicing
print ("second and third fruits:", fruits[1:3])

#Modifying Elements
# Changing banana to blueberry
fruits[1]= "blueberry"
print ("After modification:", fruits)

#Task 3: Change "cherry" to "pineapple"
#fruits[2] = "pineapple"
#print("After Changing cherry to pineapple:", fruits[2])

#Alternative way

index_cherry = fruits.index("cherry")
fruits[index_cherry] = "pineapple"
print("After changing 'cherry' to 'pineapple':", fruits)

# Task 4: Add "lemon" at the beginning of the list

fruits.insert(0, "lemon")
print ("After adding 'lemon' at beginning:", fruits)

# Removing Items
# Removes first occurrence of "apple"
fruits.remove("apple")
# Removes last item
popped_fruits= fruits.pop()
print("After removing 'apple' and popping last item:", fruits)
print("Popped fruit:", popped_fruits)

#Task 5: Remove "mango" and print the list
fruits.remove("mango")
print("After removing 'mango':", fruits)

# Sorting and Reversing
fruits.sort()
print("sorted list", fruits)
fruits.reverse()
print("reversed list:", fruits)

# Task 6: Sort in reverse alphabetical order without changing original list

sorted_reversed = sorted(fruits, reverse=True)
print("Reverse-sorted (new list):", sorted_reversed)
print("Original list remains:", fruits)

# Iterating Over a List
print("Fruits one by one:" )
for fruit in fruits:
    print("Fruit:", fruit)

# Task 7: Print each fruit in uppercase
print("Fruits in uppercase:")
for fruits in fruits:
    print(fruits.upper())

# List Comprehension
fruits_length = [len(fruits) for fruits in fruits]
print("Lengths of each fruit name:", fruits_length)

# Task 8: New list with fruits containing the letter 'e'
fruits_with_e = [fruit for fruit in fruits if 'e' in fruit]
print("Fruits with 'e':", fruits_with_e)


# Given a list of prices, write a function to apply a discount
prices = [20, 30, 50, 100, 80]
 #def discounted = (prices, )
#print(discounted)
