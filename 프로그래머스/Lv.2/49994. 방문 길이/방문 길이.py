def solution(dirs):

    cur_coor = (0, 0)
    visited = set()
    command = {"U": (0,1), "L": (-1,0), "R": (1,0), "D": (0,-1)}

    for dir in dirs:
        x, y = command[dir]
        next_x = cur_coor[0] + x
        next_y = cur_coor[1] + y

        if next_x >= -5 and next_x <= 5 and next_y >= -5 and next_y <= 5:
            next_coor = (next_x, next_y)
            route = (min(cur_coor, next_coor), max(cur_coor, next_coor))
            visited.add(route)
            cur_coor = next_coor

    return len(visited)