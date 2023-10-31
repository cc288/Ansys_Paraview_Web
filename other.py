from ansys.mapdl import reader as pymapdl_reader

result = pymapdl_reader.read_binary('file.rst')
print(result)

result.save_as_vtk('file0.vtk', [0])