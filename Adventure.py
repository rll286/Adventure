# Randy Limon
# Simple text adventure game with random generation

import random
import time 
import sys

# List of names for towns
town_name = ['Aerilon ', 'Aquarin ', 'Aramoor ', 'Azmar ', 'Begger\'s_Hole ', 'Black_Hollow ', 
             'Blue_Field ', 'Briar_Glen ', 'Brickelwhyte ', 'Broken_Shield ', 'Boatwright ', 
             'Bullmar ', 'Carran ', 'City_of_Fire ', 'Coalfell ', 'Cullfield ', 'Darkwell ', 
             'Deathfall ', 'Doonatel ', 'Dry_Gulch ', 'Easthaven ', 'Ecrin ', 'Erast ', 'Far_Water ', 
             'Firebend ', 'Fool\'s_March ', 'Frostford ', 'Goldcrest ', 'Goldenleaf ', 'Greenflower ', 
             'Garen\'s_Well ', 'Haran ', 'Hillfar ', 'Hogsfeet ', 'Hollyhead ', 'Hull ', 'Hwen ', 
             'Icemeet ', 'Ironforge ', 'Irragin ', 'Jarren\'s_Outpost ', 'Jongvale ', 'Kara\'s_Vale ', 
             'Knife\'s_Edge ', 'Lakeshore ', 'Leeside ', 'Lullin ', 'Marren\'s_Eve ', 'Millstone ', 
             'Moonbright ', 'Mountmend ', 'Nearon ', 'New_Cresthill ', 'Northpass ', 'Nuxvar ', 
             'Oakheart ', 'Oar\'s_Rest ', 'Old_Ashton ', 'Orrinshire ', 'Ozryn ', 'Pavv ', 'Pella\'s_Wish ', 
             'Pinnella_Pass ', 'Pran ', 'Quan_Ma ', 'Queenstown ', 'Ramshorn ', 'Red_Hawk ', 'Rivermouth ', 
             'Saker_Keep ', 'Seameet ', 'Ship\'s_Haven','Silverkeep ', 'South_Warren ', 'Snake\'s_Canyon ', 
             'Snowmelt ', 'Squall\'s_End ', 'Swordbreak ', 'Tarrin ', 'Three_Streams ', 'Trudid ', 
             'Ubbin_Falls ', 'Ula\'ree ', 'Veritas ', 'Violl\'s_Garden ', 'Wavemeet ', 'Whiteridge ', 
             'Willowdale ', 'Windrip ', 'Wintervale ', 'Wellspring ', 'Westwend ', 'Wolfden ', 
             'Xan\'s_Bequest ', 'Xynnar ', 'Yarrin ', 'Yellowseed ', 'Zao_Ying ', 'Zeffari ', 'Zumka '
             ]
# Copy to replenish list 
TOWN_NAME_COPY = town_name.copy()

# Coordinates for player 
x_pos = random.randint(0,99)
y_pos = random.randint(0,99)

# Find line index for current cell
line_of_pos = y_pos*100+x_pos

# Master list for printing to save data
master_list = []
# Sublist for populating master list
sublist = []

# Random biome genertion
def biome():
    # List of possible biomes
    biome_list = ['Forest', 'Grasslands', 'Hills', 'Town']
    # Picks number for random generation
    biome_rng = random.randint(1,100)
    
    # Biome probability
    if biome_rng<11:
        biome = 3
    elif 10<biome_rng<41:
        biome = 0
    elif 40<biome_rng<71:
        biome = 1
    elif 70<biome_rng<101:
        biome = 2

    # Writing biome to sublit
    sublist.append(biome_list[biome])

    # Running town generation, otherwise writing filler data
    if biome == 3:
        town_gen(TOWN_NAME_COPY, town_name)
    else: 
        sublist.append('Na')
        sublist.append('Na')

# Generating town atributes
def town_gen(TOWN_NAME_COPY, town_name):
    # Generating random population
    town_population = str(random.randint(50, 10000))

    # Regenerating name list if empty
    if not town_name:
        town_name = list(TOWN_NAME_COPY)

    # Picking random index of town_name    
    town_name_rng = random.randint(0,len(town_name)-1)

    # Writing town attributes
    sublist.append(town_name[town_name_rng])
    sublist.append(town_population)
    
    # Removing used town name
    town_name.pop(town_name_rng)

# Populates save data with biome and town attributes
def generation():
    # Start timer for world generation
    start_time = time.time()

    # Calls biome generation 10,000 times
    for number in range(10000):
        biome()
        # Add new line to sublist
        sublist.append('\n')
        # Add sublist as a string to master_list
        master_list.append(' '.join(map(str, sublist)))
        # Clear sublist for new data
        sublist.clear()

    # Writes master_list to save data    
    with open('data.txt', 'a') as file:
        file.write(''.join(map(str, master_list)))

    # Indicates generation is done and gives load time        
    print('Generation Done in %s Seconds' %round((time.time() - start_time), 2))

