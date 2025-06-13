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











def main():
    words = ["vengeance", "darkness", "batman"]
    concatenate(words)

    words = []
    concatenate(words)


main()