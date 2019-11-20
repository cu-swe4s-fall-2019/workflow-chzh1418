import unittest
import os
import sys
import get_tissue_samples as gts


class TestParser(unittest.TestCase):
    def test_parser(self):
        A = gts.parse_args()
        self.assertNotEqual(A.attribute_file, 'file_name')
        self.assertNotEqual(A.tissue_group, 'whatever')
        self.assertNotEqual(A.out_file, 'Anthing')


if __name__ == '__main__':
    unittest.main()
