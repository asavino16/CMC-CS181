CMC-CS181
Alex Savino
asavino16@cmc.edu
lab 3

For this lab, I used the USConstitution and applied Huffman coding to it. The result was: 
{"Huffman code": {"0": "1100", "A": "00010001", "C": "10111100", "B": "1010100001", "E": "1011000110", "D": "1010100010", "G": "10101000000", "F": "00010000011", "I": "1011000111", "H": "1011000001", "K": "00010011101101", "J": "1011000000", "M": "000100101", "L": "010010000", "O": "1011010100", "N": "000100100", "Q": "0001001110101", "P": "10111101", "S": "0100101", "R": "101010010", "U": "101100001", "T": "01001001", "W": "0001001111", "V": "000100001", "Y": "10110101101", "a": "0101", "c": "111100", "b": "000110", "e": "011", "d": "01000", "g": "1011011", "f": "111101", "i": "0011", "h": "11111", "k": "1011010101", "j": "1011010111", "m": "010011", "l": "10100", "o": "1001", "n": "1000", "q": "1010100011", "p": "000101", "s": "0010", "r": "0000", "u": "101011", "t": "1110", "w": "1010101", "v": "1011001", "y": "1011111", "x": "1101", "z": "0001001100"}}


Part b: encoding txt files 
Compression ratios:
US Constitution: 44K/26K
Drinks list: 47K/29K
The Aliens III Script: 71K/37K

Part c: 
Compressed USConstitution into "compressed.bin" and effectively decompressed it into file called "decompressed.txt". It looks the exact same as the original file. 

Part 4: Extra Credit 
Switched files with Iris and Kayla. The decompression worked with Iris but with Kayla's file it gave me an error: Non-ASCII character '\xfd' in file compressed_kayla.txt. 

