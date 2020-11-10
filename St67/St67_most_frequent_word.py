def most_frequent_word():
    import os

    path = os.path.join('.', 'St67_most_frequent_word_input.txt')
    with open(path, 'r') as inf:
        s = [inf.readline().strip().split() for _ in inf]

    print(s)

    
    #with open('St67_most_frequent_word_output.txt', 'w') as ouf:
    #    ouf.write(s_out)

most_frequent_word()