inp = input("Enter a text : ")

s = 1

a = ["Hey how are you doing young man !?"]
print(a[0],"is to match with")

def find_best_match (inp , available , sens=1) :
    #inp -->  user input
    #sens --> the accuracy of the answer
    #available --> the database


    sens = len(inp) // sens # atleast this much match count

    inv_inp = inp.lower().split()  #optimized input string

    ign_words = ["is","the","an","a"]

    index = -1
    word_match = 0
    overall_match = { }  # "question" : average of word match and word count
    for question in available :

        index += 1 # index of the taken question in the database

        q = question.lower().split() # list of all individual words in the selected question(optimized question string)

        for word in inv_inp :

            if word.lower() in ign_words :
                pass
            
            elif word in q :
                word_match += 1

        word_match = int(( word_match/len(inv_inp)) * 100 ) # percentage of words matched
        print(word_match,"% match")

        #ind = 0 # for checkiung the order of the words
        #try : 
        #    if inv_inp[in1] == q[in2] :

        

find_best_match(inp,a,s)