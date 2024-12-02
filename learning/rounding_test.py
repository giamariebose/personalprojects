import math

def round_up_to_nearest_hundredth(x):
    return round(math.ceil(x * 100)) / 100

x = 3.1415
print(f"X set to {x}")
round_up_to_nearest_hundredth(x)
print(f"rounded to : {x}")