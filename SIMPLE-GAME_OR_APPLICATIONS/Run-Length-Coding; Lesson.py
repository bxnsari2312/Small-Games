#Bansari Shah
#ICS3U0
#Waterloo J3; 2019--- NOT MY ANSWER
#22 Oct 2020


##Compress the original string by building a new string
##Each char and how many times it repeats in given run
##Returns the compreess Text 
def compress(line):              
    results = ""
    current_run_char = ""
    run_length = 0
        
##if this is the first character, start our run
    for i in range(len(line)):
        if i == 0:
            current_run_char = line[i]
            run_length = 1
                
##If we are not on out first character; check if we continue run 
        else:
            current_char = line[i]
                
##Added a new variable to check if current is the same as run char
            if current_char == current_run_char:
                run_length += 1
                    
##Otherwise add to our current run char
            else:
                results += current_run_char + str(run_length)
##reset run
                current_run_char = current_char
                run_length = 1
        return results
print(compress("1223334444"))

                        
                    
                
                
        
    
    
