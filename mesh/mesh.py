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

    def write_nodes(self):
        with open(Path(self.file_with_path).parent.resolve() / self.output_file_name, "a") as file:
            for node in self.nodes:
                file.writelines(node.get_node_definition() + "\n")

    def read_elements(self):

        index_of_start_lines_with_first_element_of_element_blocks = []
        index_of_end_lines_with_last_element_of_element_blocks = []
        ###########################################################################################################
        for index, line in enumerate(self.lines):
            if "eblock" in line:
                index_of_start_lines_with_first_element_of_element_blocks.append(index + 2)
                print(f"line: {line}")

            if line[0:2] == "-1" and len(index_of_start_lines_with_first_element_of_element_blocks) > 0:
                index_of_end_lines_with_last_element_of_element_blocks.append(index - 1)

        print(
            f"index_of_start_lines_with_first_element_of_element_blocks: {index_of_start_lines_with_first_element_of_element_blocks}")
        print(
            f"index_of_end_lines_with_last_element_of_element_blocks: {index_of_end_lines_with_last_element_of_element_blocks}")
        ###########################################################################################################

        for index_of_startline, element_block in enumerate(index_of_start_lines_with_first_element_of_element_blocks):
            print(f"index_of_startline: {index_of_startline}")
            element_type = \
                self.lines[index_of_start_lines_with_first_element_of_element_blocks[index_of_startline] - 3].split(
                    ',')[-1]
            print(f"element_type: {element_type}")

            # TET10
            if int(element_type) == 187:
                print("TET10")
                for index, line in enumerate(self.lines):
                    if index_of_start_lines_with_first_element_of_element_blocks[index_of_startline] <= index <= \
                            index_of_end_lines_with_last_element_of_element_blocks[
                                index_of_startline] and index % 2 == 1:
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
            if int(element_type) == 154:
                print("TRIA6")
                print(index_of_start_lines_with_first_element_of_element_blocks[index_of_startline])
                print(index_of_end_lines_with_last_element_of_element_blocks[index_of_startline])
                for index, line in enumerate(self.lines):
                    if index_of_start_lines_with_first_element_of_element_blocks[index_of_startline] <= index <= \
                            index_of_end_lines_with_last_element_of_element_blocks[index_of_startline]:
                        element_info_line = self.lines[index].split()
                        number = element_info_line[0]
                        node_01 = element_info_line[5]
                        node_02 = element_info_line[6]
                        node_03 = element_info_line[7]
                        node_04 = element_info_line[9]
                        node_05 = element_info_line[10]
                        node_06 = element_info_line[12]

                        self.elements["TRIA6"].append(
                            ElementTRIA6(number, node_01, node_02, node_03, node_04, node_05, node_06)
                        )

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

            for element in self.elements["TRIA6"]:
                print(f"element: {element}")
                file.writelines(" ")
                for index, item in enumerate(element.get_element_definition()):
                    file.writelines(item)
                    file.writelines("   ")
                file.writelines("\n")
