import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

ON = 255
OFF = 0
vals = [ON, OFF]
N = None  # side size
is_it_the_same = False  # he makes sure that he does not check the same tables twice
rounds_counter = 0
alive = 0  # number of living cells


def update(frame_num, img, grid, old_grid, N):
    global is_it_the_same, rounds_counter
    new_grid = grid.copy()
    for i in range(N):
        for j in range(N):
            total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                         grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                         grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
                         grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])/255)
            if grid[i, j] == ON:
                if (total < 2) or (total > 3):
                    new_grid[i, j] = OFF
            else:
                if total == 3:
                    new_grid[i, j] = ON
    img.set_data(new_grid)
    same_counter = 0
    for i in range(N*N):
    # checks if the old and new table is the same
        if rounds_counter > 0:
            if old_grid.reshape(N*N, 1)[i] == new_grid.reshape(N*N, 1)[i]:
                same_counter += 1
    if same_counter == N*N and is_it_the_same is False:
        is_it_the_same = True
        with open('data.txt', 'a') as data:
            print('%sx%s,%s,%s:%s' % (N, N, rounds_counter-1, alive, 1-alive),
                  file=data)
    old_grid[:] = grid[:]
    grid[:] = new_grid[:]
    rounds_counter += 1
    return img


def main():
    side_length()
    proportion()
    update_int = 100
    grid = np.random.choice(vals, N*N, p=[alive, 1-alive]).reshape(N, N)
    old_grid = grid.copy()
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, old_grid, N),
                                  frames=60, interval=update_int,
                                  save_count=50)
    plt.show()


def side_length():  # sets side length
    global N
    N = input('Enter the dimension of the side (10 - 100): ')
    if N not in map(str, range(10, 101)):
        print('Value out of range. Try one more time.')
        side_length()
    N = int(N)


def proportion():  # sets the proportion between living and dead cells
    global alive
    alive = input('''How many percent of the cells should be
alive in the first round(recommended 20): ''')
    if alive not in map(str, range(1, 101)):
        print('Enter an integer from 1 to 100.')
        proportion()
    alive = int(alive) / 100

main()
