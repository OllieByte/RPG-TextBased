position = (0,0)

def player_movement(pos: tuple[int, int]):
    # x = East+ West- | y = North+ South-
    x, y = pos
    direction_prompt = ('Which direction would you like to move?\n'
                        '1.North\n'
                        '2.East\n'
                        '3.South\n'
                        '4.West\n'
                        '5.Exit Movement:\n'
                        'Enter your choice: ')
    choice = input(direction_prompt)

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

        choice = input(direction_prompt)

    new_position = (x,y)
    return new_position




if __name__ == '__main__':
   position = player_movement(position)
   print(position)
   position = player_movement(position)
   print(position)
