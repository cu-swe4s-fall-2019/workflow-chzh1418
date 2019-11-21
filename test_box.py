import unittest
import os
import sys
import box


class TestBoxPlot(unittest.TestCase):
    def testboxplot(self):
        Array = [[1, 2, 3], [4, 5, 6], [7, 7, 7]]
        title = ['x', 'y', 'z']
        xticks = ['a', 'b', 'c']
        out_file = 'test1.png'
        box.box_plot(Array, title, xticks, out_file)
        self.assertTrue(os.path.exists('test1.png'))
        os.remove('test1.png')


if __name__ == '__main__':
    unittest.main()
