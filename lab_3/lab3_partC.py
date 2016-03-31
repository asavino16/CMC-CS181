#Alex Savino 
#CS 181
#Lab 3 Part C: Decoding a Compressed File 

import sys 
import json
import hashlib
import struct


def main():
    
#3.1 Reading the Header and Huffman Code 
    input_file=open(sys.arg[1], "rb") 
    header = json.loads(input_file.readline())
    print header
    
    huffman_code = json.loads(input_file.readline()) 
    decode_dict = {v: k for k, v in huffman_code.iteritems()} 
    binary_data = input_file.read() 
    
#3.2 Converting Binary to String 
    binary_string = ""
    for byte in binary_data: 
        binary_string+= format(ord(byte, '08b'))
        
#3.3 Decoding the Compressed Data 
    decoded_data = ""
    while len(decoded_data) != header['size']: 
        sub_str = "" 
        i = 0 
        while sub_str not in decode_dict: 
            sub_str = binary_string[0:i]
            i=i+1
        decoded_data += decode_dict[sub_str]
        binary_string = binary_string[i-1:]

#3.4 Verifying the Decompressed Data" 
    if hashlib.md5(decoded_data).hexdigest() == header['hash']:
        f = open(sys.argv[2], 'wb') 
        f.write(decoded_data) 
        f.close()
        print "MD5 hash matched. Wrote %i bytes to %s" % (header['size'])
    else: 
        print "MD5 hash mismatch." 
        

if __name__ == '__main__':
    main()
    