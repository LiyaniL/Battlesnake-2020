def createGrid(data, verbose):

    """
    Variables for all board related data such as
    food, height, width, and snakes
    """
    height = data['board']['height']
    width = data['board']['width']
    foodPos = data['board']['food']
    enemySnakes = data['board']['snakes']
    enemySnakeHeads = data['board']['snakes'][0]

    head = 1
    snake = 1
    tail = 1
    foods = 0

    """ If verbose is true, debugging print statements will be printed """
    if verbose:
        print "Height: ", height, '\n'
        print "Width: ", width, '\n'
        print "Food Position: ", json.dumps(foodPos, indent=4, sort_keys=True), '\n'
        print "enemySnakes: ", json.dumps(enemySnakes, indent=4, sort_keys=True), '\n'
        print "enemySnakeHeads: ", json.dumps(enemySnakeHeads, indent=4, sort_keys=True), '\n'

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

    """ Grid Creation """
    grid = [[0 for col in range(width)] for row in range(height)]

    """ Plotting out the food in the board """
    for food in foodPos:
        grid[food['y']][food['x']] = foods

    """ Plotting snakes that are on the board in the grid """

    for cords in enemySnakeHeads['body']:
        grid[cords['y']][cords['x']] = snake

    for snakeHeads in enemySnakes:
        x = snakeHeads['body'][0]['x']
        y = snakeHeads['body'][0]['y']
        grid[y][x] = head

    """ Our snakes head and body positions """
    for cords in body:
        grid[cords['y']][cords['x']] = snake

    grid[yHeadPos][xHeadPos] = head
    grid[yTailPos][xTailPos] = tail

    return grid

"""
[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 0, 0, 0, {u'y': 3, u'x': 5}, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
"""
