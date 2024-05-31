import random

word_bank = ['impaired', 'fax', 'lost', 'needle', 'scribe', 'crunchy', 'state', 'finalize', 'respectful', 'disillusion', 'us-led', 'resistance', 'european', 'decency', 'ranking', 'songwriting', 'grocer', 'shoddy', 'smuggle', 'backstage', 'slink', 'infinity', 'plug', 'abomination', 'limo', 'relation', 'syphilis', 'fell', 'broom', 'celibacy', 'intuition', 'earnest', 'falsify', 'hearty', 'taunt', 'chromosome', 'sneakers', 'placid', 'speaking', 'probability', 'music', 'challenger', 'regret', 'insightful', 'might', 'tuber', 'arbor', 'cinch', 'nylon', 'fat-free']
word = word_bank[random.randrange(len(word_bank))]
repeats = []
print("_ " * len(word))

def guess(s):
    if not(s >= 'a' and s <= 'z'):
        print('ERROR')
    elif s in repeats:
        print('REPEAT')
    elif s in word:
        print(s)
    else:
        print('not in word')
    repeats += s