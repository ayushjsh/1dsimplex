import onedsimplex


def main():
    stc = onedsimplex.StockCutting("datafile")
    stc.initial_patterns()

if __name__ == '__main__':
    main()