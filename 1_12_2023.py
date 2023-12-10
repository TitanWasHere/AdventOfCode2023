from subprocess import Popen, PIPE
from time import sleep 
from collections import defaultdict as dd 
from collections import deque as de 
from collections import Counter as cn 
from string import ascii_uppercase as au 
from string import ascii_lowercase as al 
from copy import deepcopy as dp 
from itertools import * 
from math import prod 
from math import factorial 
from sys import exit 
from sys import setrecursionlimit as srl 
from statistics import mode 
from statistics import median 
from heapq import * 
from re import * 




def part1(input):
    tot = 0
    for word in input:
        firstVal = 0
        lastVal = 0
        for i in word:
            if i >= '0' and i <= '9':
                firstVal = ord(i)
                break
        
        for i in word[: :-1]:
            if i >= '0' and i <= '9':
                lastVal = ord(i)
                break
        
        print(firstVal-48, lastVal-48)
        firstVal = ((firstVal-48) * 10)+(lastVal-48)

        tot = tot + firstVal
    
    return tot


def part2(input):
    tot = 0    
    numbers = ["one" , "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for word in input:
        firstVal = 0
        lastVal = 0
        for i in range(len(word)):
            if word[i] >= '0' and word[i] <= '9':
                firstVal = ord(word[i])-48
                break
            else:
                ok = False
                for k in range(len(numbers)):
                    if word[i:i+3] == numbers[k]:
                        firstVal = k+1
                        ok = True
                        break
                    elif word[i:i+4] == numbers[k]:
                        firstVal = k+1
                        ok = True
                        break
                    elif word[i:i+5] == numbers[k]:
                        firstVal = k+1
                        ok = True
                        break
                
                if ok == True:
                    break
        
        i = len(word)-1
        while i>=0:
            if word[i] >= '0' and word[i] <= '9':
                firstVal = ord(word[i])-48
                break
            else:
                ok = False
                for k in range(len(numbers)):
                    print(word[i-3 : i])
                    if word[i-2:i+1] == numbers[k]:
                        firstVal = k+1
                        ok = True
                        break
                    elif word[i-4:i] == numbers[k]:
                        firstVal = k+1
                        ok = True
                        break
                    elif word[i-5:i] == numbers[k]:
                        firstVal = k+1
                        ok = True
                        break
                
                if ok == True:
                    break
            i = i-1

            print(firstVal, lastVal)
        
        tot = tot + ((firstVal*10) + lastVal) 
            

    return tot
input = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
""".splitlines()



#print(part1(input))

print(part2(input))

