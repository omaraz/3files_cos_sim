from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from math import sqrt


def read_file(filename):
    try:
        with open(filename, 'r') as f:
            data = f.read()
        return data

    except IOError:
        print("Error opening or reading input file: ", filename)
        sys.exit()




def cos_sim(X,Y):
    X_list = word_tokenize(X)
    Y_list = word_tokenize(Y)

    sw = stopwords.words('english')
    # print(sw)
    l1 = [];
    l2 = []

    X_set = {w for w in X_list if not w in sw}
    Y_set = {w for w in Y_list if not w in sw}

    rvector = X_set.union(Y_set)
    for w in rvector:
        if w in X_set:
            l1.append(1)
        else:
            l1.append(0)
        if w in Y_set:
            l2.append(1)
        else:
            l2.append(0)
    c = 0

    for i in range(len(rvector)):
        c += l1[i] * l2[i]
    cosine = c / float(sqrt(sum(l1) * sum(l2)))
    #print("Cosine similarity:", "% 0.4f" % cosine)
    return "% 0.4f" % cosine

def mul_cos_sim(file_1,file_2,file_3):
    a=[]
    a.append([cos_sim(file_1,file_1),cos_sim(file_1,file_2),cos_sim(file_1, file_3)])
    a.append([cos_sim(file_2, file_1),cos_sim(file_2, file_2),cos_sim(file_2, file_3)])
    a.append([cos_sim(file_3, file_1),cos_sim(file_3, file_2),cos_sim(file_3, file_3)])
    for i in range(len(a)):
        print(a[i])


