import numpy as np


def _initial_feasibility(demands, pattern, availability):
    """
    Checks if the initial basis matrix is feasible or not.
    :param demands:
    :param pattern:
    :param availability:
    :return:
    """
    usage = 0
    for item, demand in zip(pattern, demands):
        usage += demand//item
    if usage < availability:
        return True
    else:
        return False


def initial_basis(sc_object):
    """
    Creates the initial basis to be used by the Simplex method. If the basis does not meet the feasibility demand
    then an artificial basis is generated.

    :return:
    """
    pattern = []
    initstock = max(sc_object.stock_length)
    initstocknum = sc_object.stock_num[np.argmax(sc_object.stock_length)]

    for order, demand in zip(sc_object.order_length, sc_object.order_num):
        activity = initstock // order
        pattern.append(min(activity, demand))

    print(pattern)

    order_types = len(sc_object.order_length)
    stock_type = len(sc_object.stock_length)

    B = np.diagflat(pattern)
    print(B)

    kcol = np.zeros(stock_type)[np.newaxis].T
    kcol[0] = 1
    #print(kcol)

    bot_left = kcol
    for ktimes in range(order_types - 1):
        bot_left = np.concatenate((kcol, bot_left), axis=1)

    print(bot_left)

    left_matrix = np.concatenate((B, bot_left), axis=0)


    top_right =  np.zeros((order_types, stock_type))

    print(top_right)

    if _initial_feasibility(sc_object.order_length, pattern, initstocknum):
        temp = np.ones((1,stock_type))
        bot_right = np.diagflat(temp)#fix_basis(self)
        right_matrix = np.concatenate((top_right,bot_right), axis=0)
    else:
        temp = np.ones((1, stock_type))
        temp[0,0] = -1
        print(temp)
        bot_right = np.diagflat(temp)
        right_matrix = np.concatenate((top_right, bot_right), axis=0)

    final_matrix = np.concatenate((left_matrix,right_matrix), axis=1)
    print(final_matrix)


def findapattern():
    pass