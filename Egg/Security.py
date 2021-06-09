import random

def loopAppend(init, addit):

    for i in addit:

        init.append(i)

    return init

alnum = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLNOPQRSTUVWXYZ'
num = '1234567890'
spec = r"""!"£$%^&*()_+-={}[]:@;'<>?,./|\`"""

def createID(prefix='0x', suffix='', length=32, include_characters=True, include_specials=True, include_numbers=True):

    sel_id = ''

    selection = []

    if include_characters: selection = loopAppend(selection, alnum)
    if include_specials: selection = loopAppend(selection, spec)
    if include_numbers: selection = loopAppend(selection, num)

    for i in range(length):

        random.shuffle(selection)
        sel_id += selection[0]

    return prefix + sel_id + suffix

def createRandomDictionary(seed):

    random.seed(seed)
    sel = isel = alnum + num + spec + ' '
    sel = [x for x in sel]
    random.shuffle(sel)

    return {isel[i]: s for i, s in enumerate(sel)}

class Egg:

    def __init__(self, seed):

        self.seed = seed
        self.keys = createRandomDictionary(self.seed)
        self.rkeys = {y: x for x, y in self.keys.items()}

    def encrypt(self, string):

        ms = ''

        for c in string:

            m = False

            for key, enc in self.keys.items():

                if key == c:

                    m = True
                    ms += enc
                    break

            if not m:

                ms += c

        return ms

    def decrypt(self, string):

        ms = ''

        for c in string:

            m = False

            for key, enc in self.rkeys.items():

                if key == c:

                    m = True
                    ms += enc
                    break

            if not m:
                ms += c

        return ms
