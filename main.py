# my company
owner = "Blessing Philips"
name = input("Enter your name, please\n")
print(f"You're welcome to {owner} 'Bot, {name}")
purchase = input(f"What would you like to purchase, {name}?\n")
if purchase == 'Robot':
    print(
        "Here are lists and prices of available 'bots\nBaby 'Bot : $15\nVacuum 'Bot : $40\nSmurf : $45\nDora : $48\nLady Bug : $50\nDog 'Bot : $60\nHuman 'Bot : $80")
else:
    print("Item not available")
choice = input(f"Please input your choice, {name}\n")
if choice == "Baby 'Bot":
    print(f"Baby 'Bot packed and delivered\nThanks {name}")
elif choice == "Vacuum 'Bot":
    print(f"Vacuum 'Bot packed and delivered\nThanks {name}")
elif choice == "Smurf":
    print(f"Smurf packed and delivered\nThanks {name}")
elif choice == "Dora":
    print(f"Dora packed and delivered\nThanks {name}")
elif choice == "Lady Bug":
    print(f"Lady Bug packed and delivered\nThanks {name}")
elif choice == "Dog 'Bot":
    print(f"Dog 'Bot packed and delivered\nThanks {name}")
elif choice == "Human 'Bot":
    print(f"Human 'Bot packed and delivered\nThanks for trading at {owner} 'Bot {name}")
else:
    print("Incorrect input")


