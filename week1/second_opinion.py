total_seconds_str = input() # Do not change this line.
# Convert to hours, minutes and seconds.
seconds_int = int(total_seconds_str)

hours =  seconds_int // 3600

seconds = seconds_int % 3600

minutes = seconds // 60

seconds = seconds % 60

print(hours, ":", minutes, ":", seconds) # Do not change this line.
