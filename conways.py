import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

ON = 255
OFF = 0
vals = [ON, OFF]
N = None

def update(frame_num, img, grid, N):
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
    grid[:] = new_grid[:]
    return img


def main():
    side_length()
    update_int = 100
    grid = np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N, N)
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N),
                                  frames=60, interval=update_int,
                                  save_count=50)
    plt.show()


def side_length():
    global N
    N = input('Enter the dimension of the side (20 - 1000): ')
    if N not in map(str, range(20, 1001)):
        print('Value out of range. Try one more time.')
        side_length()
    N = int(N)

main()
