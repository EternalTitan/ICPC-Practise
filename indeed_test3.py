def doesCircleExist(commands):
    def left_turn(direction):
        return (direction + 3) % 4

    def right_turn(direction):
        return (direction + 1) % 4

    MOVEMENT = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    ans = []
    for each_command in commands:
        x = 0
        y = 0
        direction = 0
        for i in each_command:
            if i == 'G':
                x += MOVEMENT[direction][0]
                y += MOVEMENT[direction][1]
            elif i == 'L':
                direction = left_turn(direction)
            else:
                direction = right_turn(direction)
        if x == 0 and y == 0 or direction != 0:
            ans.append('YES')
        else:
            ans.append('NO')
    return ans


print(doesCircleExist(['G', 'L']))
