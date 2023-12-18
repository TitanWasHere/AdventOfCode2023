import re

input = """Time:        42     89     91     89
Distance:   308   1170   1291   1467
"""

def part1(input):
    tot = 1
    times, distances = input.splitlines()
    times = list(map(int, re.findall('\d+', times)))
    distances = list(map(int, re.findall('\d+', distances)))
    for time, distance in zip(times, distances):
        wins = 0
        speed = 0
        for acceleration in range(1, time):
            speed += 1
            travelled = (time-acceleration) * speed
            if (travelled > distance):
                wins += travelled > distance
            elif wins:
                break
            
        tot *= wins

    return tot

print(part1(input))