#Given two lists of strings artists and set_times of length n, write a function lineup() that maps each artist to their set time.

#An artist artists[i] has set time set_times[i]. 
# Assume i <= 0 < n and len(artists) == len(set_times).

def lineup(artists, set_times):
    dictionary={}
    for i in range(len(artists)):
       dictionary[artists[i]] = set_times[i]
    return dictionary




#You are designing an app for your festival to help attendees have the best experience possible! 
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

'''
just my idea :)

def best_set(votes):
    if not votes:
        return 
    
    counter = {}
    for artist in votes.values():
        if artist in counter.keys():
            counter[artist] += 1
        else:
            counter[artist] = 1
    
    max_votes = max(counter.values())
    for artist in counter.keys():
        if counter[artist] >= max_votes:
            return artist
'''


def best_set(votes):
    most_votes=sorted(votes.keys())

    print(most_votes)


    

    

def main():
    
    
    votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

    votes2 = {
        1234: "SZA", 
        1235: "Yo-Yo Ma",
        1236: "Ethel Cain",
        1237: "Ethel Cain",
        1238: "SZA"
    }

    print(best_set(votes1))
    print(best_set(votes2))
    

    


main()