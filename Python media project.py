#this program is a review
#Program must take 6 inputs
###
media_list= ["book", "movie", "music", "videogame",]
media = input( " What type of media do you use " )
# Genre of Media types
book_genre= []
if media == media_list[0]:
    book_genre= ["horror", "mystery","fantasy","fiction","nonfiction","history"] 
print (book_genre) 
movie_genre= []
if media == media_list[1]:
    movie_genre= ["horror","action","adventure","comedy"]
print (movie_genre) 
music_genre= []
if media == media_list[2]:
    music_genre= ["pop","rap","rock","country", "hip_hop"]
print (music_genre)
videogame_genre= []
if media == media_list[3]:
    videogame_genre= ["shooting","fighting","rpg","moba","horror"]
print (videogame_genre)
# Title
print('    ')
title = input(" What is the Titles that you enjoy on/in " + media + ':')
print('    ')

print ('What is ' + title + ' about?: ')
Description = input()
print('    ')   

print ('*tip-If you dont know the date then, plesase enter (N/A)')
year = input('What year was it created: ')
print('    ')   

rating = float(input('How would you rate ' + str(title) + ' in a scale of 1-10: '))
print (rating)o

Review_list = [media,title,Description,year,media_list,rating]
review_list_str = ["media", "title", "Description", "year", "genre", "rating"]

print('    ')     
print ('   //////Review//////   ')

i = 0
for value in Review_list:
    print(review_list_str[i] + " " + str(value))
    i += 1
    
    

# print ('media---' + Review_list[0])
# print ('title---' + Review_list[1])
# print ('Description---' + Review_list[2])
# print ('year Created---' + Review_list[3])
# print ('genre---' + Review_list[])
# print ('rating---' + str(Review_list[] ))

print ('   //////Review//////   ')
