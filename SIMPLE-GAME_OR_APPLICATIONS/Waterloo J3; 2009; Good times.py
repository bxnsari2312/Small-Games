#Bansari Shah
#ICS3U0
#Waterloo J3; 2009
#29 Oct 2020

##ottawa_time = int(input())
##if ottawa_time > 2400:
##    ottawa_time -= 2400
##elif ottawa_time < 0:
##    ottawa_time += 2400
##
##if ottawa_time % 100 >= 60:
##    ottawa_time = ((ottawa_time % 100)-60)+(((ottawa_time//100)*100)+100)
##print(ottawa_time, "in Ottawa")
##
#######Victria Time
##victoria_time = ottawa_time - 300
##if victoria_time > 2400:
##    victoria_time -= 2400
##elif victoria_time < 0:
##    victoria_time += 2400
##
##if victoria_time % 100 >= 60:
##    victoria_time = ((victoria_time % 100)-60)+(((victoria_time//100)*100)+100)
##print(victoria_time, "in Victoria")
##
#######Edmoton
##edmoton_time = ottawa_time - 200
##if edmoton_time > 2400:
##    edmoton_time -= 2400
##elif edmoton_time < 0:
##    edmoton_time += 2400
##
##if edmoton_time % 100 >= 60:
##    edmoton_time = ((edmoton_time % 100)-60)+(((edmoton_time//100)*100)+100)
##print(edmoton_time - 200, "in Edmoton")
########Winnipeg
##
##print(ottawa_time - 100, "in Winnipeg")
##print(ottawa_time, "in Toronto")
##print(ottawa_time + 100, "in Halifax")
##print(ottawa_time + 130, "in St. John's")


############################################################################################################################################

time = int(input())

def region_time(time, additional):
    new_time = time + additional
    
    if new_time > 2400:
        new_time -= 2400
    
    elif new_time < 0:
        new_time += 2400

    if new_time % 100 >= 60:
        new_time = ((new_time % 100)-60)+(((new_time//100)*100)+100)

    return (new_time)

print(region_time(time, 0), "in Ottawa")
print(region_time(time, -300), "in Victoria")
print(region_time(time, -200), "in Edmonton")
print(region_time(time, -100), "in Winnipeg")
print(region_time(time, 0), "in Toronto")
print(region_time(time, 100), "in Halifax")
print(region_time(time, 130), "in St. John's")

    









