import unittest

from src.Node_Data import Node_Data


class MyTestCase(unittest.TestCase):
    # This is a method of testing
    def test_getKey(self) -> Exception:
        v1 = Node_Data(0)
        v2 = Node_Data(1)
        v3 = Node_Data(2)
        self.assertEqual(0, v1.getKey())
        self.assertEqual(1, v2.getKey())
        self.assertEqual(2, v3.getKey())

    # This is a method of testing
    def test_getLocation(self) -> Exception:
        v1 = Node_Data(0, (0, 0, 0))
        v2 = Node_Data(1, (1, 1, 1))
        v3 = Node_Data(2, (2, 2, 2))
        self.assertEqual(0, v1.getLocation()[0])
        self.assertEqual(1, v2.getLocation()[1])
        self.assertEqual(2, v3.getLocation()[2])

    # This is a method of testing
    def test_setLocation(self) -> Exception:
        v1 = Node_Data(0, (0, 0, 0))
        v2 = Node_Data(1, (1, 1, 1))
        v3 = Node_Data(2, (2, 2, 2))
        v1.setLocation((5.1, 5.1, 5.1))
        v2.setLocation((1.1, 1.1, 1.1))
        v3.setLocation((2.1, 2.1, 2.1))
        self.assertEqual(5.1, v1.getLocation()[0])
        self.assertEqual(1.1, v2.getLocation()[1])
        self.assertEqual(2.1, v3.getLocation()[2])

    # This is a method of testing
    def test_getWeight(self) -> Exception:
        v1 = Node_Data(0, (0, 0, 0))
        v2 = Node_Data(1, (1, 1, 1))
        v3 = Node_Data(2, (2, 2, 2))
        v1.setWeight(1)
        v2.setWeight(2)
        v3.setWeight(3)
        self.assertEqual(1, v1.getWeight())
        self.assertEqual(2, v2.getWeight())
        self.assertEqual(3, v3.getWeight())

    # This is a method of testing
    def test_setWeight(self) -> Exception:
        v1 = Node_Data(0, (0, 0, 0))
        v2 = Node_Data(1, (1, 1, 1))
        v3 = Node_Data(2, (2, 2, 2))
        self.assertEqual(0.0, v1.getWeight())
        self.assertEqual(0.0, v2.getWeight())
        self.assertEqual(0.0, v3.getWeight())
        v1.setWeight(1)
        v2.setWeight(2)
        v3.setWeight(3)
        self.assertEqual(1, v1.getWeight())
        self.assertEqual(2, v2.getWeight())
        self.assertEqual(3, v3.getWeight())

    # This is a method of testing
    def test_getInfo(self) -> Exception:
        v1 = Node_Data(0, (0, 0, 0))
        v2 = Node_Data(1, (1, 1, 1))
        v3 = Node_Data(2, (2, 2, 2))
        v1.setInfo("v1")
        v2.setInfo("v2")
        v3.setInfo("v3")
        self.assertEqual("v1", v1.getInfo())
        self.assertEqual("v2", v2.getInfo())
        self.assertEqual("v3", v3.getInfo())

    # This is a method of testing
    def test_setInfo(self) -> Exception:
        v1 = Node_Data(0, (0, 0, 0))
        v2 = Node_Data(1, (1, 1, 1))
        v3 = Node_Data(2, (2, 2, 2))
        v1.setInfo("v11")
        v2.setInfo("v22")
        v3.setInfo("v33")
        self.assertEqual("v11", v1.getInfo())
        self.assertEqual("v22", v2.getInfo())
        self.assertEqual("v33", v3.getInfo())

    # This is a method of testing
    def test_getTag(self) -> Exception:
        v1 = Node_Data(0, (0, 0, 0))
        v2 = Node_Data(1, (1, 1, 1))
        v3 = Node_Data(2, (2, 2, 2))
        v1.setTag(0)
        v2.setTag(1)
        v3.setTag(2)
        self.assertEqual(0, v1.getTag())
        self.assertEqual(1, v2.getTag())
        self.assertEqual(2, v3.getTag())

    # This is a method of testing
    def test_setTag(self) -> Exception:
        v1 = Node_Data(0, (0, 0, 0))
        v2 = Node_Data(1, (1, 1, 1))
        v3 = Node_Data(2, (2, 2, 2))
        v1.setTag(10)
        v2.setTag(11)
        v3.setTag(12)
        self.assertEqual(10, v1.getTag())
        self.assertEqual(11, v2.getTag())
        self.assertEqual(12, v3.getTag())


if __name__ == '__main__':
    unittest.main()
