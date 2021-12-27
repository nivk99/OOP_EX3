import unittest

from src.DiGraph import DiGraph

graph = DiGraph()

# add the nodes

# key -> 0
graph.add_node(0)
# key -> 1
graph.add_node(1)
# key -> 2
graph.add_node(2)
# key -> 3
graph.add_node(3)
# key -> 4
graph.add_node(4)

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


class MyTestCase(unittest.TestCase):
    # This is a method of testing
    def test_v_size(self) -> Exception:
        self.assertEqual(5, graph.v_size())

    # This is a method of testing
    def test_e_size(self) -> Exception:
        self.assertEqual(10, graph.e_size())

    # This is a method of testing
    def test_get_mc(self) -> Exception:
        self.assertEqual(19, graph.get_mc())

    # This is a method of testing
    def test_get_all_v(self) -> Exception:
        i = -1
        for v in graph.get_all_v().keys():
            i = i + 1
            self.assertEqual(i, v)

    # This is a method of testing
    def test_all_in_edges_of_node(self) -> Exception:
        i = 1
        for v_in in graph.all_in_edges_of_node(0):
            self.assertEqual(i, v_in)
            i = 4
        i = 0
        for v_out in graph.all_in_edges_of_node(1):
            self.assertEqual(i, v_out)
            i = 3

    # This is a method of testing
    def test_all_out_edges_of_node(self) -> Exception:
        i = 1
        for v_out in graph.all_out_edges_of_node(0):
            self.assertEqual(i, v_out)
            i = 4
        i = 0
        for v_out in graph.all_out_edges_of_node(1):
            self.assertEqual(i, v_out)
            i = 3

    # This is a method of testing
    def test_add_edge(self) -> Exception:
        self.assertEqual(10, graph.e_size())
        graph.add_edge(0, 3, 5)
        self.assertEqual(11, graph.e_size())
        graph.remove_edge(0, 3)

    # This is a method of testing
    def test_add_node(self) -> Exception:
        self.assertEqual(5, graph.v_size())
        graph.add_node(5)
        self.assertEqual(6, graph.v_size())
        graph.remove_node(5)

    # This is a method of testing
    def test_remove_node(self) -> Exception:
        self.assertEqual(5, graph.v_size())
        graph.add_node(5)
        self.assertEqual(6, graph.v_size())
        graph.remove_node(5)

    # This is a method of testing
    def test_remove_edge(self) -> Exception:
        self.assertEqual(10, graph.e_size())
        graph.add_edge(0, 3, 5)
        self.assertEqual(11, graph.e_size())
        graph.remove_edge(0, 3)


if __name__ == '__main__':
    unittest.main()
