from pathlib import Path


def get_node_line_as_aster_mail(line):
    number = line.split()[0]
    x_coordinate = line.split()[1]
    y_coordinate = line.split()[2]
    z_coordinate = line.split()[3]
    return " " + "N" + number + "   " + x_coordinate + "    " + y_coordinate + "    " + z_coordinate


def get_element_line_as_aster_mail_TET10(line):
    try:
        number = line.split()[10]
        node_1 = line.split()[11]
        node_2 = line.split()[12]
        node_3 = line.split()[13]
        node_4 = line.split()[14]
        node_5 = line.split()[15]
        node_6 = line.split()[16]
        node_7 = line.split()[17]
        node_8 = line.split()[18]

        return " " + "M" + number + "   N" + node_1 + "    N" + node_2 + "    N" + node_3 + "    N" + node_4 + "    N" + node_5 + "    N" + node_6 + "    N" + node_7 + "    N" + node_8
    except IndexError:
        node_9 = line.split()[0]
        node_10 = line.split()[1]
        return "    N" + node_9 + "    N" + node_10


class Mesh:

    # _mesh_reader=
    # _mesh_writer=

    def __init__(self, file_with_path, output_file_name):
        self.file_with_path = file_with_path
        self.output_file_name = output_file_name
        self.lines = ""
        self.read_file()
        self.nodes = []
        self.elements = []
        self.read_nodes()
        self.read_elements()

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
                self.nodes.append(line)

        print(f"index_start_line_nodes: {index_start_line_nodes}")
        print(f"index_end_line_nodes: {index_end_line_nodes}")

    def write_nodes(self):
        with open(Path(self.file_with_path).parent.resolve() / self.output_file_name, "a") as file:
            for node in self.nodes:
                file.writelines(get_node_line_as_aster_mail(node) + "\n")

    def read_elements(self):
        index_start_line_elements = None
        index_end_line_elements = None
        for index, line in enumerate(self.lines):
            if "eblock" in line:
                index_start_line_elements = index + 2
                break

        for index, line in enumerate(self.lines):
            if line[0:2] == "-1" and index > index_start_line_elements:
                index_end_line_elements = index - 1
                break

        for index, line in enumerate(self.lines):
            if index >= index_start_line_elements and index <= index_end_line_elements:
                self.elements.append(line)

        print(f"index_start_line_nodes: {index_start_line_elements}")
        print(f"index_end_line_nodes: {index_end_line_elements}")

    def write_elements(self):
        with open(Path(self.file_with_path).parent.resolve() / self.output_file_name, "a") as file:
            for element in self.elements:
                print(f"element: {element}")
                file.writelines(get_element_line_as_aster_mail_TET10(element) + "\n")
