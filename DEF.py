
class DEF:

    alphabetic = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Y'
               , 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


    def split_X(self, word, length):
        chars_ = []

        len_ = len(word)
        for i in range(0, len_, length):
            splited_X = word[i:(i+length)]
            chars_.append(splited_X)

        return chars_


    def sort_ascending (self, word):
        sorting = []
        for i in self.alphabetic:
            for j in word:
                if i == j:
                    sorting.append(j)

        return sorting

    def sort_descending (self, word):
        sorting = []
        for i in reversed(self.alphabetic):
            for j in word:
                if i == j:
                    sorting.append(j)

        return sorting


    def sort_(self, word, reverse):
        sorting = sorted(word, reverse=reverse)

        return sorting

    def initiaize(self, matrix_, row, column):
        for x in range(0, row):
            blocks = []
            for z in range(0, column):
                blocks.extend('0')
            matrix_.append(blocks)

        return matrix_