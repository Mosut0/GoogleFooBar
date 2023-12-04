import sys

def solution(s):
    substring = ""
    for i in s:
        substring += i
        slices = s.count(substring)
        if slices * len(substring) == len(s):
            return slices
        
print(solution(sys.argv[1]))