water_available = 400
milk_available = 540
coffee_beans_available = 120
disposable_cups_available = 9
money_available = 550

espresso_supplies = [250, 0, 16, 1, 4]
latte_supplies = [350, 75, 20, 1, 7]
cappucino_supplies = [200, 100, 12, 1, 6]
all_supplies = [espresso_supplies, latte_supplies, cappucino_supplies]


def run_coffee_machine():
    while True:
        user_option = input("Write action (buy, fill, take, remaining, exit):")
        print("")
        if user_option == "exit":
            break
        elif user_option == "buy":
            buy_coffee()
        elif user_option == "fill":
            fill_supplies()
        elif user_option == "take":
            take_money()
        elif user_option == "remaining":
            print_remaining_supllies()


def take_money():
    global money_available
    print(f"I gave you ${money_available}", end="\n\n")
    money_available = 0


def print_remaining_supllies():
    print("The coffee machine has:")
    print(f"{water_available} of water")
    print(f"{milk_available} of milk")
    print(f"{coffee_beans_available} of coffee beans")
    print(f"{disposable_cups_available} of disposable cups")
    print(f"${money_available} of money", end="\n\n")


def buy_coffee():
    coffee_choice = input(
        "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappucino:")
    if coffee_choice == "1":  # espresso
        if has_enough_supplies(int(coffee_choice)):
            make_coffee_choice(250, 0, 16, 1, 4)
    elif coffee_choice == "2":  # latte
        if has_enough_supplies(int(coffee_choice)):
            make_coffee_choice(350, 75, 20, 1, 7)
    elif coffee_choice == "3":  # cappucino
        if has_enough_supplies(int(coffee_choice)):
            make_coffee_choice(200, 100, 12, 1, 6)

    print("")


def has_enough_supplies(coffee_choice: int):
    global all_supplies
    required_supplies = all_supplies[coffee_choice - 1]
    available_supplies = get_available_supplies()
    names_of_supplies = ["water", "milk", "coffee beans", "disposable cups"]
    has_enough_supplies = True

    supplies_num = len(required_supplies)
    for idx in range(supplies_num - 1):
        difference = available_supplies[idx] - required_supplies[idx]
        if difference < 0:
            print(f"Sorry, not enough {names_of_supplies[idx]}")
            has_enough_supplies = False
            break

    if has_enough_supplies:
        print("I have enough resources, making you a coffee!")

    return has_enough_supplies


def make_coffee_choice(water, milk, coffee_beans, disposable_cups, money):
    global water_available, milk_available, coffee_beans_available, disposable_cups_available, money_available
    water_available = water_available - water
    milk_available = milk_available - milk
    coffee_beans_available = coffee_beans_available - coffee_beans
    disposable_cups_available = disposable_cups_available - disposable_cups
    money_available = money_available + money


def fill_supplies():
    global water_available, milk_available, coffee_beans_available, disposable_cups_available, money_available
    water_available = water_available + \
        int(input("Write how many ml of water do you want to add:"))
    milk_available = milk_available + \
        int(input("Write how many ml of milk do you want to add:"))
    coffee_beans_available = coffee_beans_available + \
        int(input("Write how many grams of coffee beans do you want to add:"))
    disposable_cups_available = disposable_cups_available + \
        int(input("Write how many disposable cups do you want to add:"))
    print("")


def get_available_supplies():
    global water_available, milk_available, coffee_beans_available, disposable_cups_available, money_available
    return [water_available, milk_available, coffee_beans_available, disposable_cups_available, money_available]


# run_coffee_machine()