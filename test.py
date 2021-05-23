if __name__ == '__main__':
    x = [1, 2, 3];
    y = [1, 2, 3];
    #创建一个没有重复元素当tuple
    print([(xx, yy) for xx in x for yy in y if xx != yy])


    # expected output:
    # [{'name': 'jason', 'dob': '2000-01-01', 'gender': 'male'},
    #  {'name': 'mike', 'dob': '1999-01-01', 'gender': 'male'},
    #  {'name': 'nancy', 'dob': '2001-02-01', 'gender': 'female'}]
    attributes = ['name', 'dob', 'gender']
    values = [['jason', '2000-01-01', 'male'],
              ['mike', '1999-01-01', 'male'],
              ['nancy', '2001-02-01', 'female']
              ]
    result = []
    for x in values:
        p = {}
        result.append(p)
        for i,v in enumerate(attributes):
            p[v] = x[i]
    print(result)
    # 一行搞定
    print([dict(zip(attributes, value)) for value in values])