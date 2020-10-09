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
room_visits = {}


while len(traversal_graph) != 500:
    # If the current room isn't in the traversal graph, add it.
    if player.current_room.id not in traversal_graph:
        traversal_graph[player.current_room.id] = {}
    
    # If the current room isn't in room visits, add it with a one.
    if player.current_room.id not in room_visits:
        room_visits[player.current_room.id] = 1

    # If it's in room visits, add a one because we're visiting it again.
    else:
        room_visits[player.current_room.id] += 1

    # This section finds all the surrounding rooms and puts them in our traversal graph
    # it also puts the rooms in rooms visited but with a zero since we haven't
    # actually visited them yet.
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

    # This section looks at all the options for next room to go into
    # If we've been in them the same number of times, it favors going
    # south, then east, then north, then west.
    # Otherwise, it chooses the room we've been in the fewest times.
    # This keeps us from getting stuck in loops of going back and forth
    # between the same two or three rooms.
    options = {}
    if player.current_room.s_to != None:
        options[room_visits[player.current_room.s_to.id]] = 's'
    if player.current_room.e_to != None:
        options[room_visits[player.current_room.e_to.id]] = 'e'        
    if player.current_room.n_to != None:
        options[room_visits[player.current_room.n_to.id]] = 'n'   
    if player.current_room.w_to != None:
        options[room_visits[player.current_room.w_to.id]] = 'w'
    
    # Then we actually do the moving to that room and add it 
    # To the path. 
    x = options[min(options)]
    player.travel(x)
    traversal_path.append(x)


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
