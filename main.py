import pathlib
import os

import meshio

if __name__ == '__main__':

    filename = os.path.join(os.getcwd(), 'output_from_gmesh_with_pysikal_group_ttt.inp')
    print(f"filename: {filename}")

    mesh = meshio.read(
        filename,  # string, os.PathLike, or a buffer/open file
        # file_format="stl",  # optional if filename is a path; inferred from extension
        # see meshio-convert -h for all possible formats
    )

    mesh.write(
        "output_from_gmesh_with_pysikal_group_ttt.med",  # str, os.PathLike, or buffer/open file
        file_format="med",
        # binary=False# optional if first argument is a path; inferred from extension
    )

    mesh.write(
        "klotz_with_physical_out.vtk",  # str, os.PathLike, or buffer/open file
        file_format="vtk",
        binary=False
        # binary=False# optional if first argument is a path; inferred from extension
    )