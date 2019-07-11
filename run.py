from src.fp_growth import FpGrowth

if __name__ == '__main__':
    item_sets = []
    with open('data/item_sets', mode='r', encoding='utf-8') as file:
        for line in file:
            item_sets.append(line.strip().split(' '))

    fp = FpGrowth(min_support=3)
    fp.build(item_sets=item_sets)

    frequent_item_sets = fp.find_frequency_item_sets()
    print('-' * 20, 'frequent item sets', '-' * 20)
    for item_set in frequent_item_sets:
        print(item_set)
