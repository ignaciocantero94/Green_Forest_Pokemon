import os
import readchar

from starting_battles import Fight

POS_X = 0
POS_Y = 1
my_position = [18, 10]
end_game = False
enemies = [[8, 8], [12, 5], [7, 1], [18, 4], [28, 9], [29, 6], [27, 2]]
victories = 0
finish = [[22, 0], [23, 0], [24, 0]]

# Map of the game
forest = """\
AAAAAAAAAAAAAAAAAAAAA   AAAAAAAAAAAAAA
A####        AAAAAA            ####AAA
A###               AAAAAA       #####A
A######   AAAAAA    AAAA#####     ###A
A#####     AAAAA       AAAAAAA     AAA
AAAAAAAA      AAAA#     #####        A
A######         AAA     ####     AA##A
A#########     AAAAAA      ##    ####A
AAAA             ######              A
A###     ####         #####    ####AAA
AAAAAAAAAAAAAAA        AAAAAAAAAAAAAAA\
"""
forest = [list(row) for row in forest.split("\n")]
MAP_WIDTH = len(forest[0])
MAP_HEIGHT = len(forest)

# Main Loop
while not end_game:
    os.system("clear")

    #Draw the limits of the map where the map is going to be and all the icons
    print("+" + "-" * MAP_WIDTH * 2 + "+")
    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")

        for coordinate_x in range(MAP_WIDTH):# Draw all the icons in the map
            icon = " "
            for foe in enemies: # This for is to draw the enmies on the map
                if foe[POS_X] == coordinate_x and foe[POS_Y] == coordinate_y:
                    icon = "*"
            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y: #Define my position
                icon = "@"
            elif forest[coordinate_y][coordinate_x] == "A":
                icon = "A"

            elif forest[coordinate_y][coordinate_x] == "#":
                icon = "#"

        # In this case the format is helping us to replace whatever we have in the print
            print(" {}".format(icon), end="")
        print("|")
    print("+" + "-" * MAP_WIDTH * 2 + "+")

    # Here is where we are starting the battles when the icon "@" is on "*"
    for foe in enemies:
        if my_position[POS_X] == foe[POS_X] and my_position[POS_Y] == foe[POS_Y]:
            if foe[POS_X] == 8 and foe[POS_Y] == 8:
                encounter = Fight() # Here we are calling to the class for start the battle
                result = encounter.battle_1() # Here we are calling the method that is into the class
                if result == "Win":
                    enemies.remove(foe) # Delete the current "*" from the map
                    victories += 1
                    print("Number of victories: {}".format(victories))
                elif result == "Lost":
                    print("Number of victories: {}".format(victories))
                elif result == "Run":
                    print("Number of victories: {}".format(victories))
                elif result == "Deny":
                    print("Number of victories: {}".format(victories))

            if foe[POS_X] == 12 and foe[POS_Y] == 5:
                encounter = Fight() # Here we are calling to the class for start the battle
                result = encounter.battle_2() # Here we are calling the method that is into the class
                if result == "Win":
                    enemies.remove(foe) # Delete the current "*" from the map
                    victories += 1
                    print("Number of victories: {}".format(victories))
                elif result == "Lost":
                    print("Number of victories: {}".format(victories))
                elif result == "Run":
                    print("Number of victories: {}".format(victories))
                elif result == "Deny":
                    print("Number of victories: {}".format(victories))

            if foe[POS_X] == 7 and foe[POS_Y] == 1:
                encounter = Fight() # Here we are calling to the class for start the battle
                result = encounter.battle_3() # Here we are calling the method that is into the class
                if result == "Win":
                    enemies.remove(foe) # Delete the current "*" from the map
                    victories += 1
                    print("Number of victories: {}".format(victories))
                elif result == "Lost":
                    print("Number of victories: {}".format(victories))
                elif result == "Run":
                    print("Number of victories: {}".format(victories))
                elif result == "Deny":
                    print("Number of victories: {}".format(victories))

            if foe[POS_X] == 18 and foe[POS_Y] == 4:
                encounter = Fight() # Here we are calling to the class for start the battle
                result = encounter.battle_4() # Here we are calling the method that is into the class
                if result == "Win":
                    enemies.remove(foe) # Delete the current "*" from the map
                    victories += 1
                    print("Number of victories: {}".format(victories))
                elif result == "Lost":
                    print("Number of victories: {}".format(victories))
                elif result == "Run":
                    print("Number of victories: {}".format(victories))
                elif result == "Deny":
                    print("Number of victories: {}".format(victories))

            if foe[POS_X] == 28 and foe[POS_Y] == 9:
                encounter = Fight() # Here we are calling to the class for start the battle
                result = encounter.battle_5() # Here we are calling the method that is into the class
                if result == "Win":
                    enemies.remove(foe) # Delete the current "*" from the map
                    victories += 1
                    print("Number of victories: {}".format(victories))
                elif result == "Lost":
                    print("Number of victories: {}".format(victories))
                elif result == "Run":
                    print("Number of victories: {}".format(victories))
                elif result == "Deny":
                    print("Number of victories: {}".format(victories))

            if foe[POS_X] == 29 and foe[POS_Y] == 6:
                encounter = Fight() # Here we are calling to the class for start the battle
                result = encounter.battle_6() # Here we are calling the method that is into the class
                if result == "Win":
                    enemies.remove(foe) # Delete the current "*" from the map
                    victories += 1
                    print("Number of victories: {}".format(victories))
                elif result == "Lost":
                    print("Number of victories: {}".format(victories))
                elif result == "Run":
                    print("Number of victories: {}".format(victories))
                elif result == "Deny":
                    print("Number of victories: {}".format(victories))

            if foe[POS_X] == 27 and foe[POS_Y] == 2:
                encounter = Fight() # Here we are calling to the class for start the battle
                result = encounter.battle_7() # Here we are calling the method that is into the class
                if result == "Win":
                    enemies.remove(foe) # Delete the current "*" from the map
                    victories += 1
                    print("Number of victories: {}".format(victories))
                elif result == "Lost":
                    print("Number of victories: {}".format(victories))
                elif result == "Run":
                    print("Number of victories: {}".format(victories))
                elif result == "Deny":
                    print("Number of victories: {}".format(victories))

    for f in finish:
        if my_position[POS_X] == f[POS_X] and my_position[POS_Y] == f[POS_Y]:
            print("Congratulation, you´ve manage to get out of the Green Forest,\n"
                  "see you soon!!")
            print("Number of victories: {}".format(victories))
            break

    print("Make your movements with (wasd)\n " # Make movements
          "press (q) to exit")
    movement = readchar.readchar()
    new_x, new_y = my_position[POS_X], my_position[POS_Y] # Make copies of our position
    if movement == "w":
        new_y -= 1
    elif movement == "s":
        new_y += 1
    elif movement == "a":
        new_x -= 1
    elif movement == "d":
        new_x += 1
    elif movement == "q":
        end_game = True

# Here we are defining the edges of the map and a copy of our last position to decide if we are moving forward or not
# if we are finding the simbol "A"
    if movement in ("w", "s", "a", "d"):
        map_edge = 0 <= new_y < MAP_HEIGHT and 0 <= new_x < MAP_WIDTH
        if map_edge and forest[new_y][new_x] != "A":
            my_position[POS_X] = new_x
            my_position[POS_Y] = new_y


if end_game:
    print("You finished")
