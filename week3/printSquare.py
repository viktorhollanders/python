size = int(input())

# Write your solution here below



star = "*"
line = ""

for i in range(0, size):
    for j in range(0, size):
        if j == size -1: 
            line += f"{star}\n"
        elif i == 0 or j == 0:
            line += f"{star} "
        # elif :
        #     line += f"{star} "
        elif i == size - 1:
            line += f"{star} "    
        else:
            line += "  "
       
print(line, end="")
  