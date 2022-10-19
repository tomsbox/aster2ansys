import pathlib
import os

import meshio

if __name__ == '__main__':
    # two triangles and one quad
    points = [
        [0.0, 0.0],
        [1.0, 0.0],
        [0.0, 1.0],
        [1.0, 1.0],
        [2.0, 0.0],
        [2.0, 1.0],
    ]
    cells = [
        ("triangle", [[0, 1, 2], [1, 3, 2]]),
        ("quad", [[1, 4, 5, 3]]),
    ]

    mesh = meshio.Mesh(
        points,
        cells,
        # Optionally provide extra data on points, cells, etc.
        point_data={"T": [0.3, -1.2, 0.5, 0.7, 0.0, -3.0]},
        # Each item in cell data must match the cells array
        cell_data={"a": [[0.1, 0.2], [0.4]]},
    )
    mesh.write(
        "foo.med",  # str, os.PathLike, or buffer/open file
        file_format="med",  # optional if first argument is a path; inferred from extension
    )

    # Alternative with the same options
    meshio.write_points_cells("foo.vtk", points, cells)

    filename = os.path.join(os.getcwd(), 'foo.med')
    print(f"filename: {filename}")

    mesh = meshio.read(
        filename,  # string, os.PathLike, or a buffer/open file
        # file_format="stl",  # optional if filename is a path; inferred from extension
        # see meshio-convert -h for all possible formats
    )
