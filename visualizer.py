import matplotlib.pyplot as plt
import numpy as np


def Cube_3D(voxels, len_x=8, len_y=8, len_z=8):
    # создаем 3D фигуру
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Координаты точек для дискретного 3D куба
    x, y, z = np.indices((len_x, len_y, len_z))

    # Визуализируем куб
    ax.voxels(voxels, edgecolor='k')

    # Масштаб осей
    ax.set_xlim(0, len_x - 1)
    ax.set_ylim(0, len_y - 1)
    ax.set_zlim(0, len_z - 1)

    plt.show()
