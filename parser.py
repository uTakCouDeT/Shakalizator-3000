import visualizer
from shakalizator import compression, compression_begin
import json

model_name = 'Heart'

if __name__ == '__main__':
    # Путь до исходной модели
    filename = f'models/{model_name}.obj'

    # Масштаб сжатия
    len_x, len_y, len_z = 8, 8, 8

    # Функция сжатия 3D модели
    # grid = compression_begin(filename, len_x, len_y, len_z)
    grid = compression(filename, len_x, len_y, len_z)

    # Визуализация результатов
    visualizer.Cube_3D(grid, len_x, len_y, len_z)

    data = {
        'voxels': grid.tolist()
    }

    with open(f'json_data/{model_name}.json', 'w') as writer:
        json.dump(data, writer)