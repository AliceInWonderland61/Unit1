#hello
#Problem 1: Reverse Sentence
#Write a function reverse_sentence() that takes in a string 
# Sentence and returns the sentence with the order of the words reversed. 
# The sentence will contain only alphabetic characters and spaces to separate the words. 
# If there is only one word in the sentence, the function should return the original string.


def reverse_sentence(sentence):
    #we need to split the sentence and save it in variable word
    words = sentence.split() 
    
   
    result=[] # create empty list 

    #gets the last word in the list and appends it to variable result until you reach the first word
    for i in words[::-1]:
        result.append(i) 
        
    #join the reversed splitted strings
    reversed_str=" ".join(result)

    # print the final reversed string
    print(reversed_str)

# the sentence we want to reverse
sentence = "tubby little cubby all stuffed with fluff"
reverse_sentence(sentence)


 # https://pythontutor.com/ 
 # https://pythontutor.com/render.html#mode=display
    