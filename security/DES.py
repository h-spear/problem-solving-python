class Common:
    def __init__(self):
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

    def left_shift(self, binstr: str, shift: int) -> str:
        binstr += binstr[:shift]
        return binstr[shift:]

    def xor(self, binstr1: str, binstr2: str, length: int) -> str:
        result = ""
        for i in range(length):
            if binstr1[i] == binstr2[i]:
                result += "0"
            else:
                result += "1"
        return result


class DES_Table:
    def __init__(self):
        self.initial_permutation = [
            58, 50, 42, 34, 26, 18, 10, 2,
            60, 52, 44, 36, 28, 20, 12, 4,
            62, 54, 46, 38, 30, 22, 14, 6,
            64, 56, 48, 40, 32, 24, 16, 8,
            57, 49, 41, 33, 25, 17, 9,  1,
            59, 51, 43, 35, 27, 19, 11, 3,
            61, 53, 45, 37, 29, 21, 13, 5,
            63, 55, 47, 39, 31, 23, 15, 7,
        ]

        self.initial_permutation_reverse = [
            40, 8, 48, 16, 56, 24, 64, 32,
            39, 7, 47, 15, 55, 23, 63, 31,
            38, 6, 46, 14, 54, 22, 62, 30,
            37, 5, 45, 13, 53, 21, 61, 29,
            36, 4, 44, 12, 52, 20, 60, 28,
            35, 3, 43, 11, 51, 19, 59, 27,
            34, 2, 42, 10, 50, 18, 58, 26,
            33, 1, 41, 9, 49, 17, 57, 25
        ]

        self.key_permutation = [
            57, 49, 41, 33, 25, 17, 9,
            1, 58, 50, 42, 34, 26, 18,
            10, 2, 59, 51, 43, 35, 27,
            19, 11, 3, 60, 52, 44, 36,
            63, 55, 47, 39, 31, 23, 15,
            7, 62, 54, 46, 38, 30, 22,
            14, 6, 61, 53, 45, 37, 29,
            21, 13, 5, 28, 20, 12, 4,
        ]

        self.compression_permutation = [
            14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10,
            23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2,
            41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48,
            44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32,
        ]

        self.expansion_permutation = [
            32, 1, 2, 3, 4, 5,
            4, 5, 6, 7, 8, 9,
            8, 9, 10, 11, 12, 13,
            12, 13, 14, 15, 16, 17,
            16, 17, 18, 19, 20, 21,
            20, 21, 22, 23, 24, 25,
            24, 25, 26, 27, 28, 29,
            28, 29, 30, 31, 32, 1,
        ]

        self.s_box = [
            [
                [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
                [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
                [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
                [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
            ],
            [
                [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
                [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
                [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
                [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
            ],
            [
                [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
                [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
                [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
                [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
            ],
            [
                [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
                [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
                [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
                [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
            ],
            [
                [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
                [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
                [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
                [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
            ],
            [
                [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
                [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
                [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
                [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
            ],
            [
                [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
                [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
                [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
                [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
            ],
            [
                [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
                [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
                [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
                [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
            ],
        ]

        self.p_box = [
            16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10, 2,
            8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25,
        ]

        self.shift_bit_per_round = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]


class DES:
    def __init__(self, plain_text, key):
        self.__plain_text = plain_text
        self.__key = key
        self.__sub_keys_hex = []
        self.__sub_keys = []
        self.common = Common()
        self.tables = DES_Table()

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

    @property
    def sub_keys(self):
        return self.__sub_keys_hex

    def generate_sub_keys(self):
        key_64 = self.common.hex_to_bin(key)
        key_56 = self.permutation(key_64, self.tables.key_permutation, 64, 56)
        sub_keys = []
        sub_keys_hex = []
        L_28, R_28 = key_56[:28], key_56[28:]
        for round in range(16):
            L_28 = self.common.left_shift(L_28, self.tables.shift_bit_per_round[round])
            R_28 = self.common.left_shift(R_28, self.tables.shift_bit_per_round[round])
            temp_56 = L_28 + R_28
            compressed_48 = self.permutation(
                temp_56, self.tables.compression_permutation, 56, 48
            )
            compressed_hex = self.common.bin_to_hex(compressed_48)
            sub_keys.append(compressed_48)
            sub_keys_hex.append(compressed_hex)
        self.__sub_keys = sub_keys
        self.__sub_keys_hex = sub_keys_hex

    def permutation(self, text, table, input_bit, output_bit):
        result = ["0"] * output_bit
        for i in range(output_bit):
            p = table[i]
            result[i] = text[p - 1]
        return "".join(result)

    def substitution(self, text, table, input_bit, output_bit):
        result = ""
        for i in range(8):
            frag_6 = text[i * 6 : i * 6 + 6]
            r = int(frag_6[0] + frag_6[5], 2)
            c = int(frag_6[1:5], 2)
            num = table[i][r][c]

            temp = ""
            while num:
                temp += str(num % 2)
                num //= 2
            result += temp[::-1].zfill(4)
        return result

    def round_function(self, text: str, sub_key) -> str:
        L_32, R_32 = text[:32], text[32:]
        R_48 = self.permutation(R_32, self.tables.expansion_permutation, 32, 48)
        R_48 = self.common.xor(R_48, sub_key, 48)

        temp_32 = self.substitution(R_48, self.tables.s_box, 48, 32)
        temp_32 = self.permutation(temp_32, self.tables.p_box, 32, 32)

        NR_32 = self.common.xor(temp_32, L_32, 32)
        NL_32 = R_32
        return NL_32, NR_32

    def encrypt(self):
        bin_plain_text = self.common.hex_to_bin(self.plain_text)

        bin_text = self.permutation(
            bin_plain_text, self.tables.initial_permutation, 64, 64
        )

        for round in range(16):
            sub_key = self.__sub_keys[round]
            L_32, R_32 = self.round_function(bin_text, sub_key)
            if round == 15:
                L_32, R_32 = R_32, L_32
            bin_text = L_32 + R_32

        cipher_text = self.permutation(
            bin_text, self.tables.initial_permutation_reverse, 64, 64
        )
        cipher_text = self.common.bin_to_hex(cipher_text)
        return cipher_text

    def decrypt(self):
        bin_plain_text = self.common.hex_to_bin(self.plain_text)

        bin_text = self.permutation(
            bin_plain_text, self.tables.initial_permutation, 64, 64
        )

        # use sub key 15, 14, 13, ... , 1
        for round in range(15, -1, -1):
            sub_key = self.__sub_keys[round]
            L_32, R_32 = self.round_function(bin_text, sub_key)
            if round == 0:
                L_32, R_32 = R_32, L_32
            bin_text = L_32 + R_32

        cipher_text = self.permutation(
            bin_text, self.tables.initial_permutation_reverse, 64, 64
        )
        cipher_text = self.common.bin_to_hex(cipher_text)
        return cipher_text


plain_text = "0123456789ABCDEF"
key = "85E813540F0AB405"

des = DES(plain_text, key)
des.generate_sub_keys()

# encrypt
cipher_text = des.encrypt()
print(cipher_text)

# decrypt
des.plain_text = cipher_text
print(des.decrypt())
