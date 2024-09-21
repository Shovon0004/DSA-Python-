stock_prices=[230,324,223,123,568]
print(stock_prices[0])
print(stock_prices[3])
for i in range(len(stock_prices)):
    if stock_prices[i]==230:
        print(i)
for price in stock_prices:
    print (price)   
stock_prices.insert(1,999)         