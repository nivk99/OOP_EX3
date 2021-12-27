import random
from src.NodeData import NodeData


class Node_Data(NodeData):
    """
     This class describes the vertices in the graph
    """

    def __init__(self, key: int = 0, location: tuple = None, weight: float = 0.0, info: str = "", tag: int = 0,
                 inDegree: dict = None, outDegree: dict = None):
        """"
        constructor
        """
        self._node_key = key
        self._node_location = location
        self._node_weight = weight
        self._node_info = info
        self._node_tag = tag
        self._inDegree = inDegree
        self._outDegree = outDegree

    def getKey(self) -> int:
        """

        :return:Vertex ID number
        """
        return self._node_key

    def getLocation(self) -> tuple:
        """

        :return: 3D point
        """
        if self._node_location is None:
            return random.random()*10,random.random()*10,0.0
        return self._node_location

    def setLocation(self, location: tuple) -> None:
        """

        :param location:new new location  (position) of this node.
        :return: the void
        """

        self._node_location = location

    def getWeight(self) -> float:
        """

        :return:  The weight of the vertex
        """
        return self._node_weight

    def setWeight(self, weight: float) -> None:
        """

        :param weight:- the new weight
        :return: the void
        """
        self._node_weight = weight;

    def getInfo(self) -> str:
        """

        :return:Get Info
        """
        return self._node_info

    def setInfo(self, info: str) -> None:
        """

        :param info: changes Info
        :return: the void
        """
        self._node_info = info

    def getTag(self) -> int:
        """

        :return: Get Tag
        """
        return self._node_tag

    def setTag(self, tag: int) -> None:
        """

        :param tag:  the new value of the tag
        :return: the void
        """
        self._node_tag = tag

    def __repr__(self) -> str:
        """
        :return:A string of the whole class
        """
        return f"{self._node_key}: |edges out| {len(self._outDegree)} |edges in| {len(self._inDegree)} "
if __name__ == '__main__':
   v = random.random()*10
   print(v)