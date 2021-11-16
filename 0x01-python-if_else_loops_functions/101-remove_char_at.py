#!/usr/bin/python3
def remove_char_at(str, n):
    first_part = str[:n]
    last_part = str[n+1:]
    total_part = first_part + last_part
    if n > 0:
        return total_part
    else:
        return str[0:]
