#Problem1: Space Crew
#Given two lists of length n, crew and position, map the space station crew to their position on board the international space station.
#Each crew member crew[i] has job position[i] on board, where 0 <= i < n and len(crew) == len(position).
#Hint: Introduction to dictionaries
def space_crew(crew, position):
    #create your dictionary 
    my_dict={}
    #the one we're traversing doesn't really matter since they both have the same length
    #since we want crew to be first I just kinda used it first but it really doesnt matter
    for i in range(len(crew)):
        #save that specific crew as a key in dictionary and assign it the value of what position has in that specific index
        my_dict[crew[i]]=position[i]
        
    #then return it once we're done going through all the lists
    return my_dict

#Problem2: Space Encyclopedia 
#Given a dictionary planets that maps planet names to a dictionary containing the planet's number of moons and orbital period, 
# write a function planet_lookup() that accepts a string planet_name and returns a string 
# in the form Planet <planet_name> has an orbital period of <orbital period> Earth days and has <number of moons> moons. 
# If planet_name is not a key in planets, return "Sorry, I have no data on that planet.".

def planet_lookup(planet_name):
    planetary_info = {
    "Mercury": {
        "Moons": 0,
        "Orbital Period": 88
    },
    "Earth": {
        "Moons": 1,
        "Orbital Period": 365.25
    },
    "Mars": {
        "Moons": 2,
        "Orbital Period": 687
    },
    "Jupiter": {
        "Moons": 79,
        "Orbital Period": 10592
    }
}
    if planet_name in planetary_info:
        return f"Planet {planet_name} has an orbital period of {planetary_info[planet_name]["Orbital Period"]} Earth days and has {planetary_info[planet_name]["Moons"]} moons. "
    else:
        return f"Sorry, I have no data on that planet."


#Problem 3: Breathing Room
#As part of your job as an astronaut, you need to perform routine safety checks. 
# You are given a dictionary oxygen_levels which maps room names to current oxygen levels 
# and two integers min_val and max_val specifying the acceptable range of oxygen levels. 
# Return a list of room names whose values are outside the range defined by min_val and max_val (inclusive).

def check_oxygen_levels(oxygen_levels, min_val, max_val):
    my_list=[]

    for room, level in oxygen_levels.items():
        if level <min_val or level>max_val:
            my_list.append(room)
    return my_list


oxygen_levels = {
    "Command Module": 21,
    "Habitation Module": 20,
    "Laboratory Module": 19,
    "Airlock": 22,
    "Storage Bay": 18
}

min_val = 19
max_val = 22

print(check_oxygen_levels(oxygen_levels, min_val, max_val))
