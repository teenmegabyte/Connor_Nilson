# Connor Nilson
# 3/23/18
#1st Period

MG = int(input( "What is your math grade" ))
SG = int(input( "What is your science grade" ))
CSG = int(input( "What is your Computer Science grade" ))
EG = int(input( "What is your English grade" ))
SSG = int(input( "What is your Social Studies grade" ))
divided_by = int(input( "How many grades do you have" ))

grade_list = [ MG, SG, CSG, EG, SSG, ]
average = (MG + SG + CSG + EG + SSG) / divided_by
grade_list.append(str(average))
if average < 60:
    print ("Unsatisfactory")
elif average < 60 or average < 70:
    print (" Needs improvement ")
elif average < 70 or average < 80:
    print(" Doing alright ")
elif average < 80 or average < 90:
    print( " Doing good ")
elif average >= 91:
    print ("Doing Great!")

print (grade_list)
print (average)
while 1==1:
 input( "What is your math grade" )
 input( "What is your science grade" )
 input( "What is yuor Computer Science grade" )
 input( "What is your English grade" )
 input( "What is your Social Studies grade" )
 input( "How many grades do you have" )
