#Nested Dictionary.
world = {
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

#Display Oakwood
print(world[(0,0)]['name'])


#Print Dragons Peak name and danger level
print(f"At location 2,3 is {world[(2,3)]['name']}")
print(f"Danger scale from 1 to 10 is: {world[(2,3)]['danger']}")


#Increase danger for Ironhold
world[(4,2)]['danger'] = 2
print(f"Danger has increased for {world[(4,2)]['name']} to {world[(4,2)]['danger']}.")


world[(1,1)] = {
'name': 'Ashenwoods',
'type': 'forest',
'danger': 3}

print(f"New location {world[(1,1)]}")

# coordinate and location name
for key, value in world.items():
    print(key, value['name'])
    

def display_location(world: dict, position: tuple[int, int]):
 location = world[position]
 print(f"Name: {location['name']}")
 print(f"Type: {location['type'].capitalize()}")
 print(f"Danger level: {location['danger']}" )
    


current_loc_test = (1,1)
display_location(world, current_loc_test)
