from pathlib import Path
from .node import Node
from .element import Element


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
                node_info = line.split()
                self.nodes.append(Node(node_info[0], node_info[1], node_info[2], node_info[3]))

        print(f"index_start_line_nodes: {index_start_line_nodes}")
        print(f"index_end_line_nodes: {index_end_line_nodes}")

    def write_nodes(self):
        with open(Path(self.file_with_path).parent.resolve() / self.output_file_name, "a") as file:
            for node in self.nodes:
                file.writelines(node.get_node_definition() + "\n")

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

            if index >= index_start_line_elements and index <= index_end_line_elements and index % 2 == 1:
                element_info_line_1 = self.lines[index].split()
                print(f"element_info_line_1: {element_info_line_1}")
                element_info_line_2 = self.lines[index + 1].split()
                print(f"element_info_line_2: {element_info_line_2}")

                number = element_info_line_1[10]
                node_01 = element_info_line_1[11]
                node_02 = element_info_line_1[12]
                node_03 = element_info_line_1[13]
                node_04 = element_info_line_1[14]
                node_05 = element_info_line_1[15]
                node_06 = element_info_line_1[16]
                node_07 = element_info_line_1[17]
                node_08 = element_info_line_1[18]

                node_09 = element_info_line_2[0]
                node_10 = element_info_line_2[1]

                self.elements.append(Element(number=number, node_01=node_01, node_02=node_02, node_03=node_03,
                                             node_04=node_04, node_05=node_05, node_06=node_06, node_07=node_07,
                                             node_08=node_08, node_09=node_09, node_10=node_10))

        print(f"index_start_line_nodes: {index_start_line_elements}")
        print(f"index_end_line_nodes: {index_end_line_elements}")

    def write_elements(self):
        with open(Path(self.file_with_path).parent.resolve() / self.output_file_name, "a") as file:
            for element in self.elements:
                print(f"element: {element}")
                file.writelines(element.get_element_definition() + "\n")
