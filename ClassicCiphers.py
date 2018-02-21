# Decipher the following message ciphered with two diffent
# classic algorithms

class ClassicCiphers:

    def __init__(self, alphabet: str):
        self.alphabet = alphabet

    def caesar(self, message: str, key: int) -> str:
        ciphered = []
        for char in message.lower():
            if char.isalpha():
                ciphered.append(
                    self.alphabet[(self.alphabet.index(char) + key) % len(self.alphabet)])
            elif char.isspace():
                ciphered.append(char)
        return ''.join(ciphered)

    def affine(self, message: str, key: (int, int)) -> str:
        ciphered = []
        for char in message.lower():
            if char.isalpha():
                ciphered.append(self.alphabet[((self.alphabet.index(
                    char) * key[0]) + key[1]) % len(self.alphabet)])
            elif char.isspace():
                ciphered.append(char)
        return ''.join(ciphered)

    def daffine(self, message: str, key: (int, int)) -> str:
        key_inv = (self.__inv(key[0], len(self.alphabet)), key[1])
        ciphered = []
        for char in message.lower():
            if char.isalpha():
                ciphered.append(self.alphabet[((self.alphabet.index(
                    char) - key_inv[1]) * key_inv[0]) % len(self.alphabet)])
            elif char.isspace():
                ciphered.append(char)
        return ''.join(ciphered)

    def playfair(self, message: str, key: str) -> str:
        key_matrix = self.__get_key_matrix(key)
        message = self.__prepare_playfair_message(message)
        ciphered = []
        for i in range(0, len(message), 2):
            first = (key_matrix.index(message[i]) % 5, key_matrix.index(
                message[i]) // 5, key_matrix.index(message[i]))
            second = (key_matrix.index(message[i + 1]) % 5, key_matrix.index(
                message[i + 1]) // 5, key_matrix.index(message[i + 1]))
            if first[0] == second[0]:
                ciphered.append(key_matrix[((first[2] + 5) % 25)])
                ciphered.append(key_matrix[((second[2] + 5) % 25)])
            elif first[1] == second[1]:
                ciphered.append(
                    key_matrix[((first[0] + 1) % 5) + first[1] * 5])
                ciphered.append(
                    key_matrix[((second[0] + 1) % 5) + second[1] * 5])
            else:
                ciphered.append(key_matrix[(second[0] + first[1] * 5) % 25])
                ciphered.append(key_matrix[(first[0] + second[1] * 5) % 25])
        return ''.join(ciphered)

    def dplayfair(self, message: str, key: str) -> str:
        key_matrix = self.__get_key_matrix(key)
        ciphered = []
        for i in range(0, len(message) - 1, 2):
            first = (key_matrix.index(message[i]) % 5, key_matrix.index(
                message[i]) // 5, key_matrix.index(message[i]))
            second = (key_matrix.index(message[i + 1]) % 5, key_matrix.index(
                message[i + 1]) // 5, key_matrix.index(message[i + 1]))
            if first[0] == second[0]:
                ciphered.append(key_matrix[((first[2] - 5) % 25)])
                ciphered.append(key_matrix[((second[2] - 5) % 25)])
            elif first[1] == second[1]:
                ciphered.append(
                    key_matrix[((first[0] - 1) % 5) + first[1] * 5])
                ciphered.append(
                    key_matrix[((second[0] - 1) % 5) + second[1] * 5])
            else:
                ciphered.append(key_matrix[(second[0] + first[1] * 5) % 25])
                ciphered.append(key_matrix[(first[0] + second[1] * 5) % 25])
        return ''.join(ciphered)

    def vigenere(self, message: str, key: str) -> str:
        ciphered = []
        for i, char in enumerate(message.lower()):
            first_shift = self.alphabet.index(char)
            second_shift = self.alphabet.index(
                key[i % len(key)])
            ciphered.append(
                self.alphabet[(first_shift + second_shift) % len(self.alphabet)])
        return ''.join(ciphered)

    def dvigenere(self, message: str, key: str) -> str:
        ciphered = []
        for i, char in enumerate(message.lower()):
            first_shift = self.alphabet.index(char)
            second_shift = self.alphabet.index(
                key[i % len(key)])
            ciphered.append(
                self.alphabet[(first_shift - second_shift) % len(self.alphabet)])
        return ''.join(ciphered)

    def __curate_key(self, key: str) -> str:
        return ''.join([ch for ch in key.lower() if ch in list(self.alphabet)])

    def __get_key_matrix(self, key: str) -> [str]:
        key_list = []
        key_done = False
        key_index = 0
        alphabet_index = -1
        for i in range(len(self.alphabet) + len(key) - 1):
            if not key_done and key[key_index] not in key_list:
                if (key[key_index] == 'i' or key[key_index] == 'j'):
                    key_list.append('i')
                else:
                    key_list.append(key[key_index])
            if key_index < len(key):
                key_index += 1
            if key_index == len(key):
                key_done = True
                alphabet_index += 1
            if key_done and self.alphabet[alphabet_index] not in key_list and \
                    self.alphabet[alphabet_index] != 'j':
                key_list.append(self.alphabet[alphabet_index])
        # matriz = []
        # for i in range(5):
        #     matriz.append(key_list[i*5:i*5+5])
        # print(matriz)
        return key_list

    def __prepare_playfair_message(self, message: str) -> str:
        new_message = ''
        i = 0
        if len(message) % 2 != 0:
            message += 'x'
        while i < len(message):
            if i + 1 < len(message) and message[i] == message[i + 1]:
                new_message += message[i] + 'x'
                i -= 1
            elif i + 2 <= len(message):
                new_message += message[i: i + 2]
            elif i + 1 <= len(message):
                new_message += message[i: i + 1]
            i += 2
        if len(new_message) % 2 != 0:
            new_message += 'x'
        return new_message.replace('j', 'i')

    def gen_caesar(self) -> int:
        for i in range(len(self.alphabet)):
            yield i

    def gen_affine(self) -> (int, int):
        for i in range(len(self.alphabet)):
            for j in range(len(self.alphabet)):
                yield (i, j)

    def gen_words(self, word_file: str) -> str:
        WORDS = open(word_file).read().splitlines()
        for word in WORDS:
            yield self.__curate_key(word)

    @classmethod
    def railfence(self, message: str, rails: int) -> str:
        ciphered = []
        for i in range(rails):
            if i == 0 or i == rails - 1:
                ciphered.append(message[i::(rails - 1) * 2])
            else:
                first = message[i::(rails - 1) * 2]
                second = message[rails * 2 - i - 2::(rails - 1) * 2]
                for i in range(max(len(first), len(second))):
                    if i < len(first):
                        ciphered.append(first[i])
                    if i < len(second):
                        ciphered.append(second[i])
        return ''.join(ciphered)

    @classmethod
    def drailfence(self, message: str, rails: int) -> str:
        ciphered = []
        parts = [message[i:i + len(message) // rails]
                 for i in range(0, len(message), len(message) // rails)]
        for i in range(self.__getmax(parts)):
            for j in range(len(parts)):
                if i < len(parts[j]):
                    ciphered.append(parts[j][i])
        return ''.join(ciphered)

    @classmethod
    def columnartransposition(self, message: str, key: str) -> str:
        matrix = []
        message = message.lower()
        while len(message) % len(key) != 0:
            message += 'X'
        for i in range(len(message) // len(key)):
            matrix.append(list(message[i * len(key): i * len(key) + len(key)]))
        matrix = [list(i) for i in zip(*matrix)]
        matrix = [x for _, x in sorted(zip(list(key), matrix))]
        ciphered = []
        for i in range(len(matrix)):
            ciphered.append(''.join(matrix[i]))
        return ''.join(ciphered).replace('X', '')

    @classmethod
    def dcolumnartransposition(self, message: str, key: str) -> str:
        message = message.lower()
        complete_columns = len(message) % len(key)
        parts = [None] * len(key)
        aux = []
        for i in range(len(key)):
            aux.append(i)
        key_ord = list(zip(key, aux))
        key_ord = sorted(key_ord)
        rows = len(message) // len(key)
        for i in range(len(key)):
            if key_ord[i][1] < complete_columns:
                parts[i] = message[0:rows + 1]
                message = message[rows + 1:len(message)]
            else:
                parts[i] = message[0:rows]
                message = message[rows:len(message)]

        key_ord = sorted(key)
        parts = self.__untangle(list(key), parts, key_ord)
        parts = [list(i) for i in zip(*parts)]
        ciphered = []
        for i in range(len(parts)):
            ciphered.append(''.join(parts[i]))
        return ''.join(ciphered)

    @classmethod
    def __getmax(self, array: [str]) -> int:
        m = 0
        for s in array:
            m = max(m, len(s))
        return m

    @classmethod
    def __untangle(self, key: [str], matrix: [[str]], key_ord: [str]) -> [str]:
        parts_zipped = list(zip(matrix, key_ord))
        parts = []
        for i in range(len(key)):
            for j in range(len(parts_zipped)):
                if key[i] == parts_zipped[j][1]:
                    part = parts_zipped[j][0]
                    parts_zipped.pop(j)
                    break
            parts.append(part)
        return parts

    def __gcd(self, a: int, b: int) -> int:
        if b == 0:
            return a
        return self.__gcd(b, a % b)

    def __inv(self, a: int, m: int) -> int or False:
        if self.__gcd(a, m) != 1:
            return False
        for k in range(0, m):
            x = ((k * m) + 1) / float(a)
            if x.is_integer():
                return int(x)
        return False
