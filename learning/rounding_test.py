import math

xrounded = float('0')

def round_up_to_nearest_hundredth(x):
    #xceil = math.ceil(x*100)
    #xceildivided = xceil / 100
    #return xceildivided
    return math.ceil(x * 100) / 100

x = float('3.1415')
print(f"X set to {x}")
roundedx = round_up_to_nearest_hundredth(x)
print(f"rounded to : {roundedx}")

xceil = math.ceil(x*100)
print(f"ceiling of x: {xceil}")

xceildivided = xceil / 100
print(f"xceil devided: {xceildivided}")