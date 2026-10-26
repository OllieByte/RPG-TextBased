#Dictionary {key,value}
player_stats = {
    "name": "Ollie",
    "health": 100,
    "level": 1,
    "experience": 0
}

#List [var, var]
player_inventory = ["dagger", "sword", "scimitar"]

#Tuple (var, var)
player_position = (0, 0)

#Set {var, var}
player_visited_locations = {"Village", "Forest"}



#Display the players stats and current position
def display_player_stats(stats: dict):
    print("\nCHARACTER STATS")
    for key, value in stats.items():
        print(f"{key.capitalize()}: {value}")


def display_player_inventory(items: list[str]):
    print("\nINVENTORY")
    for num, item in enumerate(items, start=1):
        print(f"{num}. {item}")


def display_player_locations(locations: set[str],  position: tuple):
    print("\nDISCOVERED LOCATIONS")
    for place in locations:
        print(f"- {place}")
    print(f"Position: {position}")


def check_inventory(item: str, inventory: list[str]):
    if item in inventory:
        print(f"{item.capitalize()} available!")
    else:
        print(f"No {item}s available.")


def add_item_to_inventory(item: str, inventory: list[str]):
    inventory.append(item)
    print(f"Added {item} to inventory.")



def player_movement(pos: tuple[int, int]):
    #x = East+ West- | y = North+ South-
    x, y = pos
    direction_prompt = ('Which direction would you like to move?\n'
                        '1.North\n'
                        '2.East\n'
                        '3.South\n'
                        '4.West\n'
                        '5.Exit Movement:\n'
                        'Enter your choice: ')
    choice = input(direction_prompt).strip()

    while choice != "5":
        if choice == "1": #north
            y += 1
        elif choice == "2": #east
            x += 1
        elif choice == "3": #south
            if y <= 0:
                print('That direction will put you off the map. Try again.')
            else:
                y -= 1
        elif choice == "4": #west
            if x <= 0:
                print('That direction will put you off the map. Try again.')
            else:
                x -= 1
        else:
            print("Invalid choice. Try again.")

        choice = input(direction_prompt).strip()

    new_position = (x,y)
    return new_position


def explore_location(visited: set[str], stats: dict, new_loc: str):
    new_loc = new_loc.capitalize()

    if new_loc not in visited:
        print(f"{new_loc.capitalize()} has been explored!.")
        stats["experience"] += 25
        visited.add(new_loc)
    else:
        print(f"{new_loc.capitalize()} has already been explored.")


def character_manager(stats: dict, position: tuple, inventory: list[str], locations: set[str]):

    print("\n========== RPG CHARACTER MANAGER ==========")
    display_player_stats(stats)
    display_player_inventory(inventory)
    display_player_locations(locations,position)
    print("===========================================\n")


def player_menu():
    print('\nMENU')
    print('1. Character Stats')
    print('2. Inventory')
    print('3. Explored Locations')
    print('4. Movement')
    print('5. Exit')



if __name__ == '__main__':
    while True:
        player_menu()
        choice = input("What would you like to do? ").strip()

        if choice == "1":
            display_player_stats(player_stats)
        elif choice == "2":
            display_player_inventory(player_inventory)
        elif choice == "3":
            display_player_locations(player_visited_locations, player_position)
        elif choice == "4":
            player_position = player_movement(player_position)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

    print("Thank you for playing!.")