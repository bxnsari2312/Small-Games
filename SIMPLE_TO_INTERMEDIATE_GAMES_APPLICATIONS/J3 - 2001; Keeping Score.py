##Bansari Shah
##ICS4U-C
##J3 - 2001; - Keeping Score
##02/20/2022

cards = input()
C = []
D = []
H = []
S = []
point_C = 0
point_D = 0
point_H = 0
point_S = 0

for index in range (len(cards)):
    if (index <(len(cards)-1)):
        if cards[index] == "C":
            for c in range(index+1,len(cards)):
                if (cards[c] == "D") or (cards[c] == "H") or (cards[c] == "S"):
                    break
                else:
                    C.append(cards[c])
        elif cards[index] == "D":
            for d in range(index+1,len(cards)):
                if (cards[d] == "C") or (cards[d] == "H") or (cards[d] == "S"):
                    break
                else:
                    D.append(cards[d])
        elif cards[index] == "H":
            for h in range(index+1,len(cards)):
                if (cards[h] == "C") or (cards[h] == "D") or (cards[h] == "S"):
                    break
                else:
                    H.append(cards[h])
        elif cards[index] == "S":
            for s in range(index+1,len(cards)):
                if (cards[s] == "C") or (cards[s] == "D") or (cards[s] == "H"):
                    break
                else:
                    S.append(cards[s])
                    
def card_points(lists_points, hand):
    lists_points = (hand.count("A")*4)+(hand.count("K")*3)+(hand.count("Q")*2)+(hand.count("J")*1)

    if len(hand) == 0:
        lists_points += 3
    elif len(hand) == 1:
        lists_points += 2
    elif len(hand) == 2:
        lists_points += 1

    return(lists_points)

total = (card_points(point_C, C) + card_points(point_D, D) + card_points(point_H, H) + card_points(point_S, S))
print(total)
        



    
