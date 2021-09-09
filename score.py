def get_score(fix_name, index):
    score={
        'char_change':
            {0:5,
             1:4,
             2:3,
             3:2,
             'else':1},
        'char_remove':
            {0: 10,
             1: 8,
             2: 6,
             3: 4,
             'else': 2},
        'char_add':
            {0: 10,
             1: 8,
             2: 6,
             3: 4,
             'else': 2},
    }
    if index<4:
        return score[fix_name][index]
    else:
        return score[fix_name]['else']
    
