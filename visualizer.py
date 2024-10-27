import matplotlib.pyplot as plt
import numpy as np


def Cube_3D(voxels, facecolors=None, len_x=8, len_y=8, len_z=8):
    # создаем 3D фигуру
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Визуализируем куб
    ax.voxels(voxels, facecolors=facecolors, edgecolor='k')

    # Масштаб осей
    ax.set_xlim(0, len_x - 1)
    ax.set_ylim(0, len_y - 1)
    ax.set_zlim(0, len_z - 1)

    # ax.view_init(0, -90)
    plt.show()
