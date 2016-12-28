import random

cycles = 2016
contestants = ['mitch', 'dave', 'michael', 'james b', 'james g', 'robyn', 'cole', 'richard', 'tom', 'lonnie']

def choose_winner(contestants, cycles):
    random.seed()
    counts = dict(zip(contestants,[0]*len(contestants)))
    for i in range(cycles):
        person = random.choice(contestants)
        counts[person] += 1
    stacked_list = sorted(counts, key=lambda i: counts[i], reverse=True)
    winner = stacked_list.pop(0)
    print "Winner: {}".format(winner)
    print "Count: {}".format(counts[winner])
    print "Honorable mentions:"
    for entry in stacked_list:
        print "{:4d}: {}".format(counts[entry], entry)
        
if __name__ == "__main__":
  choose_winner(contestants, cycles)
