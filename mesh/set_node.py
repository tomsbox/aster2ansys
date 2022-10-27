class SetNode:

    def __init__(self, set_name):
        self._set_name = set_name
        self._list_of_nodes = []

    def get_possible_items_per_line(self):
        return 5

    def add_node(self, node):
        self._list_of_nodes.append(node)

    def get_set_node_name(self):
        return self._set_name

    def get_node_set(self):
        return {"name": self._set_name, "nodes": self._list_of_nodes}
