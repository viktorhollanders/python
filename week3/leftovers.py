number_of_players = int(input())

while number_of_players  < 2:
    number_of_players = int(input())

player_count = number_of_players
sum = 0 

while player_count > 0:
    number = int(input())
    sum += number
    player_count -= 1 

remainder = sum % number_of_players

print(f"The sum of all contributions is {sum} \n When {sum} is divided by {number_of_players}, the remainder is {remainder} \n Player {remainder} is the winner!")
