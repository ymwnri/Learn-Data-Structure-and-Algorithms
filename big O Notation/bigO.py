colors = ['green', 'yellow', 'blue', 'pink'] 

# O(1) - Constant Time
def constant(colors):
    print(colors[2]) 

constant(colors)

# O(n) - Linear Time
def linear(colors):
    for color in colors:
        print(color)

#O(n log n) - Linearithmic Time
def linearithmic(colors):
    colors.sort()
    for color in colors:
        print(color)

# O(n^2) - Quadratic Time
def quadratic(colors):
    for color1 in colors:
        for color2 in colors:
            print(color1, color2)

# O(n^3) - Cubic Time
def cubic(colors):
    for color1 in colors:
        for color2 in colors:
            for color3 in colors:
                print(color1, color2, color3)
