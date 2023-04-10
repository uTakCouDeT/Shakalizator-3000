import visualizer
import shakalizator

# Путь до исходной модели
filename = 'models/Heart.obj'

# Масштаб сжатия
len_x, len_y, len_z = 28, 28, 28

# Функция сжатия 3D модели
grid = shakalizator.compression(filename, len_x, len_y, len_z)
print(grid)

# Визуализация результатов
visualizer.Cube_3D(grid, len_x, len_y, len_z)
