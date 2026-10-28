#Nested Dictionary.
#Established locations and positions
world_locations = {
(0,0): {
"name":"Oakwood",
"type": "village",
"danger": 0
},
(4,2): {
'name': 'Ironhold',
'type': 'city',
'danger': 1
},
(2,3): {
'name': "Dragon's Peak",
'type': 'mountain',
'danger': 8
}
}

#Established locations for random: Cities, Forests and Caves with danger rating.
locations_random = {
        'Ebonwharf': {
            'type': 'city',
            'danger': 3,
        },
        'Bronzekeep':{
            'type': 'city',
            'danger': 1,
        },
        'Glimmerpoint':{
            'type': 'city',
            'danger': 1,
        },
        'Madwall':{
            'type': 'city',
            'danger': 6,
        },

        'Mully Wood': {
            'type': 'forest',
            'danger': 2,
        },
        'Quiet Woods': {
            'type': 'forest',
            'danger': 6
        },
        'Ecksard Woodland': {
            'type': 'forest',
            'danger': 3,
        },

        'The Red Caverns': {
            'type': 'cave',
            'danger': 2,
        },
        'The Calmest Hollow': {
            'type': 'cave',
            'danger': 1,
        },
        'Dolshire Abyss': {
            'type': 'cave',
            'danger': 5,
        }
}




#Display Oakwood
print(world_locations[(0, 0)]['name'])


#Print Dragons Peak name and danger level
print(f"At location 2,3 is {world_locations[(2, 3)]['name']}")
print(f"Danger scale from 1 to 10 is: {world_locations[(2, 3)]['danger']}")


#Increase danger for Ironhold
world_locations[(4, 2)]['danger'] = 2
print(f"Danger has increased for {world_locations[(4, 2)]['name']} to {world_locations[(4, 2)]['danger']}.")


world_locations[(1, 1)] = {
'name': 'Ashenwoods',
'type': 'forest',
'danger': 3}

print(f"New location {world_locations[(1, 1)]}")

# coordinate and location name
for key, value in world_locations.items():
    print(key, value['name'])
    

def display_location(world: dict, position: tuple[int, int]):
 location = world[position]
 print(f"Name: {location['name']}")
 print(f"Type: {location['type'].capitalize()}")
 print(f"Danger level: {location['danger']}" )
    


current_loc_test = (1,1)
display_location(world_locations, current_loc_test)

print("\n\n")

def add_location(world_dict: dict, pos: tuple[int, int],loc: dict):
    if world_dict.get(pos):
        print("Location already exists")
    else:
        print("Location does not exist")
        world_dict[(pos)] =



current_loc_test = (5,5)
add_location(world_locations, current_loc_test, locations_random)

print(world_locations)