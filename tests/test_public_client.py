import gdax

client = gdax.PublicClient()

output = client.get_products()
print("get_products()")
print(output, "\n")

output = client.get_product_order_book(gdax.BTC_USD, 1)
print("get_product_order_book()")
print(output, "\n")

output = client.get_product_ticker(gdax.BTC_USD)
print("get_product_ticker()")
print(output, "\n")

output = client.get_trades(gdax.BTC_USD)
print("get_trades()")
print(output, "\n")

output = client.get_historic_rates(gdax.BTC_USD, "2018-01-01", "2018-01-02",
                                   granularity=300)
print("get_historic_rates()")
print(output, "\n")

output = client.get_currencies()
print("get_currencies()")
print(output, "\n")

output = client.time()
print("time()")
print(output, "\n")
