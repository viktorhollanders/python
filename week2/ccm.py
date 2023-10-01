temp_now = int(input())
temp_prev = int(input())

RAISE = "raise"
KEEP = "keep"
LOWER = "lower"
SHUTDOWN = "shutdown"

if temp_now >= 350:
    print(SHUTDOWN)
elif (temp_now > 300 and temp_now < temp_prev) or (temp_now < 300 and temp_now > temp_prev):
    print(KEEP)
elif temp_now < 300 and temp_now < temp_prev:
    print(RAISE)  
elif temp_now > 300 and temp_now >= temp_prev:
    print(LOWER)
else:
    print(KEEP)
