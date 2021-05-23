if __name__ == '__main__':
    x = [1, 2, 3];
    y = [1, 2, 3];
    #创建一个没有重复元素当tuple
    print([(xx, yy) for xx in x for yy in y if xx != yy])