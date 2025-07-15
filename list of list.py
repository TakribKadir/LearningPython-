# 1. Creating a List of Lists (2D List)
scores = [
    [85, 92, 78],   # Student 1
    [76, 88, 90],   # Student 2
    [90, 91, 95]    # Student 3
]
print("Initial Scores:", scores)

# 2. Accessing Elements
print("Score of Student 1 in subject 2:", scores[0][1])
    #Task 1: Print score of Student 3 in Subject 3
print("Score of student 3 in subject 3:", scores[2][2])

# 3 Iterating through a List of Lists
print("All scores row by row.")
for student_scores in scores:
    print(student_scores)
# Print each individual score in a tabular format
print ("individual scores:")
for i, student_scores in enumerate(scores):
    for j, score in enumerate(student_scores):
        print(f"Student{i+1}, Subject{j+1}: {score}")

# 4. Adding a New Student's Scores
scores.append([88,79,85])
print("After adding student 4:", scores)
scores.append([70, 80, 90])
print ("After adding student 5:", scores)

# updating a value
