# get and process input for a list of names
names =  input("Please input a list of names separated by commas\n").split(",")

# get and process input for a list of the number of assignments
assignments = []
while len(assignments) != len(names):
    if len(assignments) > 0:
        assignments = input("Please input the same number of assignments as the number of names in the first list\n").split(",")
    else:
        assignments = input("Please input now a list containing the number of assignments for each name of the first list\n").split(",")

# get and process input for a list of grades
grades = []
while len(grades) != len(names):
    if len(grades) > 0:
        grades = input("Please input the same number of grades as the number of names in the first list\n").split(",")
    else:
        grades = input("Please input a list containing the grades for each name of the first list").split(",")

## message string to be used for each student
## HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

## write a for loop that iterates through each set of names, assignments, and grades to print each student's message
for (name, assignment, grade) in zip(names, assignments, grades):
    tuple = (name, assignment, grade)
    print(message.format(tuple[0],tuple[1],tuple[2],int(tuple[2])+int(tuple[1])*2))
