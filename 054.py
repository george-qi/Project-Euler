"""
Project Euler Problem 54
========================

In the card game poker, a hand consists of five cards and are ranked, from
lowest to highest, in the following way:

  * High Card: Highest value card.
  * One Pair: Two cards of the same value.
  * Two Pairs: Two different pairs.
  * Three of a Kind: Three cards of the same value.
  * Straight: All cards are consecutive values.
  * Flush: All cards of the same suit.
  * Full House: Three of a kind and a pair.
  * Four of a Kind: Four cards of the same value.
  * Straight Flush: All cards are consecutive values of same suit.
  * Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the
highest value wins; for example, a pair of eights beats a pair of fives
(see example 1 below). But if two ranks tie, for example, both players
have a pair of queens, then highest cards in each hand are compared (see
example 4 below); if the highest cards tie then the next highest cards are
compared, and so on.

Consider the following five hands dealt to two players:

        Hand   Player 1            Player 2              Winner
        1      5H 5C 6S 7S KD      2C 3S 8S 8D TD        Player 2
               Pair of Fives       Pair of Eights
        2      5D 8C 9S JS AC      2C 5C 7D 8S QH        Player 1
               Highest card Ace    Highest card Queen
        3      2D 9C AS AH AC      3D 6D 7D TD QD        Player 2
               Three Aces          Flush with Diamonds
               4D 6S 9H QH QC      3D 6D 7H QD QS
        4      Pair of Queens      Pair of Queens        Player 1
               Highest card Nine   Highest card Seven
               2H 2D 4C 4D 4S      3C 3D 3S 9S 9D
        5      Full House          Full House            Player 1
               With Three Fours    with Three Threes

The file poker.txt contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space): the
first five are Player 1's cards and the last five are Player 2's cards. You
can assume that all hands are valid (no invalid characters or repeated
cards), each player's hand is in no specific order, and in each hand there
is a clear winner.

How many hands does Player 1 win?
"""

tier = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
def convert_hand(p):
    return [int(tier.index(ele)) for ele in p]
def is_straight(p):
    for idx in xrange(4,0,-1):
        if p[idx] - p[idx-1] != 1: return False
    return True

def hand_tier(p):
    vals = [i[0] for i in p]
    int_vals = sorted(convert_hand(vals))
    suits = [i[1] for i in p]
    # flush variant
    if len(set(suits)) == 1:
        if int_vals == xrange(10, 15): return (10, int_vals[-1])
        if is_straight(int_vals): return (9, int_vals[-1])
        return (6, int_vals)
    # regular straight
    if is_straight(int_vals): return (5, int_vals[-1])
    # 4 of a kind
    int_set = set(int_vals)
    if len(int_set) == 2:
        single, quad = 0,0
        for ele in int_vals:
            if int_vals.count(ele) == 1: single = ele
            else: quad = ele
        return (8, [single,quad])
    pairs, triples, neither = [], [], []
    for d in int_set:
        reps = int_vals.count(d)
        if reps == 2: pairs.append(d)
        elif reps == 3: triples.append(d)
        else: neither.append(d)
    # if there exist triples
    if len(triples):
        if len(pairs): return (7, pairs + triples)
        return (4, sorted(neither) + triples)
    else:
        if len(pairs) == 0: return (1, int_vals)
        if len(pairs) == 1: return (2, sorted(neither) + pairs)
        if len(pairs) == 2: return (3, sorted(neither) + sorted(pairs))

def p1_win(p1, p2):
    h1, h2 = hand_tier(p1), hand_tier(p2)
    if h1[0] > h2[0]: return True
    if h1[0] < h2[0]: return False
    # same tier
    for i in xrange(len(h1[1])-1, -1, -1):
        if h1[1][i] != h2[1][i]:
            # print h1[1][i] > h2[1][i]
            return h1[1][i] > h2[1][i]

file = open("resources/poker.txt", 'rU')
wins = 0
for line in file:
    l = line.split(' ')
    p1, p2 = l[:5], l[-5:]
    if p1_win(p1, p2): wins += 1
print wins



