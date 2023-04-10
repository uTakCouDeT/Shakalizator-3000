import trimesh

mesh = trimesh.creation.cylinder(radius=10.0, height=1.0)
mesh.export('models/cylinder.obj')

mesh = trimesh.creation.icosphere(radius=10.0)
mesh.export('models/sphere.obj')
