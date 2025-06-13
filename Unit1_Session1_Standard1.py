#Problem 2: Write a function greeting() that accepts a single parameter, a string name, and prints the string "Welcome to The Hundred Acre Wood <name>! My name is Christopher Robin."

#single parameter
#string name -> we'll assign a name to this 
#print string, we need to call the name 

def greeting(name):
    print(f"Welcome to The Hundred Acre Wood, {name}. My name is Christopher Robin.")

# Problem 3: Catchphrase
#Write a function print_catchphrase() that accepts a string character as a parameter and prints the catchphrase of the given character as outlined in the table below.
# "Pooh" ->	"Oh bother!"
#"Tigger" -> "TTFN: Ta-ta for now!"
#"Eeyore"	"Thanks for noticing me."
#"Christopher Robin"	"Silly old bear."
# if character does not match: print "Sorry! I don't know <character>'s catchphrase!"


def print_catchphrase(character):
    if character == "Pooh":
        print("Oh bother!")
    
    elif character == "Tigger":
        print("TTFN: Ta-ta for now!")

    elif character == "Eeyore":
        print("Thanks for noticing me.")

    elif character == "Christopher Robin":
        print("Silly old bear.")
    
    else:
       print(f"Sorry! I don't know {character}'s catchphrase")





#Problem 4: Implement a function get_item() that accepts a 0-indexed list items and a non-negative integer x and returns the element at index x in items. If x is not a valid index of items, return None.

#function get_item()
#parameter is a list (array) & positive integer x

def get_item(items, x):    
    if x<0 or x >=len(items):
        return None
    
    else:
        return items[x]
    

#Problem 5: 
#Winnie the Pooh wants to know how much honey he has. 
# Write a function sum_honey() that accepts a list of integers hunny_jars and returns the sum of all elements in the list. 
# Do not use the built-in function sum().

def sum_honey(hunny_jars):
    total=0
    for i in range(len(hunny_jars)):
        total=total+hunny_jars[i]
    
    print("The sum of all the elements in the list is: ", total)


#Problem 6: Double Trouble
#Help Winnie the Pooh double his honey! 
# Write a function doubled() that accepts a list of integers hunny_jars as a parameter and multiplies each element in the list by two.
# Return the doubled list.

def doubled(hunny_jars):
    doubled=0
    for i in range(len(hunny_jars)):
        doubled=doubled+(hunny_jars[i]*2)
    
    print("After multiplying each element in the list by two, this is the total: ", doubled)


#Problem 7: PoohSticks
#Winnie the Pooh and his friends are playing a game called Poohsticks where they drop sticks in a stream and race them. 
#They time how long it takes each player's stick to float under Poohsticks Bridge to score each round.

#Write a function count_less_than() to help Pooh and his friends determine how many players should move on to the next round of Poohsticks. 
# count_less_than() should accept a list of integers race_times and an integer threshold and return the number of race times less than threshold.

def count_less_than(race_times, threshold):
    counter=0

    for i in range(len(race_times)):
        if race_times[i]>=threshold:
            counter=counter+1
    
    print("The number of players who should move on to the next round is: ", counter)



#8: Pooh's To Do's 
#Write a function print_todo_list() that accepts a list of strings named tasks. The function should then number and print each task on a new line using the format:

#Pooh's To Dos:
#Task 1
#Task 2

def print_todo_list(task):
    print("Pooh's To Do's")
    counter=1
    for i in range(len(task)):
        print(f"{counter}. {task[i]}")
        counter+=counter
        

#Problem 9: Pairs
#Rabbit is very particular about his belongigns and wants to own an even number of each thing he owns. 
#Write a function can_pair() that accepts a list of integers item_quantities. Return True if each number in item_quantities is even.
#Return False otherwise.

def can_pair(item_quantities):
    for i in range(len(item_quantities)):
        
        if item_quantities[i]%2!=0:
            print("False")
            return False
        else:
            print("True")
            return True
    print("True")
    return True
    


#Problem 10: Split Haycorns
#Piglet's has collected a big pile of his favorite food, haycorns, and wants to split them evenly amongst his friends. 
# Write a function split_haycorns() to help Piglet determine the number of ways he can split his haycorns into even groups. 
# split_haycorns() accepts a positive integer quantity as a parameter and returns a list of all divisors of quantity.

def split_haycorns(quantity):
    groups=[]
    for i in range(1,quantity+1):
        if quantity%i==0:
            groups.append(i)

    return groups


#Problem 11: T-I-Double Guh-ER
#Signs in the Hundred Acre Wood have been losing letters as Tigger bounces around stealing any letters he needs to spell out his name. 
# Write a function tiggerfy() that accepts a string s, and returns a new string with the letters t, i, g, e, and r removed from it.
def tiggerfy(s):
    skip={'t','i','g','e', 'r', 'T','I','G', 'E', 'R' }
    new_word=""

    for letter in s:
        if letter not in skip:
            new_word+=letter
    return new_word

#Problem 12: Thistle Hunt
#Pooh, Piglet, and Roo are looking for thistles to gift their friend Eeyore. 
# Write a function locate_thistles() that takes in a list of strings items and returns a list of the indices of any elements with value "thistle". 
# The indices in the resulting list should be ordered from least to greatest.

def locate_thistles(items):
    locations=[]
    keyword="thistle"
    #need to pass both the index and value so we can keep track of both
    #index is the location where it's at and the value is what the index contains at that particular location 
    for index, value in enumerate (items):
        #if the value we're currently at matches the keyword we're looking for
        if value in keyword:
            #we add the index to our list
            #this will keep happening everytime we come across the keyword 
            locations.append(index)
    return locations



def main():
    items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
    print(locate_thistles(items))

    items = ["book", "bouncy ball", "leaf", "red balloon"]
    print(locate_thistles(items))



main()












#good job!
#like that?
# yeah you need to have it print it so it shows on the terminal#
# technically yeah if we want to see it yeah like that
## Ohhh so we do print get_item ??
# not super sure but we need to fix this lol 
#is the issue in the calling or in the function?
#like it runs but it doesn't show so I'm assuming the return statements might be the issue
#perfectionnn nice to meet you guyss
#put your linkedin so i can connect with you 
#CHAT IT WORKED 
#www.linkedin.com/in/emmanuel-serrano-campa# - Nice meeting you guys
#www.linkedin.com/in/alissen-moreno-72442b13b

#we are room 4 right ? yah I think so