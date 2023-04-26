import trimesh
import numpy as np


# Функция для работы нескольких потоков
def layer(dict_value, i):

    # Создаем один из слоев в потоке
    lay = np.zeros((1, dict_value['len_y'], dict_value['len_z']), dtype=bool)

    for j in range(dict_value['len_y']):
        for k in range(dict_value['len_z']):
            # Вычисление координаты текущего кубика
            # Минимальная точка
            x_begin = dict_value['bbox'][0][0] + i * dict_value['step_x']
            y_begin = dict_value['bbox'][0][1] + j * dict_value['step_y']
            z_begin = dict_value['bbox'][0][2] + k * dict_value['step_z']

            # Максимальная точка
            x_end = x_begin + dict_value['step_x']
            y_end = y_begin + dict_value['step_y']
            z_end = z_begin + dict_value['step_z']

            # Проверка сколько объема фигуры находится в области кубика
            small_box = trimesh.creation.box(bounds=[[x_begin, y_begin, z_begin], [x_end, y_end, z_end]])
            inter = trimesh.boolean.intersection([dict_value['mesh'], small_box])
            main_volume = inter.volume

            print(f'{main_volume}: {i} {j} {k}')

            if main_volume >= dict_value['volume_part'] * dict_value['small_box_volume']:
                lay[0, j, k] = True

            dict_value[f'layer{i}'] = lay
