import grid
import node

""" Directions for movement options """

directions = ['up','down','left','right']

""" Function that sets the tail point we can follow """

def followTail(x, y):
    tailX = x
    tailY = y
    tailPoint = (tailX, tailY)
    return tailPoint

"""
Function that checks what are health is at and returns true
if it is below a certain point
"""

def checkHealth(health):
    if health >= 80:
        print("true")
        return True

"""
Function that finds food and returns the closest one to our snake head
"""

def findFood(foodPos, x, y):
    foodToEat = (foodPos[1]['x'], foodPos[1]['y'])
    for food in foodPos:
        if((abs(food['x'] - x) + abs(food['y'] - y)) < abs((foodToEat[0] - x) + abs(foodToEat[1] - y))):
            foodToEat = (food['x'], food['y'])
    return foodToEat

""" Implementation of our astar pathfinding from node.py """

def move(grid, data):
    """
    Variables for all board related data such as
    food, height, width, and snakes
    """
    height = data['board']['height']
    width = data['board']['width']
    foodPos = data['board']['food']
    enemySnakes = data['board']['snakes']
    enemySnakeHeads = data['board']['snakes'][0]

    """
    Our snake information such as id, name, position,
    and health
    """
    id = data['you']['id']
    name = data['you']['name']
    body = data['you']['body']
    xHeadPos = body[0]['x']
    yHeadPos = body[0]['y']
    xTailPos = body[-1]['x']
    yTailPos = body[-1]['y']

    foodToEat = findFood(foodPos, xHeadPos, yHeadPos)
    end = (foodToEat[0], foodToEat[1])
    start = (xHeadPos, yHeadPos)

    path = node.aStar(grid, start, end)
    next_path = path[1]
    print(path)

    if (next_path[0] == xHeadPos + 1):
        return 3

    elif (next_path[0] == xHeadPos - 1):
        return 2

    elif (next_path[1] == yHeadPos + 1):
        return 1

    else:
        return 0
