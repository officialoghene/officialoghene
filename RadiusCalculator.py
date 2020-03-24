intro = """
Type the radius(r) of your circle to get the area. EG:
Radius(r) >> 4.5
Type number less than '0' to Quit the program
"""
print(intro)
while True:    
    try:
        r = float(input("Radius >> "))
    except ValueError:
        print("Syntax Error")
    else:
        if r < 0:
            print("Hey, that's too small :)")
        elif r == 0:
            print("Bye")
            break
        else:
            ans = (22/7) * (r**2)
            print(f"For radius {r}, Area = {ans}")
    
