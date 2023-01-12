##Bansari Shah
##ICS4U-C
##2016 S1: Ragaman
##05/01/2022

games = int(input())
swifts = input().split()
sema = input().split()
result = 0
swifts_score = 0
sema_score = 0

for day in range(games):
    sema_score += int(swifts[day])
    swifts_score += int(sema[day])

    if sema_score == swifts_score:
        result = day + 1
print(result)
    



