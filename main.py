import visualizer
import numpy as np
import json

model_name = 'sphere'

if __name__ == '__main__':
    # Путь до исходной модели
    filename = f'json_data/{model_name}.json'

    with open(filename) as reader:
        data = json.load(reader)
        voxels = np.array(data['voxels'])

    # Визуализируем модель
    visualizer.Cube_3D(voxels)
