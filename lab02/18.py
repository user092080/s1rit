input=input("Enter a list of colors (comma separated):")
colors=input.split(',')
if len(colors)>=2:
 first_color = colors[0]
 last_color=colors[-1]
 print("First Color:",first_color)
 print("Last Color:",last_color)
