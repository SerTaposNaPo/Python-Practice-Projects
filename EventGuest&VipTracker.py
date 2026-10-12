guest_list = []
vip_list = []

def check_vip_status(ages):
    if ages >= 21:
        return True
    else:
        return False


def print_party_roster(vip, guests):
    print("\n🌟 VIP GUESTS 🌟")
    for person in vip:
        print(f"- {person}")

    print("\n🎉 REGULAR GUESTS 🎉")
    for person in guests:
        print(f"- {person}")

while True:
    guest = input("Enter Guest Name : ")
    if guest == "print":
        break
    age = int(input("Input Age: "))
    if check_vip_status(age):
        vip_list.append(guest)
    else:
        guest_list.append(guest)

print_party_roster(vip_list, guest_list)

