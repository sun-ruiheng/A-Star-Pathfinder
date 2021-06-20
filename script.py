import pygame
from heap import *
#EXPLORE DIFFERENT MULTIPLIERS TO H AND D IN COMPOSITION OF T
text = (
    '''
    Welcome to A* Pathfinder!\n
    This program sniffs out the shortest route linking two points, efficiently (with some exceptions).\n
    It implements the A* algorithm, an informed greedy algorithm that utilises heuristics to explore in the right general direction, avoiding unnecessary complexity.\n
    \n
    Enter anything below to start the program, then click to give it a Start point (Red), End point (Green), then Walls (Black).\n
    When you're satisfied with your maze, press space to run the algorithm, and watch it explore!\n
    Spacebar also lets you try again once the path is found, or if you're stuck.\n
    '''
)

response = input(text)
if response:
    pygame.init()

pygame.display.set_caption(" A* Pathfinder")
icon = pygame.image.load('maze.png')
pygame.display.set_icon(icon)

bounds = (500, 500)
screen = pygame.display.set_mode(bounds)
grid_length = 20


def lets_go():

    matrix = [[5000 for i in range(25)] for x in range(25)]
    matrix2 = [[i*20 for i in range(25)] for x in range(25)]

    for i in range(len(matrix2)):
        y = matrix2[i]
        yy = i * 20
        for x in y:
            pygame.draw.rect(screen, (255, 255, 255), (x, yy, 19, 19))

    press_count = 0
    end_coords = ()
    start_coords = ()

    def clicked(pos, color):
        x = pos[0] // grid_length
        y = pos[1] // grid_length
        value = 5000
        # to prevent replacing start/end:
        # if color == (0, 255, 0):
            # if (x, y) == start_coords:
            #     press_count = 1
            #     return
        if color == (0, 0, 0):
            # if (x, y) == start_coords or (x, y) == end_coords:
            #     return
            value = 10000
        pygame.draw.rect(screen, color, (x*20, y*20, 19, 19))
        matrix[y][x] = value

    running1 = True
    running2 = True
    running3 = True
    running4 = True

    # running1 is the loop where the user clicks around to set start, end, and walls
    while running1:
        pygame.time.delay(60)

        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running2 = False
            pygame.quit()
        if press_count < 2:

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if press_count == 0:
                    color = (255, 0, 0)
                    start_coords = (pos[0] // grid_length, pos[1] // grid_length)
                else:
                    if start_coords == (pos[0] // 20, pos[1] // 20): # dont allow rewriting of start point
                        continue
                    color = (0, 255, 0)
                    end_coords = (pos[0] // grid_length, pos[1] // grid_length)
                press_count += 1
                clicked(pos, color)
        else:
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                if start_coords == (pos[0] // 20, pos[1] // 20) or end_coords == (pos[0] // 20, pos[1] // 20): # dont allow rewriting of start or end
                    continue
                color = (0, 0, 0)
                press_count += 1
                clicked(pos, color)


        if pygame.mouse.get_pressed()[2]:
            pos = pygame.mouse.get_pos()
            clicked(pos, (255, 255, 255))
            press_count -= 1
        if pygame.key.get_pressed()[pygame.K_SPACE] and press_count > 1:
            running1 = False


        pygame.display.update()



    def straight_distance(pos):
        dist = ((end_coords[0] - pos[0])**2 + (end_coords[1] - pos[1])**2)**0.5
        return round(dist, 3)


    def get_t_value(pos, d_value):
        return straight_distance(pos) + d_value


    def get_neighbors(pos):
        neighbors = [
            (pos[0] + 1, pos[1]),
            (pos[0] - 1, pos[1]),
            (pos[0], pos[1] + 1),
            (pos[0], pos[1] - 1)
            ]
        for neighbor in neighbors[:]:
            if neighbor[0] > 24 or neighbor[1] > 24 or neighbor[0] < 0 or neighbor[1] < 0:
                neighbors.remove(neighbor)
        return neighbors


    current = [get_t_value(start_coords, 0), 0, start_coords]
    heap = MinHeap()

    #running2 is the algorithm doing its thing
    while running2:
        pygame.time.delay(50)

        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            pygame.quit()
        current_x = current[2][0]
        current_y = current[2][1]

        if matrix[current_y][current_x] > current[1]:
            matrix[current_y][current_x] = current[1] #replace d-value only with something smaller

        for neig in get_neighbors(current[2]): #add to heap in format [t_value, d_value, coords]
            if matrix[neig[1]][neig[0]] != 5000:
                continue
            if neig == end_coords:
                running2 = False
            # we need to find neig's neighbor that has lowest d_value
            neigneigs = get_neighbors(neig)
            source_d = min([matrix[neigneig[1]][neigneig[0]] for neigneig in neigneigs])
            d_value = 1 + source_d
            t_value = get_t_value(neig, d_value)
            heap.add([t_value, d_value, neig])
            matrix[neig[1]][neig[0]] = d_value

        current = heap.retrieve_min()
        try:
            current_x = current[2][0]
            current_y = current[2][1]
        except TypeError as e:
            print('No possible path! Press space to go again.')
            running3 = False
            break
        grey = (150, 150, 150)
        if running2:
            pygame.draw.rect(screen, grey, (current_x*20, current_y*20, 19, 19))

        pygame.display.update()


    current = [1, end_coords]
    heap = MinHeap()
    matrix[start_coords[1]][start_coords[0]] = -1

    #running3 is to find the shortest path back to start
    while running3:
        pygame.time.delay(50)
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            pygame.quit()

        for neig in get_neighbors(current[1]):
            x = neig[0]
            y = neig[1]
            if matrix[y][x]:
                d_value = matrix[y][x]
                if d_value == -1:
                    running3 = False
                heap.add([d_value, neig])
                matrix[y][x] = 0

        current = heap.retrieve_min()
        current_x = current[1][0]
        current_y = current[1][1]
        orange = (255, 165, 0)
        if running3:
            pygame.draw.rect(screen, orange, (current_x * 20, current_y * 20, 19, 19))
        pygame.display.update()

    #running4 doesnt do anything besides keeping the window alive
    while running4:
        pygame.time.delay(60)
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            pygame.quit()
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            lets_go()

lets_go()