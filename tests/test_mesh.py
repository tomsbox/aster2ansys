from mesh import Mesh
from pathlib import Path
import unittest

current_path = Path(__file__).parent.resolve()


class MeshTest(unittest.TestCase):

    def setUp(self):
        self.file_name = 'Klotz_for_aster_TET10_0p5mm'
        self.file = current_path / "example_files/ansys_mesh" / (self.file_name + ".dat")
        self.result_file = current_path / "example_files/ansys_mesh" / (self.file_name + ".mail")

    def test_mesh_reader(self):
        mesh = Mesh(self.file, self.file_name + ".mail")
        mesh.write_header()
        mesh.write_nodes()
        mesh.write_elements()
        mesh.write_set_node()
        mesh.write_set_elements()
        mesh.write_footer()
        self.assertTrue(Path.is_file(self.result_file))

    def tearDown(self):
        Path(self.result_file).unlink()
