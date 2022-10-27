class SetElement:

    def __init__(self, set_name):
        self._set_name = set_name
        self._list_of_elements = []

    def get_possible_items_per_line(self):
        return 5

    def add_element(self, node):
        self._list_of_elements.append(node)

    def get_set_element_name(self):
        return self._set_name

    def get_element_set(self):
        return {"name": self._set_name, "elements": self._list_of_elements}
