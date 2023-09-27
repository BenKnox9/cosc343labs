# This is a sample Python script.
import numpy as np


class WordEnc:

    def __init__(self, max_words):
        self.unique_words_list = list()
        self.max_words = max_words

    def fit(self, X):
        # text_file = open("D:/data.txt", "r")
        # data_string = text_file.read()
        # data_list = list(data_string)
        string = X.lower().split()
        data_list = list(string)

        if self.max_words > 0:
            data_list = data_list[0:self.max_words]

        data_set = set(data_list)
        unique_data_list = list(data_set)
        self.unique_words_list = unique_data_list
        print("\nvalues: ", unique_data_list)

        integer_encoded = []
        for i in string:
            v = np.where(np.array(unique_data_list) == i)[0][0]
            integer_encoded.append(v)
        print("\ninteger encoded: ", integer_encoded)

        # text_file.close()
    def get_vec(self, len_doc, word):
        empty_vector = [0] * len_doc
        vect = 0
        find = np.where(np.array(self.unique_words_list) == word)[0][0]
        empty_vector[find] = 1
        return empty_vector

    def transform(self, X):
        mat = []
        len_doc = len(self.unique_words_list)
        docs = X.lower().split()
        for i in docs:
            vec = self.get_vec(len_doc, i)
            mat.append(vec)
        print("\nMATRIX:")
        print(mat)
        return np.asarray(mat)

    def inverse_transform(self, X):
        pass


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
    # print("hi")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
