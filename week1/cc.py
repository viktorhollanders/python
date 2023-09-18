import math
x1_str = input() # Do not change this line.
y1_str = input() # Do not change this line.
x2_str = input() # Do not change this line.
y2_str = input() # Do not change this line.
# Convert strings to ints.
x1 = int(x1_str)
y1 = int(y1_str)

x2 = int(x2_str)
y2 = int(y2_str)
d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(d) # Change this line at your own peril.
