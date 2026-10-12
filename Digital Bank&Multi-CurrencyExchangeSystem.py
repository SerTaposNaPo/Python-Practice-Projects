# The global exchange rates: How much 1 unit of currency is worth in USD
# Example: 1 EUR = 1.10 USD. 1 JPY = 0.007 USD.
from locale import currency
from threading import activeCount

EXCHANGE_RATES = {
    "USD": 1.00,
    "EUR": 1.10,
    "JPY": 0.007
}

# The database of user accounts and their current wallet balances
user_accounts = {
    "alice_travels": {"USD": 5000, "EUR": 200, "JPY": 0},
    "bob_crypto":    {"USD": 150,  "EUR": 0,   "JPY": 50000},
    "charlie_dev":   {"USD": 1200, "EUR": 800, "JPY": 10000}
}

# Pre-packaged travel bundles that users can purchase using USD
vacation_packages = {
    "Euro Trip Basic": {"EUR": 500, "JPY": 0},
    "Tokyo Neon Kit":   {"EUR": 0,   "JPY": 100000},
    "Global Explorer": {"EUR": 300, "JPY": 50000}
}

def purchase_package(account, package):

    if account not in user_accounts:
        print(f"{account} does not exist!")
        return

    if package not in vacation_packages:
        print(f"{package} is not available")
        return

    total_usd_needed = 0

    user = user_accounts[account]
    trip = vacation_packages[package]



    for cur, value in trip.items():
        total_usd_needed += (value * EXCHANGE_RATES[cur])

    if user["USD"] < total_usd_needed:
        print(f"Transaction Failed: {account} has {user["USD"]} but needs {total_usd_needed} USD.")
        return

    user["USD"] -= total_usd_needed

    print(f"The Payment for {package} has successfully deducted in {account}'s account")






















# --- Test Cases to run your code ---
print("Initial Accounts:", user_accounts)
print("-" * 60)

# Test 1: Should Succeed!
# Cost: (300 EUR * 1.10) + (50000 JPY * 0.007) = 330 + 350 = 680 USD.
# Alice has 5000 USD. 5000 - 680 = 4320 USD left. She gains 300 EUR and 50000 JPY.
print("Transaction 1: Alice buys Global Explorer")
purchase_package("alice_travels", "Global Explorer")
print("Alice's Final Balance:", user_accounts["alice_travels"])
print("-" * 60)

# Test 2: Should Fail! (Bob only has 150 USD, but the Tokyo kit costs 700 USD)
print("Transaction 2: Bob buys Tokyo Neon Kit")
purchase_package("bob_crypto", "Tokyo Neon Kit")
print("-" * 60)
#
# Test 3: Should Fail! (User doesn't exist)
print("Transaction 3: Unknown User")
purchase_package("hacker_cat", "Euro Trip Basic")