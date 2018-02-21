import sys
from ClassicCiphers import ClassicCiphers

cipher = ClassicCiphers('abcdefghijklmnopqrstuvwxyz')
message = open('./ins/Step3.in').read()
algorithm = sys.argv[1]

if algorithm == 'caesar':
    for i in cipher.gen_caesar():
        print(i)
        print(cipher.caesar(message, i * -1))
elif algorithm == 'affine':
    for i in cipher.gen_affine():
        print(i)
        print(cipher.daffine(message, i))
elif algorithm == 'playfair':
    for i in cipher.gen_words('./ins/words'):
        if len(i) > 2:
            print(i)
            print(cipher.dplayfair(message.lower().replace('j', 'i'), i.lower()))
elif algorithm == 'vigenere':
    for i in cipher.gen_words('./ins/words'):
        print(i)
        print(cipher.dvigenere(message, i))
