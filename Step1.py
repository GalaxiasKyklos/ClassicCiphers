from ClassicCiphers import ClassicCiphers

cipher = ClassicCiphers('abcdefghijklmnopqrstuvwxyz')
message = 'theonlysourceofknowledgeisexperience'

for i in cipher.gen_caesar():
    caesar = cipher.caesar(message, i)
    for tup in cipher.gen_affine():
        affine = cipher.affine(caesar, tup)
        if affine == 'GJDHZOBRCJENDHIXGTEPWUUOXCWRHEEQOXUE'.lower():
            print('Caesar then Affine')
            print(affine)
            print(i)
            print(tup)
            print('---------------------------')

for tup in cipher.gen_affine():
    affine = cipher.affine(message, tup)
    for i in cipher.gen_caesar():
        caesar = cipher.caesar(affine, i)
        if caesar == 'GJDHZOBRCJENDHIXGTEPWUUOXCWRHEEQOXUE'.lower():
            print('Affine then Caesar')
            print(caesar)
            print(tup)
            print(i)
            print('---------------------------')

for word in cipher.gen_words('./ins/words'):
    vigenere = cipher.vigenere(message, word)
    for i in cipher.gen_caesar():
        caesar = cipher.caesar(vigenere, i)
        if caesar == 'GJDHZOBRCJENDHIXGTEPWUUOXCWRHEEQOXUE'.lower():
            print('Vigenere then Caesar')
            print(caesar)
            print(word)
            print(i)
            print('---------------------------')

for i in cipher.gen_caesar():
    caesar = cipher.caesar(message, i)
    for word in cipher.gen_words('./ins/words'):
        vigenere = cipher.vigenere(caesar, word)
        if vigenere == 'GJDHZOBRCJENDHIXGTEPWUUOXCWRHEEQOXUE'.lower():
            print('Caesar then Vigenere')
            print(vigenere)
            print(i)
            print(word)
            print('---------------------------')

for tup in cipher.gen_affine():
    affine = cipher.affine(message, tup)
    for word in cipher.gen_words('./ins/words'):
        vigenere = cipher.vigenere(affine, word)
        if vigenere == 'GJDHZOBRCJENDHIXGTEPWUUOXCWRHEEQOXUE'.lower():
            print('Affine then Vigenere')
            print(vigenere)
            print(tup)
            print(word)
            print('---------------------------')

for word in cipher.gen_words('./ins/words'):
    vigenere = cipher.vigenere(message, word)
    for tup in cipher.gen_affine():
        affine = cipher.affine(vigenere, tup)
        if affine == 'GJDHZOBRCJENDHIXGTEPWUUOXCWRHEEQOXUE'.lower():
            print('Vigenere then Affine')
            print(affine)
            print(word)
            print(tup)
            print('---------------------------')

for i in cipher.gen_caesar():
    caesar = cipher.caesar(message, i)
    for word in cipher.gen_words('./ins/words'):
        playfair = cipher.playfair(caesar, word)
        if playfair == 'GJDHZOBRCJENDHIXGTEPWUUOXCWRHEEQOXUE'.lower():
            print('Caesar then Playfair')
            print(playfair)
            print(i)
            print(word)
            print('---------------------------')

for word in cipher.gen_words('./ins/words'):
    playfair = cipher.playfair(message, word)
    for i in cipher.gen_caesar():
        caesar = cipher.caesar(playfair, i)
        if caesar == 'GJDHZOBRCJENDHIXGTEPWUUOXCWRHEEQOXUE'.lower():
            print('Playfair then Caesar')
            print(caesar)
            print(word)
            print(i)
            print('---------------------------')

for tup in cipher.gen_affine():
    affine = cipher.affine(message, tup)
    for word in cipher.gen_words('./ins/words'):
        playfair = cipher.playfair(affine, word)
        if playfair == 'GJDHZOBRCJENDHIXGTEPWUUOXCWRHEEQOXUE'.lower():
            print('Affine then Playfair')
            print(playfair)
            print(tup)
            print(word)
            print('---------------------------')

for word in cipher.gen_words('./ins/words'):
    playfair = cipher.playfair(message, word)
    for tup in cipher.gen_affine():
        affine = cipher.affine(playfair, tup)
        if affine == 'GJDHZOBRCJENDHIXGTEPWUUOXCWRHEEQOXUE'.lower():
            print('Playfair then Affine')
            print(affine)
            print(word)
            print(tup)
            deciph = cipher.daffine(
                'VJDO DCPQAED PZLGXLGA IOGGTU MXEWP JT OGY XGTEPWUUO HA GJN NZHQECZEW MCDWA WII XGCMWOUAD HN BOEPCUM JUEDUJ NBHG WRHEEQOXUE OGU WLNC XG LIM'.lower().replace(' ', ''), tup)
            print(cipher.dplayfair(deciph, word))
            print('---------------------------')