# Start menue and initilization of gameplay loop
def start():
    print('-----Welcome to Your Adventure----')

    # Get input for menu and retry if input is invalid
    try:    
        start_option = int(input('1) Continue\n'+'2) New World\n'+'3) Exit\n'))
    except:
        start()

    # Option resolution
    if start_option == 3:
        sys.exit()
    elif start_option == 2:
        open('data.txt', 'w').close()
        generation()
    elif start_option == 1:
        # Check for save data and generate world if not
        try:
            open('data.txt', 'r').close()
            print('World Ready')
        except:
            generation()

    player_pos_init(x_pos, y_pos)

# Initilize player positon
def player_pos_init(x_pos, y_pos):

    # Get data on last line
    with open("data.txt","r") as file:
        lines = file.readlines()
    line = lines[-1]
    data = line.split()

    # Check for coordinate formating and set coordinates equal to saved coordinate data write coordinates if none  
    if len(data) == 2 and data[0].isdigit() and data[1].isdigit():
        x_pos = int(data[0])
        y_pos = int(data[1])
        simple_descriptions()
    # Write random coordinates if none in save  
    else:
        with open('data.txt', 'a') as file:
            file.write(str(x_pos)+' '+str(y_pos)+'\n')
        player_pos_init(x_pos, y_pos)

# Prints description of cell player is in        
def simple_descriptions():
    global x_pos, y_pos

    # Show player coordinates
    print('x:%s' %x_pos, 'y:%s' %y_pos)

    # Recalculate line index for current cell
    line_of_pos = y_pos*100+x_pos

    # Read cell data
    with open("data.txt","r") as file:
        lines = file.readlines()
    line = lines[line_of_pos]
    data = line.split()

    # Prints town information or current biome of cell
    if data[0] == 'Town':
        print('You are in the town of '+data[1].replace('_', ' ')+', with a population of '+data[2])
    else:
        print('You are in the %s' %data[0].lower())
    task_selection(line_of_pos)

# Give options for current cell
def task_selection(line_of_pos):
    # Read data for current cell
    with open("data.txt","r") as file:
        lines = file.readlines()
    line = lines[line_of_pos]
    data = line.split()

    print('-----What would you like to do?----')

    # Optins for forest and recursion for invalid option
    if data[0] == 'Forest':
        try:
            forest_task = int(input('1) Walk\n2) Forage\n3) Build shelter\n4) Harvest wood\n5) Save and exit\n'))
        except:
            task_selection(line_of_pos)
        handle_forest_task(forest_task)
    # Optins for generic biomes and recursion for invalid option
    elif data[0] == 'Grasslands' or data[0] == 'Hills':
        try:    
            task = int(input('1) Walk\n2) Forage\n3) Build shelter\n4) Save and exit\n'))
        except:
            task_selection(line_of_pos)
        handle_generic_task(task)
    # Optins for town and recursion for invalid option
    elif data[0] == 'Town':
        try:    
            task_town = int(input('1) Walk\n2) Visit shop\n3) View task board\n4) Save and exit\n'))
        except:
            task_selection(line_of_pos)
        handle_town_task(task_town)

# Handles forest selection
def handle_forest_task(forest_task):
    if forest_task == 1:
        movement()
    elif forest_task == 2:
        foraging()
    elif forest_task == 3:
        shelter()
    elif forest_task == 4:
        wood_harvest()
    elif forest_task == 5:
        save_exit()
    else:
        task_selection(line_of_pos)

# Handles generic biome selection
def handle_generic_task(task):
    if task == 1:
        movement()
    elif task == 2:
        foraging()
    elif task == 3:
        shelter()
    elif task == 4:
        save_exit()
    else:
        task_selection(line_of_pos)

# Handles town selection
def handle_town_task(task_town):
    if task_town == 1:
        movement()
    elif task_town == 2:
        shops()
    elif task_town == 3:
        task_board()
    elif task_town == 4:
        save_exit()
    else:
        task_selection(line_of_pos)

# Iterates coordinates for movement
def movement():
    global x_pos, y_pos

    print('------Where do you want to go?-----')

    # Get direction selection and retry if invalid input
    try:
        direction = int(input('1) North\n2) South\n3) East\n4) West\n5) Exit\n'))
    except:
        movement()

    # Iteratate coordinates depending on direction
    if direction == 1:
        y_pos += 1
        print('You walk 3 miles north')
    elif direction == 2:
        y_pos -= 1
        print('You walk 3 miles south')
    elif direction == 3:
        x_pos += 1
        print('You walk 3 miles east')
    elif direction == 4:
        x_pos -= 1
        print('You walk 3 miles west')
    elif direction == 5:
        task_selection()
    else:
        movement()

    # World wrap handling
    if y_pos > 99:
        y_pos = 0
    elif y_pos < 0:
        y_pos = 99
    if x_pos > 99:
        x_pos = 0
    elif x_pos < 0:
        x_pos = 99
    simple_descriptions()
        
def main():
    start()

main()