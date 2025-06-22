#Problem 1: Given two lists of strings artists and set_times of length n, write a function lineup() that maps each artist to their set time.

#An artist artists[i] has set time set_times[i]. 
# Assume i <= 0 < n and len(artists) == len(set_times).

def lineup(artists, set_times):
    dictionary={}
    for i in range(len(artists)):
       dictionary[artists[i]] = set_times[i]
    return dictionary




#Problem 2: You are designing an app for your festival to help attendees have the best experience possible! 
# As part of the application, users will be able to easily search their favorite artist and find out the day, time, and stage the artist is playing at. 
# Write a function get_artist_info() that accepts a string artist and a dictionary festival_schedule mapping artist's names to dictionaries containing the day, time, and stage they are playing on. 
# Return the dictionary containing the information about the given artist.
#If the artist searched for does not exist in festival_schedule, return the dictionary {"message": "Artist not found"}
def get_artist_info(artist, festival_schedule):
    
    if artist in festival_schedule:
        return festival_schedule[artist]
    else:
        return {'message': 'Artist not found'}


        
#Problem3: Ticket Sales
#A dictionary ticket_sales is used to map ticket type to number of tickets sold. 
# Return the total number of tickets of all types sold.

def total_sales(ticket_sales):
    result = 0
    #to get the values from the dictionary 
    for values in ticket_sales.values():
        result+=values
    return result

#Problem 4
#Demand for your festival has exceeded expectations, so you're expanding the festival to span two different venues. 
# Some artists will perform both venues, while others will perform at just one. 
# To ensure that there are no scheduling conflicts, i
# implement a function identify_conflicts() that accepts two dictionaries venue1_schedule 
# and venue2_schedule each mapping the artists playing at the venue to their set times. 
# Return a dictionary containing the key-value pairs that are the same in each schedule.
def identify_conflicts(venue1_schedule, venue2_schedule):
    conflict={} #empty dictionary where we'll save the conflicted ones 
    for key in venue1_schedule.keys():
        if key in venue2_schedule.keys() and venue1_schedule[key]==venue2_schedule[key]:
            conflict[key]=venue1_schedule[key]
    return conflict


#Problem 5: As part of the festival, attendees cast votes for their favorite set. 
# Given a dictionary votes that maps attendees id numbers to the artist they voted for, return the artist that had the most number of votes. 
# If there is a tie, return any artist with the top number of votes.


def best_set(votes):
    most_votes={}
    for i in votes.values():
        if i not in most_votes:
            most_votes[i]=1
        else:
            most_votes[i]+=1
    #get the max value but output the key
    #get the max value by passing the dictionary most_votes and specify that we're getting the key as the output 
    max_value=max(most_votes, key=most_votes.get)
    return max_value
    
   
#Problem 6: You are given an array audiences consisting of positive integers representing the audience size for different performances at a music festival.
#Return the combined audience size of all performances in audiences with the maximum audience size.
#The audience size of a performance is the number of people who attended that performance.
def max_audience_performances(audiences):
    
    biggest=0
    total_size=0
    #this was kinda confusing but essentially we need to find the biggest attendance and if there's more audiences with that attendance then we add them up
    for i in range(len(audiences)):
        if audiences[i]>biggest:
            biggest=audiences[i]
    #after finding the largest number of atendees we double check to see if we had other audiences with that same number; 
    #If we do then we add them to the total_size and return it 
    for i in range(len(audiences)):
        if audiences[i]==biggest:
            total_size+=biggest

    return total_size

#Problem7: Performances with Maximum Audience II
#f you used a dictionary as part of your solution to max_audience_performances() in the previous problem, try reimplementing the function without using a dictionary. 
#If you implemented max_audience_performances() without using a dictionary, try solving the problem with a dictionary.
#Once you've come up with your second solution, compare the two. Is one solution better than the other? Why or why not?

#So I didn't use a dictionary; my idea is that I can create a dictionary with the key as the number and the value the # of times we see that number 
#then at the end we get the biggest number and multiply the key and the value and return that
def max_audience_performance(audiences):
    dictionary={}

    for i in audiences:
        if i not in dictionary:
            dictionary[i]=1
        else:
            dictionary+=1
    #get the biggest key we have 
    biggest=max(dictionary.keys())
    #multiply biggest * the value we got from the dictionary 
    return biggest*dictionary[biggest]


#Problem 8: Popular Song Pairs
#Given an array of integers popularity_scores representing the popularity scores of songs in a music festival playlist, return the number of popular song pairs.
#A pair (i, j) is called popular if the songs have the same popularity score and i < j.
#Hint: number of pairs = (n x n-1)/2

def num_popular_pairs(popularity_scores):
    #let's create a dictionary that will count how many times each popularity score is repeated or how many times it appears
    freq={}

    #now we go through each score in popularity_scores to register them to our dictionary 
    for score in popularity_scores:
        if score in freq:
            #if the score is already inside the freq dictionary then we increase their value 
            freq[score]+=1
        else:
            #if we still don't have it in our dictionary then we initialize it and add it 
            freq[score]=1
    
    #after we add all those to our dictionary then we go thorugh the dictionary to see which pairs we can make

    #variable to hold the number of pairs we have 
    total_pairs=0

    for i in freq.values():
        if i>1:
            #if the score is more than 1 then we calculate the pairs that can be made 
            #use the formula they gave us 
            num_pairs=i*(i-1)//2
            total_pairs+=num_pairs
    return total_pairs



#Problem 9: Stage Arrangement Difference Between Two Performances
#You are given two strings s and t representing the stage arrangements of performers in two different performances at a music festival, 
#such that every performer occurs at most once in s and t, and t is a permutation of s.
#The stage arrangement difference between s and t is defined as the sum of the absolute difference between the index of the occurrence of each performer in s 
#and the index of the occurrence of the same performer in t.
#Return the stage arrangement difference between s and t.
#A permutation is a rearrangement of a sequence. 
# For example, [3, 1, 2] and [2, 1 , 3] are both permutations of the list [1, 2, 3].
#Hint: Absolute value function

def find_stage_arrangement_difference(s, t):
    