class Node:

    def __init__(self, number, x_coord, y_coord, z_coord):
        self._number = number
        self._x = x_coord
        self._y = y_coord
        self._z = z_coord

    def get_node_definition(self):
        return " " + "N" + self._number + "   " + self._x + "    " + self._y + "    " + self._z
