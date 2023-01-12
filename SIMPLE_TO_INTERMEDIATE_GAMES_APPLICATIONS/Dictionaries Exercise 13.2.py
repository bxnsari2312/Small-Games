##Bansari Shah
##ICS4U-C
##Dictionaries Exercise 13.2
##05/11/2022


##create function for the avg rating
def avg_ratings(dic,keys):
    lst = (dic.get(keys))
    lst = [int(i) for i in lst]
    avg = sum(lst)//len(lst)
    return avg

##get the movies as input and split at str
##create a list for the ratings
##create a dictionary for the movies and rating
movies = input().split(",")
ratings = []
movie_d = {"movie":"ratings"}

##for each movie, create a list of input ratings split at space
for i in range(len(movies)):
    movie_d[movies[i]] = input().split()
print(movie_d)

##use the avg function to get the avg rating of all keys in dictionary 
for i in range (len(movies)):
    a_rarting = avg_ratings(movie_d, movies[i])
    print(movies[i], a_rarting)






