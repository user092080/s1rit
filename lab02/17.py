color_list1=input("Enter colors in color_list1(comma separated):").split(',')
color_list2=input("Enter colors in color_list2(comma separated):").split(',')
result=[color for color in color_list1 if color not in color_list2]
print("Colors in color_list1 not contained in color_list2:")
for color in result:
 print(color)
