from data import MENU, resources

current_resources = resources
money = 0
MACHINE_STATUS_ON = "on"
MACHINE_STATUS_OFF = "off"
PRINT_REPORT = "report"
CHOICE_LATTE = "latte"
CHOICE_ESPRESSO = "espresso"
CHOICE_CAPPUCCINO = "cappuccino"

machine_status = MACHINE_STATUS_ON

def printReport():
    """Prints a summary of current resources in the coffee machine and also the cash at hand"""
    print(f"Water: {current_resources['water']}ml")
    print(f"Milk: {current_resources['milk']}ml")
    print(f"Coffee: {current_resources['coffee']}g")
    print(f"Money: ${money}")

def checkResources(userChoice):
    """checks to see if we have the resources we need to make a drink"""
    required_resources = MENU[userChoice]['ingredients']
    for resource in list(required_resources.keys()):
        if current_resources[resource] < required_resources[resource]:
            print(f"Sorry there is not enough {resource}.")
            return False
    return True

def reduceResources(userChoice):
    """Reduce resources once a user can afford their drink.
    Input: user choice, Outputs: None """
    required_resources = MENU[userChoice]['ingredients']
    for resource in list(required_resources.keys()):
      current_resources[resource] -= required_resources[resource]

while machine_status == MACHINE_STATUS_ON:
    userChoice = input('What would you like? (espresso/latte/cappuccino): ').lower()

    if userChoice == MACHINE_STATUS_OFF:
        break;

    if userChoice ==  PRINT_REPORT:
        printReport();

    if userChoice ==  CHOICE_LATTE or userChoice ==  CHOICE_CAPPUCCINO  or userChoice ==  CHOICE_ESPRESSO:
        if checkResources(userChoice):
            print("Please insert coins")
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickels = int(input("how many nickels?: "))
            pennies = int(input("how many pennies?: "))
            total_money = round(quarters*.25 + dimes*.1 + nickels*.05 + pennies*.01,2)
            drink_cost = MENU[userChoice]['cost']

            if total_money >= drink_cost:
                reduceResources(userChoice)
                money += drink_cost
                balance = round(total_money - drink_cost,2)
                print(f"Here is ${balance} in change.")
                print(f"Here is your latte . Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")