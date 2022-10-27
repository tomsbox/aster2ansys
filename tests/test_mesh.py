from mesh import Mesh
from pathlib import Path
import unittest

current_path = Path(__file__).parent.resolve()


class MeshTest(unittest.TestCase):
    def test_mesh_reader(self):
        print(f"current_path: {current_path}")
        print(f"oooooooooooooooooooooo")
        file = current_path / "example_files/ansys_mesh/Klotz_for_aster_TET10.dat"
        mesh = Mesh(file, "Klotz_for_aster_TET10.mail")
        mesh.write_header()
        mesh.write_nodes()
        mesh.write_elements()
        mesh.write_set_node()
        mesh.write_footer()
        self.assertTrue(True)
