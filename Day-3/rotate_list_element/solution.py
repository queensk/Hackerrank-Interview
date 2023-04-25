# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # Implement your solution here
    A_len =len(A)
    rotated_A = A[A_len-K:] + A[:A_len-K]   
    return rotated_A
