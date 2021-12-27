class NodeData:
    """
     This interface represents the set of operations applicable on a
     ode (vertex) in a (directional) weighted graph.
    """

    def getKey(self) -> int:
        """
        :return:the key (id) associated with this node.
        """
        raise NotImplementedError

    def getLocation(self) -> tuple:
        """
        return:the location of this node, if none return null.
        """
        raise NotImplementedError

    def setLocation(self, location: tuple) -> None:
        """
         Allows changing this node's location.
        :param location: new new location  (position) of this node
        :return: void
        """
        raise NotImplementedError

    def getWeight(self) -> float:
        """
        :return:  he weight associated with this node
        """
        raise NotImplementedError

    def setWeight(self, weight: float) -> None:
        """
        Allows changing this node's weight.
        :param weight:the new weight
        :return: void
        """
        raise NotImplementedError

    def getInfo(self) -> str:
        """
        :return:the remark (meta data) associated with this node
        """
        raise NotImplementedError

    def setInfo(self, info: str) -> None:
        """
        Allows changing the remark (meta data) associated with this node
        :param info: new info
        :return: void
        """
        raise NotImplementedError

    def getTag(self) -> int:
        """
        Temporal data (aka color: e,g, white, gray, black)
        Which can be used be algorithms
        :return: dd
        """
        raise NotImplementedError

    def setTag(self, tag: int) -> None:
        """
        Allows setting the "tag" value for temporal marking an node - common
        practice for marking by algorithms.
        param tag:the new value of the tag.
        :return: void
        """
        raise NotImplementedError
