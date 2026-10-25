#Dictionary
player_stats = {

    "name": "Ollie",
    "health": 100,
    "level": 1,
    "experience": 0}

#List
player_inventory = ["dagger", "sword", "scimitar"]

#Tuple
player_position = (0, 0)

#Set
player_visited_locations = {"Village", "Forest"}

#Display the players stats and current position
def display_player_stats(stats: dict, position: tuple):
    print("\nCHARACTER STATS")
    for key, value in stats.items():
        print(f"{key.capitalize()}: {value}")
    print(f"Position: {position}")


def display_player_inventory(items: list[str]):

    print("\nINVENTORY")
    for num, item in enumerate(items, start=1):
        print(f"{num}. {item}")


def check_inventory(item: str, inventory: list[str]):

    if item in inventory:
        print(f"{item.capitalize()} available!")
    else:
        print(f"No {item}s available.")


def add_item_to_inventory(item: str, inventory: list[str]):
    inventory.append(item)
    print(f"Added {item} to inventory.")


def display_player_locations(locations: set[str]):

    print("\nDISCOVERED LOCATIONS")
    for place in locations:
        print(f"- {place}")


def player_movement(pos: tuple[int, int], direction: str):
    #East+ | West-
    x = pos[0]

    #North+ | South-
    y = pos[1]


    if direction == "north":
        y = y + 1
        new_pos = (x,y)
        return new_pos
    elif direction == "south":
        y = y - 1
        new_pos = (x,y)
        return new_pos
    elif direction == "east":
        x = x + 1
        new_pos = (x,y)
        return new_pos
    elif direction == "west":
        x = x - 1
        new_pos = (x,y)
        return new_pos
    else:
        print(f"{direction} is an invalid direction.")
        return pos


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
    display_player_stats(stats, position)
    display_player_inventory(inventory)
    display_player_locations(locations)
    print("===========================================\n")


def player_menu():
    print("\nMENU")
    print("1. Character Stats")
    print("2. Inventory")
    print("3. Explored Locations")
    print("4. Exit")



if __name__ == '__main__':
    while True:
        player_menu()
        choice = input("What would you like to do? ")

        if choice == "1":
            display_player_stats(player_stats, player_position)
        elif choice == "2":
            display_player_inventory(player_inventory)
        elif choice == "3":
            display_player_locations(player_visited_locations)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

    print("Thank you for playing!.")