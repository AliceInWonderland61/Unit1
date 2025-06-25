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


#Problem 4:  Experiment Analysis
#Write a function data_difference() that accepts two dictionaries experiment1 and experiment2 and 
# returns a new dictionary that contains only key-value pairs found exclusively in experiment1 but not in experiment2.


def data_difference(experiment1, experiment2):
    only_one={}

    for data in experiment1:
        #if this specific data is not in experiment2
        #so we also compare everything not just the key 
        if data not in experiment2 or experiment1[data]!=experiment2[data]:
            #then we add it to our dictionary 
            only_one[data]=experiment1[data]
    return only_one



#Problem 5: Name the Node
#NASA has asked the public to vote on a new name for one of the nodes in the International Space Station. 
# Given a list of strings votes where each string in the list is a voter's suggested new name, 
# implement a function get_winner() that returns the suggestion with the most number of votes.
#If there is a tie, return either option.

def get_winner(votes):
    voters={}
    for i in votes:
        if i in voters:
            voters[i]+=1
        else:
            voters[i]=1

    ascending=sorted(voters.items(), key=lambda x: x[1], reverse=True)
    #ascening is treating this like a list so we need to output [0][0]
    #first [0] is the first item they have in the list
    #second [0]is now going into the items (there's 2 name and vote) and get the first item which is the name 
    return ascending[0][0]

#Problem 6: Check if the Transmission is Complete
#Ground control has sent a transmission containing important information. 
# A complete transmission is one where every letter of the English alphabet appears at least once.
#Given a string transmission containing only lowercase English letters, return true if the transmission is complete, or false otherwise.

def check_if_complete_transmission(transmission):
    
