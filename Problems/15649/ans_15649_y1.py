#https://www.acmicpc.net/problem/15649
import sys

# 풀이 1.
def Search():
    if len(Arry) == M:
        print(' '.join(map(str, Arry)))
        return
    
    for i in range(1, N+1):
        if i in Arry:
            continue
        Arry.append(i)
        Search()
        Arry.pop()

def solve():
    global N,M
    global Arry
    N, M = map(int, sys.stdin.readline().split())
    Arry = []
    Search()    

if __name__ == "__main__":
    solve()

# 풀이 2. 진행중
# def search(Arry):
#     if len(Arry) == M:
#         print(Arry)
#         return 
#     else:
#         for i in range(1,N+1):
#             if i not in Arry:
#                 Arry.append(i)
#                 search(Arry)
    

# def solve():
#     N,M = map(int,sys.stdin.readline().split())
#     Arry=[]
#     Switch = [True]*len(M)
    
    
# if __name__ == "__main__":
#     solve()