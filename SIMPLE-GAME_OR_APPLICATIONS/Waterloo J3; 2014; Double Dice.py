#Bansari Shah
#ICS3U0
#Waterloo J3; 2014
#28 Oct 2020

rounds = int(input())
David = 100
Anatonia = 100
for count in range(rounds):
    ana, dav = input().split()
    ana = int(ana)
    dav = int(dav)
    if dav > ana:
        Anatonia -= dav
    elif ana > dav:
        David -= ana
print(Anatonia)
print(David)
        
        
    
    
