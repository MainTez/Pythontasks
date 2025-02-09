s = input("Write here: ")

for symbol in set(s):
    print(f"Symbol {symbol} shows {s.count(symbol)} time")
