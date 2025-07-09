#  Creating Veriable and Assigning values
name = "Takrib Kadir"
age = "don't like to share"
height = 5.6
is_student = True
print(name);
print(age);
print(height);
print(is_student);

# Task 1. Create variables for your city (string), number of kids (int), and has_pet (boolean)

City = "Vancouver"
num_kid = 0
has_pet = False
print(City);
print(num_kid);
print(has_pet);

#Task 2. Change the value of your city variable to another city and print it

age = 29 # Happy Birthday
print("\nNew age after birthday:", age)

# Task 3.Using Variables in Expressions
# year_born = 2025 - age
# print("\nYear born:", year_born)

#  Task 3: Calculate the age your kids will be in 5 years and print
kid_age_in_5_years = num_kid + 5
print("kids age in 5 years (assuming starting age = num_kid):", kid_age_in_5_years);




# 4. Data Types Check
#print("\nType of name:", type(name))
#print("Type of age:", type(age))
#print("Type of height:", type(height))
#print("Type of is_student:", type(is_student))

# Task 4: Print the data type of your city, num_kids, and has_pet variables
print("Type of city:", type(City))
print("Type of num_kids:", type(num_kid))
print("Type of has_pet:", type(has_pet))

# 5. String Concatenation Using Variables
#greeting = "Hello, my name is " + name + " and I live in " + city + "."
#print("\n" + greeting)


# Task 5: Create a sentence introducing yourself using your variables and print it



my_intro = f"My name is {name}, I am {age} years old, and I live in {City}."
print(my_intro)