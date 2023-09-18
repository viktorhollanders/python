year = int(input()) # Do not change this line
# Fill in the missing code below

if year % 400 == 0:
    print(True)  
elif year % 100 == 0:
   print(False)
elif year % 4 == 0:
    print(True)
else:
    print(False)

