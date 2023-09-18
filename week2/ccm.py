temp_now = int(input())
temp_prev = int(input())

RAISE = "raise"
KEEP = "keep"
LOWER = "lower"
SHUTDOWN = "shutdown"
# ... implement control logic and print the appropriate action

# if the current temperature is below 300◦C and the temperature is not rising then raise the control rods to increase temperature.

# if the current temperature is below 300◦C but the temperature is rising then keep the control rods where they are.

# if the current temperature is exactly 300◦C then keep the control rods where they are.

# if the current temperature is above 300◦C and the temperature is not falling then lower the control rods to reduce temperature.

# if the current temperature is above 300◦C but the temperature is falling then keep the control rods where they are.

# if the current temperature is 350◦C or higher then initiate emergency shut- down procedures.

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

    
# if temp_now >= 350:
#     print(SHUTDOWN)
# elif temp_now > 300:
#     if temp_now < temp_prev:
#         print(KEEP)
#     else:
#         print(LOWER)
# elif temp_now < 300:
#     if temp_now > temp_prev:
#         print(KEEP)
#     else:
#         print(RAISE)
# else:
#     print(KEEP)