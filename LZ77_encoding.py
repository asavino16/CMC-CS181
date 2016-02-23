#Alex Savino 
#CS 181
#Lab 2: Implementing a LZ77 Compression Scheme

import os
import struct
import sys 

#encoding 
def LZ77_search(search, look_ahead):
    ls = len(search)
    lla = len(look_ahead)
    
    #length of search buffer is zero
    if(ls == 0):
        return (0, 0, look_ahead[0]) 

    if(lla == 0):
    #error condition, why would you call with empty look-ahead?
        return (-1, -1, "")

    best_offset = 0
    best_length = 0

    buf = search + look_ahead
    #search_pointer 
    sp = ls
    for i in range(0,ls): #all of the potential starting positions for search
        #match length
        length = 0
        while buf[i+length] == buf[sp+length]:
            #found a match
            length += 1
            #check for search reaching the end of the look_ahead
            if (sp + length) == len(buf):
                length -= 1
                break

        if length > best_length:
            best_offset = i
            best_length = length
    return (best_offset, best_length, buf[sp+best_length])
  
MAX_SEARCH=1024
MAX_LOOKAHEAD=64
  
def encoding_LZ77(inp, output):   
    search_idx=0
    lookahead_idx=0
    input=list(inp)
    while lookahead_idx < len(input): 
        search = input[search_idx:lookahead_idx]
        lookahead = input[lookahead_idx:lookahead_idx+MAX_LOOKAHEAD]
        (offset, length, char) = LZ77_search(search, lookahead)
        print (offset, length, char)
        
        #pack into a 3-byte tuple for writing to a file 
        shifted_offset = offset << 6
        offset_and_length = (shifted_offset + length)
        out_bytes = struct.pack(">Hc", offset_and_length, char)
        output.write(out_bytes) 
        output.write(char)   
    
        lookahead_idx += length+1
        search_idx=lookahead_idx - MAX_SEARCH
        if search_idx <0:
            search_idx = 0  

#unpacking
def unpack_decompress(filename, output):
    f=open(filename,'rb')
    in_str=f.read()
    inp = list(f)
    buf = []
    i=0
    while i<len(inp):
        (offset_and_length, char) = struct.unpack('>%dH' %len(filename),in_str)
        offset = offset_and_length >> 6 
        length = offset_and_length - (offset << 6)   
        i +=3
        
        #decoding 
        if (offset == 0) and (length == 0): 
            buf += char
        else:
            start = len(buf) - MAX_SEARCH
            if start <0: 
                start = offset
            else: 
                start += offset
            for j in range(length): 
                buf += buf[start+j]
            buf += char
    output.write(str(buf)) 

def parse_file(filename): 
    d= []
    with open(filename, "rb") as f:
        text = f.read()
        text1=list(text)
        for item in text1:
            d=d+[item]
    return d 


def main(): 
    file1 = sys.argv[1]
    parsing = parse_file(file1)
    
    compressed = open("compressed.bin", "wb")
    
    compression = encoding_LZ77(parsing, compressed)
    compressed.close() 
        
    final = open("final.bin", "wb") 
    decompress = unpack_decompress("compressed.bin", final)
    final.close() 
    
    
if __name__ == '__main__':
    main()