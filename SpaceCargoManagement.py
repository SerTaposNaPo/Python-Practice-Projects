# The maximum capacities the spaceship can support
ship_resources = {
    "Weight Capacity (kg)": 5000,
    "Power Grid (kW)": 150
}

# The resource costs for each equipment module
cargo_modules = {
    "Hydroponics Farm": {"Weight Capacity (kg)": 3000, "Power Grid (kW)": 90},
    "Atmosphere Processor": {"Weight Capacity (kg)": 2500, "Power Grid (kW)": 50},
    "Comms Satellite Array": {"Weight Capacity (kg)": 1000, "Power Grid (kW)": 80}
}

def load_module(module):
    if module not in cargo_modules:
        print(f"The {module} does not exist in the equipment modules")
        return

    resource = cargo_modules[module]

    for resources, value in resource.items():
        available_resources = ship_resources.get(resources, 0)

        if available_resources < value:
            print(f"Sorry we dont have enough {resources}")
            return

    for resources, value in resource.items():
        ship_resources[resources] -= value

    print(f"You successfully get a {module}!")







# --- Test Cases to run your code ---
print("Initial Ship Resources:", ship_resources)
print("-" * 50)

# Test 1: Should succeed! (Weight drops to 2000, Power drops to 60)
print("Loading: Hydroponics Farm")
load_module("Hydroponics Farm")
print("Resources after Test 1:", ship_resources)
print("-" * 50)

# Test 2: Should fail! (Needs 50kW power, but only 60kW left. Wait... it fits! Weight fails: needs 2500kg but only 2000kg left)
print("Loading: Atmosphere Processor")
load_module("Atmosphere Processor")
print("-" * 50)

# Test 3: Should fail! (Module doesn't exist)
print("Loading: Warp Drive")
load_module("Warp Drive")