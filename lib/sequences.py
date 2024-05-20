#!/usr/bin/env python3

def print_fibonacci(length):
    # initialize an empty list
    fibonacci_sequence = []
    if length > 0:
        fibonacci_sequence.append(0)
    if length > 1:
        fibonacci_sequence.append(1)
    while len(fibonacci_sequence) < length:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])

    print(fibonacci_sequence)        

