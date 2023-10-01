#!/usr/bin/env python3


def get_input():
    return input().lower()


def validate():
    pass


def output(valid, invalid):
    print(" ".join(valid))
    print(" ".join(invalid))


user_input = input().lower()
last_input = user_input

valid_words = []
invalid_words = []

while (current := get_input()) != "x":
    if last_input[-1] == current[0]:
        valid_words.append(user_input)
        last_input = user_input
    else:
        invalid_words.append(user_input)

output(valid_words, invalid_words)
