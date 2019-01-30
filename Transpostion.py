from DEF import *

class Traspostion:

    Def = DEF()

    def encryption(self, Key, Plain):
        Key_ = Key.replace(" ", "")
        Key_arr = self.Def.split_X(Key_, 1)


        #for remove duplicate >> key
        """
        for z in range(0, len(Key_arr)):
            for b in range(z+1, len(Key_arr)):
                if Key_arr[z] == Key_arr[b]:
                    del Key_arr[b]
        """
        Sorted_Key = self.Def.sort_ascending(Key_arr)

        Plain_ = Plain.replace(" ", "")
        Plain_arr = self.Def.split_X(Plain_, 1)


        print(Sorted_Key)
        print(Key_arr)
        print(Plain_arr)

        len_of_key = len(Key_arr)
        print(len_of_key)
        len_of_Plain = len(Plain_arr)
        print(len_of_Plain)
        ##############

        matrix = [Key_arr]
        for i in range(0, len_of_Plain, len_of_key):
            block = Plain_arr[i:i+len_of_key]
            len_of_block = len(block)
            if len_of_block == len_of_key:
                matrix.append(block)
            else:
                lost_char_len = len_of_key - len_of_block
                for i in range(0, lost_char_len):
                    #alpha = string.ascii_lowercase
                    block.extend(self.Def.alphabetic[i])
                matrix.append(block)

        print(matrix)

        Cipher = ''
        for i in range(0, len(Sorted_Key)):
            for j in range(0, len(matrix[0])):
                if Sorted_Key[i] == matrix[0][j]:
                    for row in range(1, len(matrix)):
                        Cipher += matrix[row][j]

        return Cipher


    def decryption(self, key_, cipher_):

        key_arr = self.Def.split_X(key_, 1)

        # for remove duplicate >> key
        """
        for z in range(0, len(key_arr)):
            for b in range(z+1, len(key_arr)):
                if key_arr[z] == key_arr[b]:
                    del key_arr[b]
        """
        len_block = int(len(cipher_) / len(key_arr))

        sorted_key = self.Def.sort_ascending(key_arr)
        cipher_arr = self.Def.split_X(cipher_, 1)

        matrix = [key_arr]

        matrix = self.Def.initiaize(matrix, len_block, len(key_arr))

        for i in range(0, len(sorted_key)):
            for j in range(0, len(matrix[0])):
                if sorted_key[i] == matrix[0][j]:
                    for m in range(0, len_block):
                        matrix[m + 1][j] = cipher_arr[m]
                    del cipher_arr[0: len_block]
        print(matrix)

        plain = ''
        for row in range(1, len(matrix)):
            for column in range(0, len(matrix[0])):
                plain += matrix[row][column]

        return plain
