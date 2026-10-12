items = []
prices = []


budget = int(input("Input Budget : "))
try:
    while True:
        item = input("Input Item : ")
        if item == "checkout":
            break
        items.append(item)
        price = float(input("Input Price : "))
        prices.append(price)

        total_price = sum(prices)

        if total_price > budget:
            print(f"Warning: You have exceeded your budget by {total_price - budget:.2f}")

except ValueError:
    pass

print("=" * 30)
print("      GROCERY RECEIPT      ")
print("=" * 30)
for product in range(len(items)):
    print(f"{items[product]}   :   ${prices[product]}")
print("-" * 30)
print(f"TOTAL SPENT :   ${sum(prices):.2f}")





