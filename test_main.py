import unittest
from main import dijkstra, calculate_toll, create_graph

class TestDijkstra(unittest.TestCase):
    def test_dijkstra(self):
        G = create_graph()

        expected_paths = [
            ['Mumbai', 'Bangalore', 'Chennai', 'Kanpur', 'Nagpur', 'Bhopal'],
            ['Mumbai', 'Delhi', 'Chennai', 'Kanpur', 'Nagpur', 'Bhopal'],
            ['Mumbai', 'Ahmedabad', 'Chennai', 'Kolkata', 'Pune', 'Bhopal']
        ]
        expected_cost = 17  

        path, cost = dijkstra(G, 'Mumbai', 'Bhopal')

        self.assertEqual(cost, expected_cost, f"Expected cost: {expected_cost}, but got: {cost}")

        self.assertIn(path, expected_paths, f"Expected path to be one of {expected_paths}, but got: {path}")

        toll = calculate_toll(path, G)
        expected_toll = expected_cost * 0.5  
        self.assertEqual(toll, expected_toll, f"Expected toll: {expected_toll}, but got: {toll}")

if __name__ == '__main__':
    unittest.main()
