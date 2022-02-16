# write a program to calculate the area of a circle
# A = π r 2

print('''
WELCOME TO MY SOFTWARE
this software is capable of calculating calculate the area of a circle
Feel free to use it.
''')
pi = 22/7

radius = input('please specify the radius of the circle ')
print(f'you entered {radius} as the radius of your circle')

area = pi * float(radius)**2

print(f'Based on this the area of your circle is {int(area)}')

# if, elif, else

normal_area = 1000
average_area = 1500
abnormal_area = 2000

if area <= normal_area:
    print(f'You circle is a normal circle because the are fall within the standard limit of {normal_area}')
elif area > normal_area or area <= average_area:
    print('the are of your circle is average')
else:
    print('area is abnormal')



