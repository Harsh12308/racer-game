from kepoco import display, buttonL, buttonR, buttonB, reset  # L = left, R = right
import random  

display.setFPS(30)

width = display.width
height = display.height

# Car (player)
car_width, car_height = 5, 3
car_x = width // 2 - car_width // 2
car_y = height - car_height - 2

# Obstacle (enemy car)
obstacle = {
    "x": random.randint(1, width - 6),
    "y": -3,
    "width": 5,
    "height": 3
}

# Score
score = 0

def reset_obstacle(obs):
    obs["x"] = random.randint(1, width - obs["width"] - 1)
    obs["y"] = -obs["height"]

while True:

    # Exit & reset game when B is pressed
    if buttonB.justPressed():
        reset()

    # Car movement
    if buttonL.pressed():
        car_x -= 2
        if car_x < 1:
            car_x = 1

    if buttonR.pressed():
        car_x += 2
        if car_x > width - car_width - 1:
            car_x = width - car_width - 1

    # Move obstacle
    obstacle["y"] += 1

    if obstacle["y"] > height:
        reset_obstacle(obstacle)
        score += 1

    # Collision check
    if not (
        car_x + car_width < obstacle["x"] or
        car_x > obstacle["x"] + obstacle["width"] or
        car_y + car_height < obstacle["y"] or
        car_y > obstacle["y"] + obstacle["height"]
    ):
        score = 0
        reset_obstacle(obstacle)
        car_x = width // 2 - car_width // 2

    # Design

    # Background
    display.fill(display.BLACK)

    #Road borders
    display.drawLine(0, 0, 0, height, display.WHITE)
    display.drawLine(width - 1, 0, width - 1, height, display.WHITE)

    # Middle dashed line
    for y in range(0, height, 6):
        display.drawLine(width // 2, y, width // 2, y + 3, display.WHITE)

    #player car
    display.drawFilledRectangle(car_x, car_y, car_width, car_height, display.WHITE)

    #enemy car
    display.drawFilledRectangle(
        obstacle["x"], obstacle["y"],
        obstacle["width"], obstacle["height"],
        display.WHITE)

    #score
    display.drawText("Score:", 1, 1, display.WHITE)
    display.drawText(str(score), 35, 1, display.WHITE)

    display.update()
