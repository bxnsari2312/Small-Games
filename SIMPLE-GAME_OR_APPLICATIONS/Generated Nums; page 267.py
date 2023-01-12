#Bansari Shah
#ICS3U0
#Generated Nums; page 267
#27 Oct 2020

print("{0:<10s} {1:s}".format("Index", "Generated Number"))


for counter in range(101):
    index = counter
    total = counter
    pos = 0
    counter = str(counter)
    while pos < len(counter):
        number = int(counter[pos])
        total += number
        pos += 1
    print("{0:<10d} {1:d}".format(index, total))
    
        
        
    
    
