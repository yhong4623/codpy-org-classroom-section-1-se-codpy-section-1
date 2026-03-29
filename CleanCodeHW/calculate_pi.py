from random import uniform

# Constant settings
RADIUS = 1
LOWER_BOUND = -RADIUS
UPPER_BOUND = RADIUS

NUM_POINTS = 1000000
AREA_FACTOR = 4
SQUARE_EXPONENT = 2
POINT_COUNT_INCREMENT = 1

inside_circle_count = 0

# Randomly generate points and count those inside the circle
for _ in range(NUM_POINTS):
    x = uniform(LOWER_BOUND, UPPER_BOUND)
    y = uniform(LOWER_BOUND, UPPER_BOUND)
    if x**SQUARE_EXPONENT + y**SQUARE_EXPONENT <= RADIUS**SQUARE_EXPONENT:
        inside_circle_count += POINT_COUNT_INCREMENT

# Estimate pi based on the number of points inside the circle
estimated_pi = (inside_circle_count / NUM_POINTS) * AREA_FACTOR

print(f"Estimated value of pi is: {estimated_pi}")
