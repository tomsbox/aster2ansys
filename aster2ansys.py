from mesh import Mesh
from pathlib import Path

if __name__ == '__main__':
    print("########### Welcome to ansys2aster the mesh converter_examples_by_astk including groups ###############")

    current_path = Path(__file__).parent.resolve()
    print(f"current_path: {current_path}")

    file_name = "Qube_for_aster_TET10_10mm_symm"
    input_file_with_path = current_path / "tests/example_files/ansys_mesh" / (file_name + ".dat")
    print(f"input_file_with_path: {input_file_with_path}")
    name_of_the_ouput_file = file_name + ".mail"

    mesh = Mesh(input_file_with_path, name_of_the_ouput_file)
    mesh.write_header()
    mesh.write_nodes()
    mesh.write_elements()
    mesh.write_set_node()
    mesh.write_set_elements()
    mesh.write_footer()
