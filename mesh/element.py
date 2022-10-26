class Element:

    def __init__(self, number=None, node_01=None, node_02=None, node_03=None, node_04=None, node_05=None, node_06=None,
                 node_07=None, node_08=None, node_09=None, node_10=None):
        self._number = number
        self._node_01 = node_01
        self._node_02 = node_02
        self._node_03 = node_03
        self._node_04 = node_04
        self._node_05 = node_05
        self._node_06 = node_06
        self._node_07 = node_07
        self._node_08 = node_08
        self._node_09 = node_09
        self._node_10 = node_10

    def get_element_definition(self):
        return " " + "M" + self._number + "   N" + self._node_01 + "    N" + self._node_02 + "    N" + self._node_03 + \
               "    N" + self._node_04 + "    N" + self._node_05 + "    N" + self._node_06 + "    N" + self._node_07 + \
               "    N" + self._node_08 + "\n" "    N" + self._node_09 + "    N" + self._node_10
