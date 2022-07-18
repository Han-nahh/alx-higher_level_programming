#!/usr/bin/python3
def multiple_returns(sentence):
    length=len(sentence);
    first=None
    if(length>0):
        first=sentence[0]
    return length,first


sentence = "At school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))
