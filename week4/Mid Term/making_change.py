item_price = int(input())
ammount_paid = int(input())


# find remainder
remainder = ammount_paid - item_price


while remainder > 0:
    if remainder >= 20:
        bill = 20
    elif remainder >= 10:
        bill = 10
    elif remainder >= 5:
        bill = 5
    elif remainder >= 2:
        bill = 2
    elif remainder >= 1:
        bill = 1

    print(bill)
    remainder -= bill

    
