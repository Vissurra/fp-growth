from src.fp_growth import FpGrowth

if __name__ == '__main__':
    item_sets = [
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [1, 2, 3, 4, 6],
        [1, 2, 3, 5],
        [1, 2, 3],
        [2],
        [2, 7],
        [2, 7],
        [2, 7],
        [2, 8],
        [2, 3],
        [2, 3],
        [2, 3],
        [2, 3],
        [2, 1],
    ]

    fp = FpGrowth(min_support=3)
    fp.build(item_sets=item_sets)
    frequent_item_sets = fp.find_frequency_item_sets()
    for item_set in frequent_item_sets:
        print(item_set)
