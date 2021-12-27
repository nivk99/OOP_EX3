import json
import math
from typing import List

from matplotlib.cbook import Stack

from src import GraphInterface
from src.DiGraph import DiGraph
from src.GraphAlgoInterface import GraphAlgoInterface
import matplotlib.pyplot as plt
import numpy as np
from queue import PriorityQueue

from src.NodeData import NodeData
from src.Node_Data import Node_Data


class GraphAlgo(GraphAlgoInterface):
    """
In this class you can find methods that work on the graph. In this class you can see a number of different algorithms that help this class.
    """

    def __init__(self, diGraph: GraphInterface = DiGraph()):
        """
           constructor
        :param diGraph: GraphInterface
        """
        self._diGraph = diGraph

    def get_graph(self) -> GraphInterface:
        """
        :return: This method returns the underlying graph of which this class works
        """
        return self._diGraph

    def load_from_json(self, file_name: str) -> bool:
        """
           * This method loads a graph to this graph algorithm.
        * if the file was successfully loaded - the underlying graph
        *of this class will be changed (to the loaded one), in case the
       * graph was not loaded the original graph should remain "as is".
        :param dict: - file name of JSON file
        :return:Whether  loaded or not
        """
        if file_name is None:
            return False
        self._diGraph = DiGraph()
        try:
            with open(file_name, 'r') as file:
                load_json = json.load(file, object_hook=self._load_node)
            for edge in load_json.get("Edges"):
                self._diGraph.add_edge(id1=edge["src"], id2=edge["dest"], weight=edge["w"])
            return True
        except Exception as e:
            print(e)
            return False
        return True

    def _load_node(selt, dict):
        """
This is a method that helps read the file by object_hook
        """
        if "pos" in dict:
            return selt._diGraph.add_node(node_id=dict["id"], pos=dict["pos"])
        if "id" in dict:
            return selt._diGraph.add_node(node_id=dict["id"], pos=None)
        return dict

    def save_to_json(self, file_name: str) -> bool:
        """
         * The function saves the graph
        *The idea for the code was taken from the Internet
        :param file_name:  the file name (may include a relative path).
        :return:Whether saved or not
        """
        try:
            with open(file_name, 'w') as file:
                e = []
                n = []
                for k, v in self._diGraph.get_all_v().items():
                    if v._node_location is None:
                        n.append({"id": k})
                    else:
                        n.append({"id": k, "pos": v._node_location})
                    for d, w in self._diGraph.all_out_edges_of_node(k).items():
                        e.append({"src": k, "w": w, "dest": d})
                dic = {"Edges": e, "Nodes": n}
                json.dump(dic, default=lambda m: m.__dict__, indent=4, fp=file)
            return True
        except IOError as e:
            print(e)
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        * This method computes the the shortest path between src to dest - as an ordered List of nodes:
        * src--> n1-->n2-->...dest
        * if no such path --> returns null;
        *  src - start node
        *  dest - end (target) node
        * Method uses Dijkstra's algorithm The explanation of the algorithm can be seen on
        * https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
        :param id1:src  - start node
        :param id2:dest - end (target) nod
        :return: list
        """
        if self._diGraph.v_size() == 0 or self._diGraph.e_size() == 0 or id1 not in self._diGraph.get_all_v().keys() or id2 not in self._diGraph.get_all_v().keys():
            return float('inf'), []
        if id1 == id2:
            return 0, id1
        ans = []
        min_heap: Node_Data = PriorityQueue()
        src_node: Node_Data = self._diGraph.get_all_v()[id1]
        dest_node: Node_Data = self._diGraph.get_all_v()[id2]
        for n in self._diGraph.get_all_v().values():
            n.setWeight(float('inf'))
            n.setTag(0)

        src_node.setWeight(0)
        min_heap.put(src_node.getKey())
        while not min_heap.empty():
            node_pq: Node_Data = self._diGraph.get_all_v()[min_heap.get()]
            for v in self._diGraph.all_out_edges_of_node(node_pq.getKey()).keys():
                node_dest: Node_Data = self._diGraph.get_all_v()[v]
                weight: float = node_pq.getWeight() + self._diGraph.all_out_edges_of_node(node_pq.getKey())[v]
                if float(node_dest.getWeight()) > float(weight):
                    node_dest._node_weight = weight
                    node_dest._node_tag = node_pq.getKey()
                    min_heap.put(node_dest.getKey())

        st = Stack()
        st.push(dest_node)
        sum: float = 0;
        while dest_node is not src_node:
            dest = dest_node
            dest_node = self._diGraph.get_all_v()[dest_node.getTag()]
            st.push(dest_node)
            try:
                sum += self._diGraph.all_out_edges_of_node(dest_node.getKey())[dest.getKey()]
            except Exception:
                return float('inf'), []

        while not st.empty():
            ans.append(st.forward().getKey())
            st.remove(st.forward())

        return sum, ans

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        """
        * This method Computes a list of consecutive nodes which go over all the nodes in cities.
        *  the sum of the weights of all the consecutive (pairs) of nodes (directed) is the "cost" of the solution .
         * The function checks for each vertex where it is best to go. This is a greedy method
        :param node_lst: list  key nods
        :return: list nods and sum
        """
        ans = []
        arr = []
        for v in node_lst:
            temp = []
            temp.append(v)
            ans.append(temp)

        for i in range(len(node_lst)):
            list_cities = [k for k in node_lst]
            id = list_cities[i]
            list_cities.remove(id)
            total: float = 0
            for j1 in range(len(list_cities)):
                sort: float = float('inf')
                kay: int = list_cities[0]
                remov = kay
                for j2 in list_cities:
                    w: float = float(self.shortest_path(id, j2)[0])
                    if sort > w:
                        sort = w
                        remov = j2
                ans[i].append(remov)
                total += sort
                id = remov
                if remov not in list_cities:
                    break
                list_cities.remove(remov)
            k = node_lst[i]
            g = self._diGraph.get_all_v()[k]
            g.setInfo(total)
            arr.append(g)

        ind = 0
        w = float('inf')
        j = -1
        for k1 in arr:
            j += 1
            t = float(k1.getInfo())
            if w > t:
                w = t
                ind = j

        return ans[ind], w

    def __isConnected(self) -> bool:
        """
      *This method Returns true if and only if there is a valid path from each node to each.
        *The method goes over the whole graph The Depth-first search method and marks each vertex when visiting it.
        *It then checks for all the vertebrae whether they have been visited. If not then returns false.
       * Plus it does the process again but on the reverse graph. And also there checks for each vertex whether mud has been visited
        :return: is connected or not
        """

        for v in self._diGraph.get_all_v().values():
            v.setInfo("False")

        self.__explore(self._diGraph.get_all_v()[0])
        for v in self._diGraph.get_all_v().values():
            if v.getInfo().__eq__("False"):
                return False

        for v in self._diGraph.get_all_v().values():
            v.setInfo("False")
        self.__explore_back(self._diGraph.get_all_v()[0])
        for v in self._diGraph.get_all_v().values():
            if v.getInfo().__eq__("False"):
                return False
        return True

    # The function marks the vertex where it was

    def __explore(self, v: NodeData) -> None:
        st = Stack()
        st.push(v)
        while not st.empty():
            nod: NodeData = st.forward()
            st.remove(st.forward())
            nod._node_info = "True"
            nod.setTag("True")
            for e in self._diGraph.all_out_edges_of_node(nod.getKey()):
                if self._diGraph.get_all_v()[e].getInfo().__eq__("False"):
                    st.push(self._diGraph.get_all_v()[e])

    #The function marks the vertex where it was according to the inverse graph

    def __explore_back(self, v: NodeData) -> None:
        st = Stack()
        st.push(v)
        while not st.empty():
            nod: NodeData = st.forward()
            st.remove(st.forward())
            nod._node_info = "True"
            for e in self._diGraph.all_in_edges_of_node(nod.getKey()):
                if self._diGraph.get_all_v()[e].getInfo().__eq__("False"):
                    st.push(self._diGraph.get_all_v()[e])

    def centerPoint(self) -> (int, float):
        """
       * This method Finds the NodeData which minimizes the max distance to all the other nodes.
       * return the Node data to which the max shortest path to all the other nodes is minimized.
       * The method goes through each and every vertex and checks which distance is the shortest
        """
        if not self.__isConnected():
            return -1, float('inf')
        ans = 0
        min_w = float('inf')
        for v1 in self._diGraph.get_all_v().keys():
            temp = 0;
            for v2 in self._diGraph.get_all_v().keys():
                if temp > min_w:
                    break;
                sum = self.shortest_path(v1, v2)[0]
                if temp < sum:
                    temp = sum
            if min_w > temp:
                min_w = temp
                ans = v1
        return ans, float(min_w)

    def plot_graph(self) -> None:
        """
        This is a method that draws the graph
        :return:
        """

        # Draws the vertices
        decs = {}
        for key in self._diGraph.get_all_v().keys():
            typ = self._diGraph.get_all_v()[key].getLocation()
            if isinstance(typ, str):
                typ = typ.split(',')
                typ = tuple(typ)
            decs[key] = typ
            xpoints = np.array([float(typ[0])])
            ypoints = np.array([float(typ[1])])
            plt.plot(xpoints, ypoints, color='b', marker='o', markersize=7)
            plt.text(xpoints + 0.20, ypoints + 0.20, key, fontsize=1, color='g')

        #  Draws the edges

        for key_src in self._diGraph.get_all_v().keys():
            for key_dest in self._diGraph.all_out_edges_of_node(key_src).keys():
                typ_src = decs[key_src]
                typ_dest = decs[key_dest]
                src_points = np.array([float(typ_src[0]), float(typ_src[1])])
                dest_points = np.array([float(typ_dest[0]), float(typ_dest[1])])
                weight = math.dist(src_points, dest_points)
                head_width = 0.01 * weight * 5
                width = 0.001
                #Adapter by location
                if weight < 1:
                    head_width = 0.0005
                    width = 0.00005
                head_length = head_width
                plt.arrow(float(typ_src[0]), float(typ_src[1]), float(typ_dest[0]) - float(typ_src[0]),
                          float(typ_dest[1]) - float(typ_src[1]),
                          lw=0.7, length_includes_head=True, shape='full', head_width=head_width,
                          head_length=head_length,
                          width=width)
        plt.show()


