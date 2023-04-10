import trimesh
import numpy as np


def compression(path, len_x=8, len_y=8, len_z=8):
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

                # Вычисление координаты текущей точки
                x = new_bbox[0][0] + i * step_x
                y = new_bbox[0][1] + j * step_y
                z = new_bbox[0][2] + k * step_z

                # Проверка, находится ли точка внутри сетки
                if mesh.contains(np.array([[x, y, z]])):
                    grid[i, j, k] = True
    return grid
