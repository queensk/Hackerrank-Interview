# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # Implement your solution here
    binary = format(N, "b")
    gaps = binary.strip("0").split("1")
    longest_gap = max([len(gap)for gap in gaps])
    return longest_gap
