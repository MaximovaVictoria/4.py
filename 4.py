import string


class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print(self):
        print(self.letters)

    def letters_num(self):
        return len(self.letters)


class EngAlphabet(Alphabet):

    __letters_num = 26

    def __init__(self):
        super().__init__('En', string.ascii_uppercase)

    def is_en_letter(self, a):
        if a in string.ascii_uppercase:
            print('буква относится к английскому алфавиту')
        else:
            print('буква не относится к английскому алфавиту')

    def letters_num(self):
       return self.__letters_num

    @staticmethod
    def example():
        return 'Hello'


if __name__ == '__main__':
    en1 = EngAlphabet()
    en1.print()
    print(en1.letters_num())
    en1.is_en_letter('F')
    en1.is_en_letter('Щ')
    print(en1.example())
