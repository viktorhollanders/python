price_input = float(input())

number_of_items = 0
total_price = 0.0
lowest_price = 0.0

if price_input > 0:
    total_price += price_input
    lowest_price = price_input


while price_input != 0:
    price_input = float(input())

    total_price += price_input

    if price_input <= lowest_price and price_input > 0:
        lowest_price = price_input

    number_of_items += 1


round_total_price = round(total_price, 1)


print(f"Number of items: {number_of_items}\nTotal price: {round_total_price}")

if number_of_items > 0:
    print(f"Lowest price: {lowest_price}")
