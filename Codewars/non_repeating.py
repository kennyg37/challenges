#!/usr/bin/env python3
def first_non_repeating_letter(string):
    lower_string = string.lower()
    for index, char in enumerate(lower_string):
        if lower_string.count(char) == 1:
            return string[index]
    return ''
