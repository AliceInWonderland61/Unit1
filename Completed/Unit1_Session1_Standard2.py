#Problem1: Write a function batman() that prints the string "I am vengeance. I am the night. I am Batman!".
def batman():
    print("I am vengeance. I am the night. I am Batman!")


#Problem2: Mad Libs
#Write a function madlib() that accepts one parameter, a string verb. 
# The function should print the sentence: "I have one power. I never <verb>. - Batman".
def madlib(verb):
    print(f"I have one power. I never {verb}. -Batman.")


#Problem3: Trilogy
#Write a function trilogy() that accepts an integer year and prints the title of the Batman trilogy movie released that year as outlined below.
        #Year	Movie Title
        #2005	"Batman Begins"
        #2008	"The Dark Knight"
        #2012	"The Dark Knight Rises"
#If the given year does not match one of the years in the table above, 
# print "Christopher Nolan did not release a Batman movie in <year>."
def trilogy(year):
    if year==2005:
        print("Batman Begins") 
    elif year==2008:
        print("The Dark Knight")
    elif year==2012:
        print("The Dark Knight Rises")
    else:
        print(f"Christopher Nolan did not release a Batman movie in {year}.")


#Problem 4: Last
#Implement a function get_last() that accepts a list of items items and returns the last item in the list. 
# If the list is empty, return None.

def get_last(items):
    for i in items:
        #so my thought process was to get to the last index. So I check if the index we're on is the same number as the length of items
        #if we are then we've reached the end so we just print it 
        if items.index(i)==len(items)-1:
            print(i)


#Problem 5: Concatenate
#Write a function concatenate() that takes in a list of strings words and returns a string concatenated that concatenates all elements in words.

def concatenate(words):
    completed_word=""
    for i in words:
        completed_word+=i
    print(completed_word)


#Problem 6: Squared
#Write a function squared() that accepts a list of integers numbers as a parameter and squares each item in the list. 
#Return the squared list.

def squared(numbers):
    #if it's a list you can append
    squared_nums=[]
    for i in numbers:
        squared_nums.append(i*i)
    print(squared_nums)


#Problem 7: NaNaNaBatman
#Write a function nanana_batman() that accepts an integer x and prints the string "nanana batman!" where "na" is repeated x times. Do not use the * operator.

def nanana_batman(x):
    repeated=""
    counter=0
    while counter<x:
        #since we have a string named repeated then we can keep adding 'na' each time the loop executes
        #it will loop x times 
        repeated+="na"
        #increment counter 
        counter+=1
    print(f"{repeated} batman!")


#Problem 8: Find the Villain
#Write a function find_villain() that accepts a list crowd and a value villain as parameters and returns a list of all indices where the villain is found hiding in the crowd.

def find_villain(crowd, villain):
    #create a list to save the indexes 
    found_villains=[]
    #we're looking at the values and the index of the list we received (crowd)
    for index, value in enumerate(crowd):
        #if the current value we are at is equal to the villain then we save the index to our list 
        if value==villain:
            found_villains.append(index)
    print(found_villains)


#Problem 9: Odd
#Write a function get_odds() that takes in a list of integers nums and returns a new list containing all the odd numbers in nums.

def get_odds(nums):
    odds_only=[]

    for i in nums:
        if i%2!=0:
            odds_only.append(i)
    print(odds_only)



#Problem 10: Up and Down
#Write a function up_and_down() that accepts a list of integers lst as a parameter. 
# The function should return the number of odd numbers minus the number of even numbers in the list.

def up_and_down(lst):
    odds_only=0
    evens_only=0

    for i in lst:
        if i%2==0:
            evens_only+=1
        else:
            odds_only+=1
    print(odds_only-evens_only)


#Problem 11: Running Sum
#Write a function running_sum() that accepts a list of integers superhero_stats representing the number of crimes Batman has stopped each month in Gotham City. 
# The function should modify the list to return the running sum such that superhero_stats[i] = sum(superhero_stats[0]...superhero_stats[i]). 
# You must modify the list in place; you may not create any new lists as part of your solution.

def running_sum(superhero_stats):
    


def main():
    lst = [1, 2, 3]
    up_and_down(lst)

    lst = [1, 3, 5]
    up_and_down(lst)

    lst = [2, 4, 10, 2]
    up_and_down(lst)


main()