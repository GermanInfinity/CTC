# "Given an input string, reverse the string word by word." 

# how to reverse string ? 

def reverse_word(sentence):
    words = sentence.split(' ')
    reverse_sentence = ' '.join(reversed(words))
    return (reverse_sentence)

if __name__=="__main__": 
    print ("Testing")
    value = reverse_word("Harry      Potter")
    print (value)
    #assert value=="yrraH rettoP"