import re

input = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
""".splitlines()


def part1(input):
    tot = 0
    for card in input:
        first = True
        val = 0
        card = (card.split(": "))[1]
        win_numbers = (card.split("|"))[0].split()
        my_numbers = (card.split("|"))[1].split()

        for win in win_numbers:
            found = False
            for mine in my_numbers:
                if not found:
                    if win == mine:
                        found = True
                        if first:
                            val = 1
                            first = False
                        else:
                            val = val * 2
            
        tot += val

    return tot

def part2(input):

    n_lines = len(input)
    n_cards = []
    for i in range(n_lines):
        n_cards.append(1)

    for i,card in enumerate(input):
        card = (card.split(": "))[1]
        win_numbers = (card.split("|"))[0].split()
        my_numbers = (card.split("|"))[1].split()
        val = 0
        for j in range(n_cards[i]):

            for win in win_numbers:
                for mine in my_numbers:
                    if win == mine:
                        val += 1

            for x in range(val):
                if i+x+1 < n_lines:
                    n_cards[i+x+1] += 1

    print(n_cards)
    return sum(n_cards)


#print(part1(input))
print(part2(input))