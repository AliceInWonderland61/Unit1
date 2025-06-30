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

  
    #so my thought process is to have the alphabet in a string and if we come across one of the letters we remove them
    alphabet=['a','b','c','d','e','f','g','h', 'i', 'j','k', 'l', 'm','n','o','p','q','r','s','t','u','v', 'w', 'x', 'y', 'z']
    #we start traversing the transmission and checking if that's in our alphabet
    for i in transmission:
        #if that char is in the alphabet we remove it from our alphabet
        if i in alphabet:
            alphabet.remove(i)
    #if the length of our alpbhabet is not zero then that means not all the letter of the alphabet were used in the string 
    if len(alphabet) !=0:
        return False
    return True


#Problem 7: Signal Pairs
#Ground control is analyzing signal patterns received from different probes. 
# You are given a 0-indexed array signals consisting of distinct strings.
#The string signals[i] can be paired with the string signals[j] if the string signals[i] is equal to the reversed string of signals[j]. 0 <= i < j < len(signals). 
# Return the maximum number of pairs that can be formed from the array signals.
#Note that each string can belong in at most one pair.

def max_number_of_string_pairs(signals):
    #so my idea is to create a dictionary and save the first string we see as the key and the reverse of it will be assigned as it's key
    #the next string we'll check our dictionary to see if it;s a key or a value 
    #if it's a new key we add it to our dictionary 
    #if it's a value then we increment our counter

    #create a dictionary to save the ones we've seen so far
    seen={} 
    #counter to count how many valid pairs we find 
    counter=0
    for i in signals:
        #reverse the current string we're at and save it to rev
        rev=i[::-1]
        #if that reverse string is in our dictionary then we increment our counter
        if rev in seen:
            counter+=1
            #delete that string so that we avoid reusing it 
            del seen[rev]
        else:
            seen[i]=True
    return counter

#Problem 8: Find the Difference of Two Signal Arrays
#You are given two 0-indexed integer arrays signals1 and signals2, representing signal data from two different probes. 
# Return a list answer of size 2 where:
#answer[0] is a list of all distinct integers in signals1 which are not present in signals2.
#answer[1] is a list of all distinct integers in signals2 which are not present in signals1.
#Note that the integers in the lists may be returned in any order.
#Below is the pseudocode for the problem. Implement this in Python and explain your implementation step-by-step.
'''
1. Convert signals1 and signals2 to sets.
2. Find the difference between set1 and set2 and store it in diff1.
3. Find the difference between set2 and set1 and store it in diff2.
4. Return the list [diff1, diff2].
'''

def find_difference(signals1, signals2):
    #convert signals1 and signals2 to sets
    set1=set(signals1)
    set2=set(signals2)

    #Find the difference between set1 and set2 and store it in diff1
    diff1=list(set1-set2)

    #Find the difference between set2 and set1 and store it in diff2
    diff2=list(set2-set1)

    #Return the list [diff1,diff2]
    return [diff1, diff2]



#Problem 9: Common Signals Between Space Probes
#Two space probes have collected signals represented by integer arrays signals1 and signals2 of sizes n and m, respectively. 
#Calculate the following values:
#answer1: the number of indices i such that signals1[i] exists in signals2.
#answer2: the number of indices j such that signals2[j] exists in signals1.
#Return [answer1, answer2].

def find_common_signals(signals1, signals2):
    #make them into sets 
    set1=set(signals1)
    set2=set(signals2)

    #counter to keep track of how many items in signals1 appear in signals2
    counter1=0
    for i in signals1:
        if i in set2:
            counter1+=1

    #counter to keep track of how many times in signals2 appear in signals1
    counter2=0
    for i in signals2:
        if i in set1:
            counter2+=1
    
    return [counter1, counter2]


#Problem 10: Common Signals Between Space Probes II
#If you implemented find_common_signals() in the previous problem using dictionaries, 
# try implementing find_common_signals() again using sets instead of dictionaries. 
# If you implemented find_common_signals() using sets, use dictionaries this time.
#Once you've come up with your second solution, compare the two. 
# Is one solution better than the other? How so? Why or why not?

#so i did sets before, I can do two dictionaries instead of sets and use two counters and return those 
def find_common_signals(signals1, signals2):
    dict_1={}
    dict2={}

    



