#!/usr/bin/python3
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(P, Q):
    # Implement your solution here
    string = P + Q
    frequency = {}
    for c in string:
        frequency[c] = frequency.get(c, 0) +1
    return len([c for c in frequency if frequency[c] > 1])

solution("ca", "ab")
