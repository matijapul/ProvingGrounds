import unittest
from permutations import permute


class PermutationsTest(unittest.TestCase):

    def test_permutations_1(self):
        inputList = [1, 2, 3]
        outputList = [
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1]
        ]
        self.assertEqual(permute(inputList), outputList)

    def test_permutations_2(self):
        inputList = [6, 5, 4]
        outputList = [
            [6, 5, 4]
            [6, 4, 5],
            [5, 6, 4],
            [5, 4, 6],
            [4, 6, 5],
            [4, 5, 6],
        ]
        self.assertEqual(permute(inputList), outputList)

if __name__ == "__main__":
    unittest.main()