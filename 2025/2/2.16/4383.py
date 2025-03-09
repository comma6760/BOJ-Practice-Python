from typing import *
import sys

input = sys.stdin.readline

def sol(n, arr) -> str:
    check_arr = [i for i in range(1, n)]
    result_arr = []
    
    for i in range(len(arr)-1):
        result : int = abs(arr[i] - arr[i+1])
        
        if result not in result_arr:
            result_arr.append(result)
    
    if sorted(result_arr) == check_arr:
        return 'Jolly'
    else:
        return 'Not jolly'
    
while 1:
    try:
        arr = list(map(int, input().split()))
        print(sol(arr[0], arr[1:]))
    except:
        break