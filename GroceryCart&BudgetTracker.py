items = []
prices = []

def buy_item(item_storage):
    item = input("Input Item: ")
    item_storage.append(item)

def item_prices(price_storage):
    price = float(input("Input Price: "))
    price_storage.append(price)

def design(prompt):
    print(prompt * 30)

def list_printer(lists):
    result_string = ""
    for item in range(len(lists)):
        result_string += str(lists[item])
    return result_string"\n"

budget = float(input("Input Budget: "))
try:
    while True:
        buy_item(items)
        if "checkout" in items:
            break
        item_prices(prices)
        total_price = sum(prices)
        if total_price > budget:
            exceed_budget = total_price - budget
            print(f"Warning: You have exceeded your budget by ${exceed_budget:.2f}")
            print(f"Current Total: ${total_price:.2f} | Budget: ${budget:.2f}")
except ValueError:
    pass

design("=")
print("      GROCERY RECEIPT      ")
design("=")

item_name = list_printer(items)
prices_value = list_printer(prices)

print(f"{item_name}  :  ${prices_value}")
design("-")
print(f"Total Spent  :  ${total_price}")
design("=")