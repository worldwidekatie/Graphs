from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "projects/adventure/maps/test_line.txt"
# map_file = "projects/adventure/maps/test_cross.txt"
# map_file = "projects/adventure/maps/test_loop.txt"
# map_file = "projects/adventure/maps/test_loop_fork.txt"
map_file = "projects/adventure/maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
# world.print_rooms()

player = Player(world.starting_room)

# # Fill this out with directions to walk
# # traversal_path = ['n', 'n']
traversal_path = []
traversal_graph = {}
room_path = []
room_visits = {}


while len(traversal_graph) != 500:

    if player.current_room.id not in traversal_graph:
        traversal_graph[player.current_room.id] = {}
    
    if player.current_room.id not in room_visits:
        room_visits[player.current_room.id] = 1
    
    else:
        room_visits[player.current_room.id] += 1

    if player.current_room.n_to != None:
        traversal_graph[player.current_room.id]['n'] = player.current_room.n_to.id
        if player.current_room.n_to.id not in room_visits:
            room_visits[player.current_room.n_to.id] = 0

    if player.current_room.s_to != None:
        traversal_graph[player.current_room.id]['s'] = player.current_room.s_to.id
        if player.current_room.s_to.id not in room_visits:
            room_visits[player.current_room.s_to.id] = 0
    if player.current_room.w_to != None:    
        traversal_graph[player.current_room.id]['w'] = player.current_room.w_to.id
        if player.current_room.w_to.id not in room_visits:
            room_visits[player.current_room.w_to.id] = 0
    if player.current_room.e_to != None:    
        traversal_graph[player.current_room.id]['e'] = player.current_room.e_to.id    
        if player.current_room.e_to.id not in room_visits:
            room_visits[player.current_room.e_to.id] = 0

    options = {}
    if player.current_room.s_to != None:
        options[room_visits[player.current_room.s_to.id]] = 's'
    if player.current_room.e_to != None:
        options[room_visits[player.current_room.e_to.id]] = 'e'        
    if player.current_room.n_to != None:
        options[room_visits[player.current_room.n_to.id]] = 'n'   
    if player.current_room.w_to != None:
        options[room_visits[player.current_room.w_to.id]] = 'w'
    x = options[min(options)]
    player.travel(x)
    traversal_path.append(x)
    room_path.append(player.current_room.id)   


# # TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



# #######
# # UNCOMMENT TO WALK AROUND
# #######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
