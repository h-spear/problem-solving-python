from copy import deepcopy


class Common:
    def __init__(self):
        self.hex_to_num_hash = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "A": 10,
            "B": 11,
            "C": 12,
            "D": 13,
            "E": 14,
            "F": 15,
        }

        self.hex_to_bin_hash = {
            "0": "0000",
            "1": "0001",
            "2": "0010",
            "3": "0011",
            "4": "0100",
            "5": "0101",
            "6": "0110",
            "7": "0111",
            "8": "1000",
            "9": "1001",
            "A": "1010",
            "B": "1011",
            "C": "1100",
            "D": "1101",
            "E": "1110",
            "F": "1111",
        }

        self.bin_to_hex_hash = {
            "0000": "0",
            "0001": "1",
            "0010": "2",
            "0011": "3",
            "0100": "4",
            "0101": "5",
            "0110": "6",
            "0111": "7",
            "1000": "8",
            "1001": "9",
            "1010": "A",
            "1011": "B",
            "1100": "C",
            "1101": "D",
            "1110": "E",
            "1111": "F",
        }

    def hex_to_bin(self, hex: str) -> str:
        temp = ""
        for char in hex:
            temp += self.hex_to_bin_hash[char]
        return temp

    def bin_to_hex(self, bin: str) -> str:
        temp = ""
        for i in range(0, len(bin), 4):
            frag = bin[i : i + 4]
            temp += self.bin_to_hex_hash[frag]
        return temp

    def left_shift(self, hexstr: str, shift: int) -> str:
        binstr = self.hex_to_bin(hexstr)
        binstr += "0" * shift
        return self.bin_to_hex(binstr[shift:])

    def xor(self, hexstr1: str, hexstr2: str, bytes: int) -> str:
        result = ""
        binstr1 = self.hex_to_bin(hexstr1)
        binstr2 = self.hex_to_bin(hexstr2)
        bits = bytes * 8
        for i in range(bits):
            if binstr1[i] == binstr2[i]:
                result += "0"
            else:
                result += "1"
        return self.bin_to_hex(result)

    def text_to_matrix(self, text):
        matrix = [[None] * 4 for _ in range(4)]
        idx = 0
        for j in range(4):
            for i in range(4):
                matrix[i][j] = text[idx : idx + 2]
                idx += 2
        return matrix

    def matrix_to_text(self, matrix):
        text = ""
        for j in range(4):
            for i in range(4):
                text += matrix[i][j]
        return text

    def xor_matrix(self, state_matrix, key_matrix):
        result = [[None] * 4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                result[i][j] = self.xor(state_matrix[i][j], key_matrix[i][j], 1)
        return result


class AES_Table:
    def __init__(self):
        self.s_box = [
            ['63', '7C', '77', '7B', 'F2', '6B', '6F', 'C5', '30', '01', '67', '2B', 'FE', 'D7', 'AB', '76'],
            ['CA', '82', 'C9', '7D', 'FA', '59', '47', 'F0', 'AD', 'D4', 'A2', 'AF', '9C', 'A4', '72', 'C0'],
            ['B7', 'FD', '93', '26', '36', '3F', 'F7', 'CC', '34', 'A5', 'E5', 'F1', '71', 'D8', '31', '15'],
            ['04', 'C7', '23', 'C3', '18', '96', '05', '9A', '07', '12', '80', 'E2', 'EB', '27', 'B2', '75'],
            ['09', '83', '2C', '1A', '1B', '6E', '5A', 'A0', '52', '3B', 'D6', 'B3', '29', 'E3', '2F', '84'],
            ['53', 'D1', '00', 'ED', '20', 'FC', 'B1', '5B', '6A', 'CB', 'BE', '39', '4A', '4C', '58', 'CF'],
            ['D0', 'EF', 'AA', 'FB', '43', '4D', '33', '85', '45', 'F9', '02', '7F', '50', '3C', '9F', 'A8'],
            ['51', 'A3', '40', '8F', '92', '9D', '38', 'F5', 'BC', 'B6', 'DA', '21', '10', 'FF', 'F3', 'D2'],
            ['CD', '0C', '13', 'EC', '5F', '97', '44', '17', 'C4', 'A7', '7E', '3D', '64', '5D', '19', '73'],
            ['60', '81', '4F', 'DC', '22', '2A', '90', '88', '46', 'EE', 'B8', '14', 'DE', '5E', '0B', 'DB'],
            ['E0', '32', '3A', '0A', '49', '06', '24', '5C', 'C2', 'D3', 'AC', '62', '91', '95', 'E4', '79'],
            ['E7', 'C8', '37', '6D', '8D', 'D5', '4E', 'A9', '6C', '56', 'F4', 'EA', '65', '7A', 'AE', '08'],
            ['BA', '78', '25', '2E', '1C', 'A6', 'B4', 'C6', 'E8', 'DD', '74', '1F', '4B', 'BD', '8B', '8A'],
            ['70', '3E', 'B5', '66', '48', '03', 'F6', '0E', '61', '35', '57', 'B9', '86', 'C1', '1D', '9E'],
            ['E1', 'F8', '98', '11', '69', 'D9', '8E', '94', '9B', '1E', '87', 'E9', 'CE', '55', '28', 'DF'],
            ['8C', 'A1', '89', '0D', 'BF', 'E6', '42', '68', '41', '99', '2D', '0F', 'B0', '54', 'BB', '16']
        ]

        self.round_constant = [
            "01000000",
            "02000000",
            "04000000",
            "08000000",
            "10000000",
            "20000000",
            "40000000",
            "80000000",
            "1B000000",
            "36000000",
        ]

        self.mix_columns_transformation = [
            [2, 3, 1, 1],
            [1, 2, 3, 1],
            [1, 1, 2, 3],
            [3, 1, 1, 2],
        ]

        self.inverse_mix_columns_transformation = [
            [14, 11, 13, 9],
            [9, 14, 11, 13],
            [13, 9, 14, 11],
            [11, 13, 9, 14],
        ]


class AES:
    def __init__(self, plain_text, key):
        self.__plain_text = plain_text
        self.__key = key
        self.__sub_keys = []
        self.common = Common()
        self.tables = AES_Table()

    @property
    def plain_text(self):
        return self.__plain_text

    @plain_text.setter
    def plain_text(self, plain_text):
        self.__plain_text = plain_text

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key):
        self.__key = key

    def create_matrix(self, hexstr, bytes):
        r = 4
        c = bytes // 4
        matrix = [[None] * c for _ in range(r)]
        idx = 0
        for j in range(c):
            for i in range(r):
                matrix[i][j] = hexstr[idx : idx + 2]
                idx += 2

        return matrix

    def rotate_word(self, word):
        return (word + word[:2])[2:]

    def substitution_word(self, word):
        result = ""
        for i in [0, 2, 4, 6]:
            r = self.common.hex_to_num_hash[word[i]]
            c = self.common.hex_to_num_hash[word[i + 1]]
            result += self.tables.s_box[r][c]
        return result

    def key_expansion(self):
        w = []
        for i in range(4):
            w.append(self.__key[8 * i : 8 * i + 8])

        for i in range(4, 44):
            if i % 4 == 0:
                temp = w[i - 1]
                rot_word = self.rotate_word(temp)
                sub_word = self.substitution_word(rot_word)
                rcon = self.tables.round_constant[i // 4 - 1]
                xor_with_rcon = self.common.xor(rcon, sub_word, 4)
                result = self.common.xor(xor_with_rcon, w[i - 4], 4)
                w.append(result)
            else:
                w.append(self.common.xor(w[i - 1], w[i - 4], 4))

        temp_sub_keys = []
        for i in range(11):
            sub_key = w[i * 4] + w[i * 4 + 1] + w[i * 4 + 2] + w[i * 4 + 3]
            temp_sub_keys.append(sub_key)
        self.__sub_keys = temp_sub_keys

    def byte_substitution(self, matrix):
        r = len(matrix)
        c = len(matrix[0])
        for i in range(r):
            for j in range(c):
                left, right = matrix[i][j]
                left = self.common.hex_to_num_hash[left]
                right = self.common.hex_to_num_hash[right]
                matrix[i][j] = self.tables.s_box[left][right]

    def shift_rows(self, matrix):
        r = len(matrix)
        for i in range(r):
            for _ in range(i):
                matrix[i].append(matrix[i].pop(0))

    def inverse_shift_rows(self, matrix):
        r = len(matrix)
        for i in range(r):
            for _ in range(i):
                matrix[i].insert(0, matrix[i].pop())

    def mix_columns(self, matrix):
        trans_matrix = self.tables.mix_columns_transformation
        copied = deepcopy(matrix)
        for i in range(4):
            for j in range(4):
                temp = "00"
                for k in range(4):
                    x = copied[k][j]
                    x_multiple_2 = self.common.left_shift(x, 1)
                    if self.common.hex_to_bin(x[0])[0] == "1":
                        x_multiple_2 = self.common.xor(x_multiple_2, "1B", 1)

                    if trans_matrix[i][k] == 1:
                        temp = self.common.xor(temp, x, 1)
                    elif trans_matrix[i][k] == 2:
                        temp = self.common.xor(temp, x_multiple_2, 1)
                    elif trans_matrix[i][k] == 3:
                        x_multiple_3 = self.common.xor(x_multiple_2, x, 1)
                        temp = self.common.xor(temp, x_multiple_3, 1)

                matrix[i][j] = temp

    def add_round_key(self, state_matrix, key_matrix):
        return self.common.xor_matrix(state_matrix, key_matrix)

    def encrypt(self):
        state_matrix = self.common.text_to_matrix(self.__plain_text)
        key_matrix = self.common.text_to_matrix(self.__sub_keys[0])

        state_matrix = self.common.xor_matrix(state_matrix, key_matrix)

        for round in range(1, 11):
            print(
                "---------------------- Round {:02d} ----------------------".format(
                    round
                )
            )
            self.byte_substitution(state_matrix)
            print("After SubBytes:   ", self.common.matrix_to_text(state_matrix))
            self.shift_rows(state_matrix)
            print("After ShiftRows:  ", self.common.matrix_to_text(state_matrix))

            if round != 10:
                self.mix_columns(state_matrix)
                print("After MixColumns: ", self.common.matrix_to_text(state_matrix))

            key_matrix = self.common.text_to_matrix(self.__sub_keys[round])
            state_matrix = self.add_round_key(state_matrix, key_matrix)
            print("After AddRoundKey:", self.common.matrix_to_text(state_matrix))
            print()

        return self.common.matrix_to_text(state_matrix)

    def decrypt(self):
        pass


#plain_text = "0123456789ABCDEFFEDCBA9876543210"
#key = "0F1571C947D9E8590CB7ADD6AF7F6798"
plain_text = "54776F204F6E65204E696E652054776F"
key = "5468617473206D79204B756E67204675"

aes = AES(plain_text, key)
aes.key_expansion()

# encrypt
cipher_text = aes.encrypt()
print(cipher_text)
