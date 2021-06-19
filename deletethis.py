

def get_neighbors(pos):
    neighbors = [
        (pos[0] + 1, pos[1]),
        (pos[0] - 1, pos[1]),
        (pos[0], pos[1] + 1),
        (pos[0], pos[1] - 1)
        ]
    for neighbor in neighbors:
        if neighbor[0] > 24 or neighbor[1] > 24:
            neighbors.remove(neighbor)
    return neighbors

eng_coor = ()
if True:
    eng_coor = (2,  1)
for neig in get_neighbors((1,1)):
    if neig == eng_coor:
        print('nice')
print(2)