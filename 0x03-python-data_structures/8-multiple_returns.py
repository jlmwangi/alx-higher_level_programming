#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None or len(sentence) == 0:
        return (None)
    else:
        first_char = sentence[0]
        return (len(sentence), first_char)
