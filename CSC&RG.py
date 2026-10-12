cart = []

total_amount = 0

discount = 10 * total_amount / 100

number = 0

print("---Welcome to PythonMart---")

while True:
    item = input("What item are you buying: ")
    if item == "checkout" :
        break
    cost = float(input("How much does it cost: "))
    cart.append((item, cost))

for product in cart:
    total_amount += product[1]

discount = 10 * total_amount / 100

coupon = input("Enter a coupon code (press enter to skip): ")
if coupon == "SAVE10":
    total_amount = total_amount - discount
else:
    discount = 0
total_tax = 8 * total_amount / 100
total_amount = total_amount + total_tax

sub_total = (total_amount + discount) - total_tax

print()
for product in cart:
    number += 1
    print(f"{number}. {product[0]} = Php {product[1]:.2f}")
print(f"Subtotal: {sub_total:.2f}")
print(f"Discount: {discount:.2f}")
print(f"Tax: {total_tax:.2f}")
print(f"Grand Total: {total_amount:.2f}")
print("-"*20)