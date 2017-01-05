import simplex

import numpy as np


class StockCutting(object):
    """
    Implementation of 1D stock cutting with multiple stock lengths with limited availability.
    """

    def __init__(self, filename):
        """
        Initialise the problem data
        :return:
        """

        self.stock_length = None
        self.stock_num = None
        self.order_length = None
        self.order_num = None
        self.total_order_pieces = None
        self.read_data(filename)

    def read_data(self, filename):

        """

        :param filename:
        :return:
        """

        datafile = open(filename, 'r')
        problem_data = datafile.readlines()
        # possibly use pattern matching
        self.stock_length = np.asarray(list(map(int,(problem_data[0].rstrip('\n')[problem_data[0].find(':') + 1:].split(',')))))
        self.stock_num = np.asarray(list(map(int,(problem_data[1].rstrip('\n')[problem_data[1].find(':') + 1:].split(',')))))
        self.order_length = np.asarray(list(map(int,(problem_data[2].rstrip('\n')[problem_data[2].find(':') + 1:].split(',')))))
        self.order_num = np.asarray(list(map(int,(problem_data[3].rstrip('\n')[problem_data[3].find(':') + 1:].split(',')))))
        self.total_order_pieces = np.sum(self.order_num)
        print(self.total_order_pieces)


sc = StockCutting("datafile")

simplex.initial_basis(sc)