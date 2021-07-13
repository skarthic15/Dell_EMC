"""
6) Suppose I have "n" chocolates. and "m" children, if i want to distribute each chocolates to all m children in a sequential order by repeating same list of children if excess. how do you distribute? (python)
    example1: if n=3 (chocolates here is 3) , m=3 (children are 3 you can name it as 1,2,3 ) answer: 1:1,2:1,3:=1 
    example 2: if n=5 and m=7 then child 1:2, 2:2, 3:1, 4:1, 5:1
can you write a simple python function to resolve this? where n and m are parameters.
"""
import argparse

def distribute_seq(n, m):
    # Divide chocolates equally (equ) and find the reminder (rem)
    equ = n//m
    rem = n%m

    # Assign Equal(equ) as value to all keys (m)
    result = dict((i, equ) for i in range(1, m+1))

    # Increase the count looping reminder
    for j in range(1, rem+1):
        result[j] += 1
    
    return result

parser = argparse.ArgumentParser()
parser.add_argument('-n', help='Number of chocolates', type=int)
parser.add_argument('-m', help='Number of children', type=int)
args = parser.parse_args()


res = distribute_seq(args.n, args.m)
print(res)