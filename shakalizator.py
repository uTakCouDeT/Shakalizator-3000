import multiprocessing
import trimesh
import numpy as np
import multiprocessing as mp
from layer import layer


def compression_begin(path, len_x=8, len_y=8, len_z=8):
    # Загружаем модель
    mesh = trimesh.load(path)

    # Находим центр масс модели
    center = mesh.center_mass

    # Перемещаем модель так, чтобы центр масс совпадал с началом координат
    mesh.apply_translation(-center)

    # Пустой массив размером 8x8x8
    grid = np.zeros((len_x, len_y, len_z), dtype=bool)

    # Рамка ограничивающая модель
    bbox = mesh.bounding_box.bounds

    # Учитываем масштаб фигуры
    min_coord = min(bbox[0])
    max_coord = max(bbox[1])
    new_bbox = np.array([[min_coord] * 3, [max_coord] * 3])

    # Размер шага для каждой оси
    step_x = (new_bbox[1][0] - new_bbox[0][0]) / len_x
    step_y = (new_bbox[1][1] - new_bbox[0][1]) / len_y
    step_z = (new_bbox[1][2] - new_bbox[0][2]) / len_z

    # Проходим по каждой точке сетки
    for i in range(len_x):
        for j in range(len_y):
            for k in range(len_z):

                # Вычисление координаты текущего кубика
                x_begin = new_bbox[0][0] + i * step_x
                y_begin = new_bbox[0][1] + j * step_y
                z_begin = new_bbox[0][2] + k * step_z

                # Проверка, находится ли точка внутри сетки
                if mesh.contains(np.array([[x_begin, y_begin, z_begin]])):
                    grid[i, j, k] = True

    return grid


def compression(path, len_x=8, len_y=8, len_z=8):
    # Загружаем модель
    mesh = trimesh.load(path)

    # Находим центр масс модели
    center = mesh.center_mass

    # Перемещаем модель так, чтобы центр масс совпадал с началом координат
    mesh.apply_translation(-center)

    # Рамка ограничивающая модель
    bbox = mesh.bounding_box.bounds

    # Учитываем масштаб фигуры
    min_coord = min(bbox[0])
    max_coord = max(bbox[1])
    new_bbox = np.array([[min_coord] * 3, [max_coord] * 3])

    # Размер шага для каждой оси
    step_x = (new_bbox[1][0] - new_bbox[0][0]) / len_x
    step_y = (new_bbox[1][1] - new_bbox[0][1]) / len_y
    step_z = (new_bbox[1][2] - new_bbox[0][2]) / len_z

    # Считаем объем кубика
    small_box = trimesh.creation.box(bounds=[[new_bbox[0][0], new_bbox[0][1], new_bbox[0][2]],
                                             [new_bbox[0][0] + step_x, new_bbox[0][1] + step_y,
                                              new_bbox[0][2] + step_z]])

    big_box = trimesh.creation.box(bounds=new_bbox)
    volume_part = mesh.volume / big_box.volume

    # Задаем массив с данными для передачи потокам
    manager = multiprocessing.Manager()
    dict_value = manager.dict({
        'bbox': new_bbox,
        'step_x': step_x,
        'step_y': step_y,
        'step_z': step_z,
        'mesh': mesh,
        'volume_part': volume_part,
        'small_box_volume': small_box.volume,
        'len_x': len_x,
        'len_y': len_y,
        'len_z': len_z,
    })

    print(f'part:{volume_part} small_box:{small_box.volume} model: {mesh.volume} big_box: {big_box.volume}')

    # Проходим по каждой точке сетки
    threads = []
    for i in range(len_x):
        th = mp.Process(target=layer, args=(dict_value, i,))
        th.start()
        threads.append(th)

    for th in threads:
        th.join()

    # Собираем все слои в одну сетку
    grid = dict_value[f'layer0']
    for i in range(1, 8):
        grid = np.vstack([grid, dict_value[f'layer{i}']])

    return grid
