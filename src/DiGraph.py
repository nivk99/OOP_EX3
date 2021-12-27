import json

from src.GraphInterface import GraphInterface
from src.Node_Data import Node_Data


class DiGraph(GraphInterface):
    """
This is the class where the graph is kept
The fields of the class are:
A dictionary of all sides with id key and value is the vertex.
A dictionary of all the ribs entering the vertex with weight.
Dictionary of all sides coming out of vertex with weight.
mc - says all changes were.
size -Says what amount of edges
    """

    def __init__(self):
        """
           constructor
        """
        self._dict_node = {}
        self._dict_inDegree = {}
        self._dict_outDegree = {}
        self._mc = 0
        self._size = 0

    def v_size(self) -> int:
        """
         *Number of nodes
        :return: Number of nodes
        """
        return len(self._dict_node)

    def e_size(self) -> int:
        """
        *Number of edge.
        * Both incoming and outgoing
        """
        return self._size

    def get_mc(self) -> int:
        """
        :return: how many times the graph has changed
        """
        return self._mc

    def get_all_v(self) -> dict:
        """
        The method return a dictionary of all the nodes in the Graph, each node is represented using a pair (node_id, node_data)
        :return:
        """
        return self._dict_node

    def all_in_edges_of_node(self, id1: int) -> dict:
        """
        The method return a dictionary of all the nodes connected to (into) node_id , each node is represented using a pair (other_node_id, weight)
        :param id1:
        :return:
        """
        if id1 in self._dict_node:
            return self._dict_inDegree.get(id1)

    def all_out_edges_of_node(self, id1: int) -> dict:
        """
        The method return a dictionary of all the nodes connected from node_id , each node is represented using a pair (other_node_id, weight)
        :param id1:
        :return:
        """
        if id1 in self._dict_node:
            return self._dict_outDegree.get(id1)

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
     *This method  Connects an edge with weight w between node src to node dest.
     * A method that examines all the options for adding an edge
        :param id1:src - the source of the edge.
        :param id2:the destination of the edge.
        :param weight:positive weight representing the cost (aka time, price, etc) between src-->dest.
        :return: boll
        """
        if id1 == id2 or self.v_size() <= 1:
            return False
        src = int(id1)
        dest = int(id2)
        if src not in self._dict_node.keys() or dest not in self._dict_node.keys():
            return False

        if dest in self._dict_outDegree.get(src):

            if self._dict_outDegree[src][dest] == weight:
                return False
            # {key,val}
            # {key,{key,val}}
            # {id src,{id dest,w}}
            # src -(w)->dest
            # {0:p0,1:p1,2:p2}//3 nodes;
            self._dict_outDegree[src][dest] = weight
            self._dict_inDegree[dest][src] = weight
            self._mc = self._mc + 1
            return True

        self._dict_outDegree[src][dest] = weight
        self._dict_inDegree[dest][src] = weight
        self._size += 1
        self._mc += 1
        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
        * This method adds a new node to the graph with the given node_data.
        * The method checks if such a vertex does not exist. If it exists it just adds nothin
        * @param n What a vertex to insert
        :param node_id:
        :param pos: location
        :return:
        """
        node = int(node_id)
        if node in self._dict_node.keys():
            return False
        self._dict_inDegree[node] = {}
        self._dict_outDegree[node] = {}
        self._dict_node[node] = Node_Data(key=node, location=pos,  inDegree=self._dict_inDegree[node],outDegree=self._dict_outDegree[node])
        self._mc += 1
        return True

    def remove_node(self, node_id: int) -> bool:
        """
        * The method deletes the node (with the given ID) from the graph -
       *  and removes all edges which starts or ends at this node.
        * Time O (k), V.degree = k
        *  return the data of the removed node (null if none).
       *  key -  Vertex ID number
       * The method goes over all the ranks of the vertices and deletes them
        :param node_id:Vertex ID number
        :return: true or false
        """

        if self.v_size() == 0:
            return False

        node = int(node_id)
        if node not in self._dict_node.keys():
            return False
        remove_outDegree = self._dict_outDegree[node].keys()
        for key in list(remove_outDegree):
            self._dict_outDegree[node].pop(key)
            self._dict_inDegree[key].pop(node)
            self._size -= 1
            self._mc += 1

        self._dict_outDegree.pop(node)

        remove_inDegree = self._dict_inDegree[node].keys()
        for key in list(remove_inDegree):
            self._dict_outDegree[key].pop(node)
            self._dict_inDegree[node].pop(key)
            self._size -= 1
            self._mc += 1

        self._dict_inDegree.pop(node)

        self._dict_node.pop(node)
        self._mc += 1
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
         *This method checks that it exists and then deletes it from the hash table.
        * Also updates size and mc
        :param node_id1:src The source of the vertex
        :param node_id2: dest Vertex target
        :return: The deleted edge
        """
        if node_id1 == node_id2 or self.v_size() <= 1:
            return False
        src = int(node_id1)
        dest = int(node_id2)
        if src not in self._dict_node.keys() or dest not in self._dict_node.keys():
            return False
        self._dict_outDegree[src].pop(dest)
        self._dict_inDegree[dest].pop(src)
        self._size -= 1
        self._mc += 1
        return True


    def __repr__(self) -> str:
        """
         A string of the whole class
        :return:
        """
        return f"Graph: |V|={self.v_size()} , |E|={self.e_size()}"



