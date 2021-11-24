#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_marks = 0
    best_marks = ''
    for key, val in a_dictionary.items():
        if val > max_marks:
            max_marks = val
            best_marks = key
    return best_marks
