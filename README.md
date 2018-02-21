# Description of the module ClassicCiphers
## Name: Saúl Ponce
## is699399
### Uses `Python 3.6`
### Instance methods:
- `ClassicCiphers(alphabet: srt)`
  - Constructor, the alphabet is a string with the symbols to use, do not separete them with spaces unless you want the space character to be part of your alphabet.
- `caesar(message: str, key: int) -> str`
  - Caesar cipher, do decrypt use the key multiplied by -1.
- `affine(message: str, key: (int, int)) -> str`
  - Affince cipher, the key is a tuple with (a, b), given that the message is encrypted using the formula `F(x, [a, b]) = (ax + b) mod m`.
- `playfair(message: str, key: str) -> str`
  - Playfair cipher, uses a word key, the key must be buildable form the alphabet, the result is given without the letter `j`.
- `vigenere(message: str, key: str) -> str`
  - Vigenerè cipher, the key must be buildable with the alphabet.
- `daffine(message: str, key: (int, int)) -> str`
  - Affince decipher.
  - The key is exactly the same used to encrypt, this method computes de modular inverse of `a` and substracts `b`.
- `dplayfair(message: str, key: str) -> str`
  - Playfair decipher, uses a word key.
- `dvigenere(message: str, key: str) -> str`
  - Vigenerè decipher, uses a word key.
- `gen_caesar() -> int`
  - Generates numbers to serve as keys to the    method.
  - The numbers come from `0` (inclusive) to `len(alphabet)` (exclusive).
- `gen_affine() -> (int, int)`
  - Generates tuples to serve as keys to the `daffine` method.
  - Generets (a, b) tuples given (a, b) are part of the set of nombers between `0` (inclusive) to `len(alphabet)` (exclusive).
- `gen_words(word_file: str) -> str`
  - Returns one by one the words in a wordfile called `word_file`.
  - The wordfile must have a word per line.
  - The words are striped from every character that is not contained in the alphabet.

### Class (static) methods
- `railfence(message: str, rails: int) -> str`
  - Railfence cipher, the number of rails must not exceed `len(message)`.
- `columnartransposition(message: str, key: str) -> str`
  - Columnar Transposition cipher, the key can have repeated letters.
  - All of the key must be either lowercase or uppercase.
  - The message will be padded with `X` to fill the gaps.
- `drailfence(message: str, rails: int) -> str`
  - Railfence decipher, the number of rails must not exceed `len(message)`.
- `dcolumnartransposition(message: str, key: str) -> str`
  - Columnar Transposition decipher, the key can have repeated letters.
  - All of the key must be either lowercase or uppercase.
  - The message may or may not be padded.
  - The message will be transformed into lowercase.