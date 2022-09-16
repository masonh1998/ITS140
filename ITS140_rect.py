
width_1 = int(input('Enter Width of rectangle 1: '))
height_1 = int(input('Enter Height of rectangle 1: '))

area_1 = (width_1 * height_1)

print ("Rectangle 1 area=", area_1)

width_2 = int(input('Enter Width of rectangle 2: '))
height_2 = int(input('Enter Width of rectangle 2: '))

area_2 = (width_2 * height_2)

print ("Rectangle 2 area=", area_2)

if area_1 >= area_2 :
    print ("Rectangle 1 is greater then rectangle 2")
    
elif area_1 <= area_2 :
    print ("Rectangle 2 is greater then rectangle 1")
    
else: 
    print ("Rectangle 1 is equal to rectangle 2")

