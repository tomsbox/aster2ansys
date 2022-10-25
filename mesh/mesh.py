from pathlib import Path


def aster_node_line(line):
    number = line.split()[0]
    x_coordinate = line.split()[1]
    y_coordinate = line.split()[2]
    z_coordinate = line.split()[3]
    return " " + "N" + number + "   " + x_coordinate + "    " + y_coordinate + "    " + z_coordinate


class Mesh:

    # _mesh_reader=
    # _mesh_writer=

    def __init__(self, file_with_path, output_file_name):
        self.file_with_path = file_with_path
        self.output_file_name = output_file_name
        self.lines = ""
        self.read_file()
        self.nodes = []
        self.read_nodes()

    def read_file(self):
        with open(self.file_with_path, "r") as file:
            self.lines = file.readlines()

    def read_nodes(self):
        index_start_line_nodes = None
        index_end_line_nodes = None
        for index, line in enumerate(self.lines):
            if "nblock" in line:
                index_start_line_nodes = index + 2

        for index, line in enumerate(self.lines):
            if line[0:2] == "-1" and index > index_start_line_nodes:
                index_end_line_nodes = index - 1
                break

        for index, line in enumerate(self.lines):
            if index >= index_start_line_nodes and index <= index_end_line_nodes:
                self.nodes.append(aster_node_line(line))

        print(f"index_start_line_nodes: {index_start_line_nodes}")
        print(f"index_end_line_nodes: {index_end_line_nodes}")

    def write_nodes(self):
        with open(Path(self.file_with_path).parent.resolve() / self.output_file_name, "w") as file:
            for node in self.nodes:
                file.writelines(node + "\n")

