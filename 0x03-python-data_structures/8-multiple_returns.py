#!/usr/bin/python3.8

def multiple_returns(sentence):
    first_char = ""
    s_len = len(sentence)
    if not sentence:
        first_char = None
    else:
        first_char = sentence[0]

    tuple_ = s_len, first_char
    return tuple_
