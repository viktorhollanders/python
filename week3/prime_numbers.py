n = int(input()) # Do not change this line
# Fill in the missing code below
# Do not change the lines below

is_prime = True
count = 2

if n == 1:
    is_prime = False

while count <= n / 2:

    if n % count == 0:
        is_prime = False
        break
    count += 1
        
if is_prime:
    print("Prime")
else:
    print("Not prime") 





