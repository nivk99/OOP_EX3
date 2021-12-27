import unittest

from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo

graph = DiGraph()

# add the nodes

# key -> 0
graph.add_node(0,[0,0])
# key -> 1
graph.add_node(1,[1,1])
# key -> 2
graph.add_node(2,[2,2])
# key -> 3
graph.add_node(3,[3,3])
# key -> 4
graph.add_node(4,[4,4])

# add the edge

# key -> 0
graph.add_edge(0, 1, 2)
graph.add_edge(0, 4, 3)

# key -> 1
graph.add_edge(1, 0, 3)
graph.add_edge(1, 3, 1)

# key -> 2
graph.add_edge(2, 3, 2)
graph.add_edge(2, 4, 2)

# key -> 3
graph.add_edge(3, 1, 5)
graph.add_edge(3, 2, 4)

# key -> 4
graph.add_edge(4, 0, 5)
graph.add_edge(4, 2, 1)

graph_algo=GraphAlgo(graph)

class MyTestCase(unittest.TestCase):
    # This is a method of testing
    def test_get_graph(self):
        self.assertEqual(graph,graph_algo.get_graph())

    # This is a method of testing
    def test_load_from_json(self):
        self.assertFalse(graph_algo.load_from_json(None))

    # This is a method of testing
    def test_save_to_json(self):
        self.assertTrue(graph_algo.save_to_json("test.json"))
        print(graph_algo.load_from_json("test.json"))

    # This is a method of testing
    def test_shortest_path(self):
        self.assertEqual(3,graph_algo.shortest_path(0,3)[0])

    # This is a method of testing
    def test_TSP(self):
        arr=[0,1,4]
        tsp=graph_algo.TSP(arr)[0]
        tsp_sum=graph_algo.TSP(arr)[1]
        self.assertEqual(6,tsp_sum)
        self.assertEqual(1,tsp[0])
        self.assertEqual(0, tsp[1])
        self.assertEqual(4, tsp[2])

    # This is a method of testing
    def test_centerPoint(self):
       self.assertEqual(0,graph_algo.centerPoint()[0])
       self.assertEqual(4.0, graph_algo.centerPoint()[1])

    # This is a method of testing
    def test_plot_graph(self):
       graph_algo.plot_graph()


if __name__ == '__main__':
    unittest.main()
