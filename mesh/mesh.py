from pathlib import Path
from .node import Node
from .element import ElementTET10, ElementTRIA6


class Mesh:

    # _mesh_reader=
    # _mesh_writer=

    def __init__(self, file_with_path, output_file_name):
        self.file_with_path = file_with_path
        self.output_file_name = output_file_name
        self.lines = ""
        self.nodes = []
        self.elements = {"TET10": [], "TRIA6": []}
        self.start_and_end_line_for_every_element_block = []

        self.read_file()
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

        # TODO: start_and_end_line_for_every_element_block = [[start_line_1,end_line_1],[start_line_2,end_line_2]]
        index_of_start_lines_with_first_element_of_element_blocks = []
        index_of_end_lines_with_last_element_of_element_blocks = []
        ###########################################################################################################
        for index, line in enumerate(self.lines):
            if "eblock" in line:
                index_of_start_lines_with_first_element_of_element_blocks.append(index + 2)
                print(f"line: {line}")

            if line[0:2] == "-1":
                index_of_end_lines_with_last_element_of_element_blocks.append(index - 1)
            # TODO filer node end line
            # self.start_and_end_line_for_every_element_block.append([index_start_line_elements, index_end_line_elements])

        print(
            f"index_of_start_lines_with_first_element_of_element_blocks: {index_of_start_lines_with_first_element_of_element_blocks}")
        print(
            f"index_of_end_lines_with_last_element_of_element_blocks: {index_of_end_lines_with_last_element_of_element_blocks}")
        ###########################################################################################################

        for index, line in enumerate(self.lines):
            if "eblock" in line:
                index_start_line_elements = index + 2
                break

        for index, line in enumerate(self.lines):
            if line[0:2] == "-1" and index > index_start_line_elements:
                index_end_line_elements = index - 1
                break

        element_type = self.lines[index_start_line_elements - 3].split(',')[-1]
        print(f"element_type: {element_type}")

        # TET10
        if int(element_type) == int(187):
            print("TET10")
            for index, line in enumerate(self.lines):
                if index_start_line_elements <= index <= index_end_line_elements and index % 2 == 1:
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

                    self.elements["TET10"].append(
                        ElementTET10(number, node_01, node_02, node_03, node_04, node_05,
                                     node_06, node_07, node_08, node_09, node_10)
                    )

        # TRIA6
        if element_type == 154:
            print("TRIA6")

        print(f"index_start_line_nodes: {index_start_line_elements}")
        print(f"index_end_line_nodes: {index_end_line_elements}")

    def write_elements(self):
        with open(Path(self.file_with_path).parent.resolve() / self.output_file_name, "a") as file:
            for element in self.elements["TET10"]:
                print(f"element: {element}")
                file.writelines(" ")
                for index, item in enumerate(element.get_element_definition()):
                    file.writelines(item + "   ")
                    if index == element.get_possible_items_per_line() - 1:
                        file.writelines("\n")
                        file.writelines("   ")
                file.writelines("\n")
