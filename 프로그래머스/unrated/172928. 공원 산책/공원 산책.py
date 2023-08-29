def solution(park, routes):
    answer = []
    is_continue = True
    # find 현재위치
    for row, line in enumerate(park):
        if not is_continue:
            break
        for col, cell in enumerate(line):
            if cell == 'S':
                answer = [row, col]
                is_continue = False
                break
    
    for route in routes:
        cur_row = answer[0]
        cur_col = answer[1]
        route_direction, route_distance = route.split()
        route_distance = int(route_distance)
        is_okay = True

        if route_direction == 'E':
            if cur_col + route_distance >= len(park[0]):
                continue
            for i in range(1, route_distance + 1):
                if park[cur_row][cur_col + i] == 'X':
                    is_okay = False
                    break
            if is_okay:
                answer = [cur_row, cur_col + route_distance]

        elif route_direction == 'W':
            if cur_col - route_distance < 0:
                continue
            for i in range(1, route_distance + 1):
                if park[cur_row][cur_col - i] == 'X':
                    is_okay = False
                    break
            if is_okay:
                answer = [cur_row, cur_col - route_distance]

        elif route_direction == 'S':
            if cur_row + route_distance >= len(park[0]):
                continue
            for i in range(1, route_distance + 1):
                if park[cur_row + i][cur_col] == 'X':
                    is_okay = False
                    break
            if is_okay:
                answer = [cur_row + route_distance, cur_col]

        else:
            if cur_row - route_distance < 0:
                continue
            for i in range(1, route_distance + 1):
                if park[cur_row - i][cur_col] == 'X':
                    is_okay = False
                    break
            if is_okay:
                answer = [cur_row - route_distance, cur_col]

    return answer
