# Do not change the following 4 lines:
budget = int(input())
project1 = int(input())
project2 = int(input())
project3 = int(input())

total_project_sum = project1 + project2 + project3

# Fill in the missing code below
if total_project_sum <= budget:
    print("Budget is sufficient.")
else:
    print("Budget is insufficient.")