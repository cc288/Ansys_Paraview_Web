from ansys.mapdl import reader as pymapdl_reader

result=pymapdl_reader.read_binary(r'file0.rst')

result.plot_nodal_solution(0)

#result.plot_principal_nodal_stress(0,'seqv')

#result.plot_nodal_stress(0,'x')

#result.plot_nodal_displacement(0)

result.save_as_vtk('test.vtk',[0])




