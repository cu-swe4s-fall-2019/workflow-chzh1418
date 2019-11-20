import unittest
import random
import os
import sys
import get_gene_counts as ggc


class TestGeneCount(unittest.TestCase):
    def test_linear_search(self):
        D = [1, 2, 3, 4, 5]
        A = ggc.linear_search(1, D)
        self.assertEqual(A, 0)
        self.assertNotEqual(A, 1)
        B = ggc.linear_search(0, D)
        self.assertNotEqual(B, 0)
        self.assertEqual(B, -1)


if __name__ == '__main__':
    unittest.main()
