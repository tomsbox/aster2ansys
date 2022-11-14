from mesh import Mesh
from pathlib import Path
import unittest
import filecmp

current_path = Path(__file__).parent.resolve()


class MeshTest(unittest.TestCase):
    # TODO: Subtests for all example files
    def setUp(self):
        self.file_name = 'Qube_for_aster_TET10_0p5mm'
        self.file = current_path / "example_files/ansys_mesh" / (self.file_name + ".dat")
        self.result_file = current_path / "example_files/ansys_mesh" / (self.file_name + ".mail")
        self.result_file_reference = current_path / "example_files/ansys_mesh" / (self.file_name + "_reference.mail")

    def test_read_ansys_mesh_and_write_aster_mesh_complete_process(self):
        # read the ansys mesh
        mesh = Mesh(self.file, self.file_name + ".mail")
        # write the aster mesh
        mesh.write_header()
        mesh.write_nodes()
        mesh.write_elements()
        mesh.write_set_node()
        mesh.write_set_elements()
        mesh.write_footer()

        self.assertTrue(Path.is_file(self.result_file))
        self.assertTrue(filecmp.cmp(self.result_file, self.result_file_reference, shallow=False))

    def tearDown(self):
        Path(self.result_file).unlink()
