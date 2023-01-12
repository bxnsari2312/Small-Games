##Bansari Shah
##ICS3U0
##Waterloo J3; 2001
##5 Nov 2020

cards = input()
C = []
D = []
H = []
S = []
points = []

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

point_C = (C.count("A")*4)+(C.count("K")*3)+(C.count("Q")*2)+(C.count("J")*1)
point_D = (D.count("A")*4)+(D.count("K")*3)+(D.count("Q")*2)+(D.count("J")*1)
point_H = (H.count("A")*4)+(H.count("K")*3)+(H.count("Q")*2)+(H.count("J")*1)
point_S = (S.count("A")*4)+(S.count("K")*3)+(S.count("Q")*2)+(S.count("J")*1)

if len(C) == 0:
    point_C += 3
elif len(C) == 1:
    point_C += 2
elif len(C) == 2:
    point_C += 1

if len(D) == 0:
    point_D += 3
elif len(D) == 1:
    point_D += 2
elif len(D) == 2:
    point_D += 1

if len(H) == 0:
    point_H += 3
elif len(H) == 1:
    point_H += 2
elif len(H) == 2:
    point_H += 1

if len(S) == 0:
    point_S += 3
elif len(S) == 1:
    point_S += 2
elif len(S) == 2:
    point_S += 1
    
total = (point_C+point_D+point_H+point_S)

new_C = " ".join(C)
new_D = " ".join(D)
new_H = " ".join(H)
new_S = " ".join(S)

space = 5

print("{0:s} {1:>20s}".format("Cards Dealth", "Points"))
print("Clubs", new_C, "{:>20d}".format(point_C))
print("Diamonds", new_D, "{space:>20d}".format(point_D))
print("Hearts", new_H, "{:>20d}".format(point_H))
print("Spades", new_S, "{:>20d}".format(point_S))
print("{0:>32s} {1:>d}".format("Total", total))

        
                    
        
