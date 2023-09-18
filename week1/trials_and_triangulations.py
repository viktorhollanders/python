import math
a_str = input() # Do not change this line.
b_str = input() # Do not change this line.
c_str = input() # Do not change this line.
# Fill in the missing code below.

a = int(a_str)
b = int(b_str)
c = int(c_str)

s = (a + b + c) / 2

area = math.sqrt(s * (s - a) * (s - b) * (s - c))
print(area) # Change this line at your own peril.
