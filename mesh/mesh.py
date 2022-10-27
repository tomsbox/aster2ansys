from pathlib import Path
from .node import Node
from .element import ElementTET10, ElementTRIA6
from .set_node import SetNode
from .set_element import SetElement


def remove_underscore_as_first_char_in_group_names(name):
    if name[0] == "_":
        return name[1:]
    else:
        return name


class Mesh:

    # _mesh_reader=
    # _mesh_writer=

    def __init__(self, file_with_path, output_file_name):
        self.file_with_path = file_with_path
        self.output_file_name = output_file_name
        self.lines = ""
        self.nodes = []
        self.elements = {"TET10": [], "TRIA6": []}
        self.set_nodes = []
        self.set_elements = []
        self.read_file()
        self.read_nodes()
        self.read_elements()
        self.read_sets_node()
        self.read_sets_element()

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

    def read_elements(self):

        index_of_start_lines_with_first_element_of_element_blocks = []
        index_of_end_lines_with_last_element_of_element_blocks = []
        ###########################################################################################################
        for index, line in enumerate(self.lines):
            if "eblock" in line:
                index_of_start_lines_with_first_element_of_element_blocks.append(index + 2)
                #print(f"line: {line}")

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

                    if index_of_start_lines_with_first_element_of_element_blocks[index_of_startline] <= index <= index_of_end_lines_with_last_element_of_element_blocks[index_of_startline]:
                        element_info_line_1 = self.lines[index].split()
                        element_info_line_2 = self.lines[index + 1].split()
                        try:
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

                        except IndexError:
                            pass



            # TRIA6
            if int(element_type) == 154:
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

    def read_sets_node(self):
        index_of_start_lines_with_first_nodes_of_set_nodes = []
        index_of_end_lines_with_last_nodes_of_set_nodes = []

        ###########################################################################################################
        for index, line in enumerate(self.lines):
            if "CMBLOCK" in line:
                # print(f"line: {line}")
                # print(f"set node name: {line.split(',')[1]}")

                index_of_start_lines_with_first_nodes_of_set_nodes.append(index + 2)
                self.set_nodes.append(SetNode(line.split(',')[1]))

            if ("golist" in line or "cmsel" in line) and len(index_of_start_lines_with_first_nodes_of_set_nodes) > 0:
                index_of_end_lines_with_last_nodes_of_set_nodes.append(index - 1)

        for set in self.set_nodes:
            print(f"set name from set note object: {set.get_set_node_name()}")

        print(
            f"index_of_start_lines_with_first_nodes_of_set_nodes: {index_of_start_lines_with_first_nodes_of_set_nodes}")
        print(
            f"index_of_end_lines_with_last_nodes_of_set_nodes: {index_of_end_lines_with_last_nodes_of_set_nodes}")
        ###########################################################################################################

        for index_of_startline, dummy in enumerate(index_of_start_lines_with_first_nodes_of_set_nodes):

            print(f"index_of_startline: {index_of_startline}")
            print(index_of_start_lines_with_first_nodes_of_set_nodes[index_of_startline])
            print(index_of_end_lines_with_last_nodes_of_set_nodes[index_of_startline])

            for index, line in enumerate(self.lines):

                if index_of_start_lines_with_first_nodes_of_set_nodes[index_of_startline] <= index <= \
                        index_of_end_lines_with_last_nodes_of_set_nodes[index_of_startline]:

                    #print(f"line: {line}")
                    #print(f"line.split(): {line.split()}")

                    for node in line.split():
                        #print(f"node: {int(node)}")
                        self.set_nodes[index_of_startline].add_node(int(node))

        for set in self.set_nodes:
            print(f"set name from set note object: {set.get_node_set()}")

    def read_sets_element(self):
        index_of_start_lines_with_first_element_of_set_elements = []
        index_of_end_lines_with_last_element_of_set_elements = []

        ###########################################################################################################
        for index, line in enumerate(self.lines):
            if "Define Pressure Using Surface Effect Elements" in line:
                #print(f"line: {line}")
                index_of_start_lines_with_first_element_of_set_elements.append(index + 4)
                self.set_elements.append(SetElement("pressure"))

            if line[0:2] == "-1" and len(index_of_start_lines_with_first_element_of_set_elements) > 0:
                #print(f"line: {line}")
                index_of_end_lines_with_last_element_of_set_elements.append(index - 1)

        for set in self.set_elements:
            print(f"set name from set element object: {set.get_set_element_name()}")

        print(
            f"index_of_start_lines_with_first_element_of_set_elements: {index_of_start_lines_with_first_element_of_set_elements}")
        print(
            f"index_of_end_lines_with_last_element_of_set_elements: {index_of_end_lines_with_last_element_of_set_elements}")
        ###########################################################################################################

        for index_of_startline, dummy in enumerate(index_of_start_lines_with_first_element_of_set_elements):

            print(f"index_of_startline: {index_of_startline}")
            print(index_of_start_lines_with_first_element_of_set_elements[index_of_startline])
            print(index_of_end_lines_with_last_element_of_set_elements[index_of_startline])

            for index, line in enumerate(self.lines):

                if index_of_start_lines_with_first_element_of_set_elements[index_of_startline] <= index <= \
                        index_of_end_lines_with_last_element_of_set_elements[index_of_startline]:
                    # print(f"line: {line}")
                    # print(f"line.split(): {line.split()}")
                    # print(f"line.split()[0]: {line.split()[0]}")
                    # print(f"index_of_startline: {index_of_startline}")
                    # print(self.set_elements)
                    self.set_elements[index_of_startline].add_element(line.split()[0])



    def write_header(self):
        with open(Path(self.file_with_path).parent.resolve() / self.output_file_name, "a") as file:
            file.writelines(" TITRE\n")
            file.writelines(" %  Hand made mesh from ansys\n")
            file.writelines(" FINSF\n")

    def write_footer(self):
        with open(Path(self.file_with_path).parent.resolve() / self.output_file_name, "a") as file:
            file.writelines(" FIN\n")

    def write_nodes(self):
        with open(Path(self.file_with_path).parent.resolve() / self.output_file_name, "a") as file:
            file.writelines(" COOR_3D\n")
            for node in self.nodes:
                file.writelines(node.get_node_definition() + "\n")
            file.writelines(" FINSF\n")

    def write_elements(self):
        with open(Path(self.file_with_path).parent.resolve() / self.output_file_name, "a") as file:

            file.writelines(" TETRA10\n")

            for element in self.elements["TET10"]:
                # print(element.get_element_definition())
                file.writelines(" ")
                for index, item in enumerate(element.get_element_definition()):
                    # print(f"item: {item}")
                    file.writelines(item + "   ")
                    if index == element.get_possible_items_per_line() - 1:
                        file.writelines("\n")
                        file.writelines("   ")
                file.writelines("\n")

            file.writelines(" FINSF\n")

            file.writelines(" TRIA6\n")
            for element in self.elements["TRIA6"]:
                file.writelines(" ")
                for index, item in enumerate(element.get_element_definition()):
                    file.writelines(item)
                    file.writelines("   ")
                file.writelines("\n")
            file.writelines(" FINSF\n")

    def write_set_node(self):
        with open(Path(self.file_with_path).parent.resolve() / self.output_file_name, "a") as file:
            for set_node in self.set_nodes:
                file.writelines(" GROUP_NO\n")
                file.writelines(" " + remove_underscore_as_first_char_in_group_names(set_node.get_node_set()["name"]) + "\n")
                file.writelines(" ")
                for index, item in enumerate(set_node.get_node_set()["nodes"]):
                    file.writelines("N" + str(item) + "   ")
                    if index != 0 and index % set_node.get_possible_items_per_line() == 0:
                        file.writelines("\n")
                        file.writelines(" ")
                file.writelines("\n")
                file.writelines(" FINSF\n")

    def write_set_elements(self):
        with open(Path(self.file_with_path).parent.resolve() / self.output_file_name, "a") as file:
            for set_element in self.set_elements:
                file.writelines(" GROUP_MA\n")
                file.writelines(" " + remove_underscore_as_first_char_in_group_names(set_element.get_element_set()["name"]) + "\n")
                file.writelines(" ")
                for index, item in enumerate(set_element.get_element_set()["elements"]):
                    file.writelines("M" + str(item) + "   ")
                    if index != 0 and index % set_element.get_possible_items_per_line() == 0:
                        file.writelines("\n")
                        file.writelines(" ")
                file.writelines("\n")
                file.writelines(" FINSF\n")
