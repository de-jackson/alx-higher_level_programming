#!/usr/bin/python3
def remove_char_at(str, n):
    first_part = str[:n]
    last_part = str[n+1:]
    total_part = first_part + last_part
    return total_part
