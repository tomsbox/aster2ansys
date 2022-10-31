from mesh import Mesh

if __name__ == '__main__':
    print("########### Welcome to ansys2aster the mesh converter including groups ###############")

    input_file_with_path = "C:/Users/Thomas/Documents/WEBAPP/aster2ansys/tests/example_files/ansys_mesh/Klotz_for_aster_TET10_0p5mm.dat"
    name_of_the_ouput_file = "Klotz_for_aster_TET10_0p5mm_reference.mail"

    mesh = Mesh(input_file_with_path, name_of_the_ouput_file)
    mesh.write_header()
    mesh.write_nodes()
    mesh.write_elements()
    mesh.write_set_node()
    mesh.write_set_elements()
    mesh.write_footer()
