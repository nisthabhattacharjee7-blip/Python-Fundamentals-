def palidrome_checker (word):

    word = word.lower()     #convert into lower case for case sensitivity 

    #reverse the word to check palidrome or not 
    reversed_word = word[::-1]

    if word == reversed_word:
       return "Palidrome"
    else:
       return "Not a palidrome"


p = input("Enter a word : ")
print(palidrome_checker(p))
