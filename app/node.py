class Node():
    # This class will be used for the A* Pathfinding Algorithm #

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

def aStar(grid, start, end):
    # Returns a list of tuples as a path from the given start to the given end in the given grid #

    # Create start and end node #
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # initialize both the open and closed lists #
    open_list = []
    closed_list = []

    # Add the start node the open list #
    open_list.append(start_node)

    # Loop until you find the end #
    while len(open_list) > 0:

        # Get the current Node #
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list and add it to the closed list #
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal #
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]
            # This returns the reversed Path #

        # Generate Children #
        children = []
        for new_position in [(0, -1),
                            (0, 1),
                            (-1, 0),
                            (1, 0)]:  # Adjacent squares #

            # Get node position #
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range #
            if node_position[0] > (len(grid) - 1) or node_position[0] < 0 or node_position[1] > (len(grid[len(grid)-1]) -1) or node_position[1] < 0:

            # Make sure area is safe to enter #
                if grid[node_position[0]][node_position[1]] != 0:
                    continue

            # Create the new node #
            new_node = Node(current_node, node_position)

            # Append #
            children.append(new_node)

        # Loop through the children #
        for child in children:

            # Child is in the closed list #
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values #
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list #
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list #
            open_list.append(child)

def createGrid(data):

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
    food = 0

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
        grid[food['y']][food['x']] = food

    """ Plotting snakes that are on the board in the grid """
    print(enemySnakeHeads['body'])
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
    grid[xTailPos][yTailPos] = tail

    return grid

# def main():
#
#         grid = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
#
#         start = (0, 5)
#         end = (7, 6)
#
#         path = aStar(grid, start, end)
#         print(path)
#
#
# if __name__ == '__main__':
#     main()
