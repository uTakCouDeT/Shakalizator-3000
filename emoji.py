import json
import numpy as np
import visualizer
from PIL import ImageColor


def hex_to_rgb(colors):
    rgb = np.zeros((len(colors), len(colors[0]), len(colors[0, 0])), dtype=tuple)
    for i in range(len(colors)):
        for j in range(len(colors[i])):
            for k in range(len(colors[i, j])):
                rgb[i, j, k] = ImageColor.getcolor(colors[i, j, k], "RGB")

    return rgb


def build_smile():

    filename = 'json_data/sphere.json'

    with open(filename) as reader:
        data = json.load(reader)
        voxels = np.array(data['voxels'])

    colors = voxels.copy()
    # Глаза смайлика
    colors[2, 1, 5] = False
    colors[5, 1, 5] = False
    # Улыбка
    colors[5, 1, 2] = False
    colors[4, 1, 1] = False
    colors[3, 1, 1] = False
    colors[2, 1, 2] = False
    facecolors = np.where(colors, '#ffff00', '#000000')

    rgb_format = hex_to_rgb(facecolors)

    input_data = {
        'rgb': rgb_format.tolist()
    }

    with open('emojis/smile.json', 'w') as writer:
        json.dump(input_data, writer)

    visualizer.Cube_3D(voxels, facecolors)


def build_sad():

    filename = 'json_data/sphere.json'

    with open(filename) as reader:
        data = json.load(reader)
        voxels = np.array(data['voxels'])

    colors = voxels.copy()
    # Глаза смайлика
    colors[2, 1, 5] = False
    colors[5, 1, 5] = False
    # Улыбка
    colors[5, 1, 1] = False
    colors[4, 0, 2] = False
    colors[3, 0, 2] = False
    colors[2, 1, 1] = False
    facecolors = np.where(colors, '#ffff00', '#000000')

    rgb_format = hex_to_rgb(facecolors)

    input_data = {
        'rgb': rgb_format.tolist()
    }

    with open('emojis/sad.json', 'w') as writer:
        json.dump(input_data, writer)

    visualizer.Cube_3D(voxels, facecolors)


build_smile()
build_sad()
