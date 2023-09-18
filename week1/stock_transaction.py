symbol = input("The stock symbol: ")
nshares = int(input("Number of shares: "))
bprice = float(input("The stock buying price: "))
sprice = float(input("The stock selling price: "))

total_buy_price = round(bprice * nshares, 2)
buy_commission = total_buy_price * 0.03
total_sell_price = round(sprice * nshares, 2)
sell_commission = total_sell_price * 0.03
profit_loss = (total_sell_price - sell_commission) - (total_buy_price + buy_commission)

print("Transactions for stock: {}".format(symbol))
print("Bought {} shares @ {}".format(nshares, bprice))
print("Paid {}".format(total_buy_price))
print("Commission when buying: {}".format(buy_commission))
print("Sold {} shares @ {}".format(nshares, sprice))
print("Received {}".format(total_sell_price))
print("Commission when selling: {}".format(sell_commission))
print("Profit or loss: {}".format(profit_loss))



