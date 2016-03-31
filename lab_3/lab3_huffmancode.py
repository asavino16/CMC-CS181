#Alex Savino 
#CS 181
#Lab 3 
#Part A: Huffman Encoding Compression 
#Part B: Huffman Encoding Based Compression 
import os
import sys 
import json
from heapq import merge 
import hashlib
import struct
 
def parse_file(filename): 
    d= {}
    with open(filename, "rb") as f:
        text = f.read()
        text1=list(text)
        for item in text1:
            if item not in d: 
                d[item]=1
            else:
                d[item]=d[item] +1
    return d 

def tolist(histogram): 
    lst = []
    for key in histogram: 
        lst.append((key, histogram[key])) 
    return lst
 

#takes in list of characters with number of occurences and builds binary tree 
def build_tree(lst):
    lst = sorted(lst, key=lambda y: y[1]) #sorts by second item in tuple (ex: [('c', 1), ('d', 2), ('f', 4)...])
    while len(lst)>1: 
        z=lst[0]
        y=lst[1]
        v=z[1]+y[1]
        k=[z[0],y[0]]
        lst=lst[2:]
        lst.append([k,v])
        lst = sorted(lst, key=lambda y:y[1])
        #lst = list(merge(lst[2:], [(k,v)]))
    tree =lst[0][0]
    return tree


def huffman(lst, side, code):
    if len(lst)==1: 
        code.append((lst, side))
    else: 
        left=huffman(lst[0],side+"0",code)
        right=huffman(lst[1], side+"1",code) 
    return code
    

def encode(filename, huff_code): 
     l=[]
     a = ""
     with open(filename, "rb") as f:
         text = f.read()
         text1=list(text)
         for item in text1:
             l.append(item)
         for item in l: 
             a = a + huff_code[item]
     return a

def check_length8(answer):
    tally=0
    for ch in answer: 
        tally+=1
    print tally
    if (tally%8==0):
        return answer
    else:
        diff = tally%8
        diff1=8-diff
        zero = diff1*"0"
        answer=answer+zero
        return answer

def convert_binary(string, output):
    for i in range(0, len(string),8): 
        integer_string = string[i:i+8]
        a = 0
        for j in range(7,-1, -1):
            a+=pow(2, j)*int(integer_string[7-j])
        output.write(struct.pack("B", a))
        
        
def main():

#1.1 Importing file 
    file1 = sys.argv[1]

#1.2 Calculating statistics on binary data 
    histogram = parse_file(file1)
    #histogram = convert_hex(parsing)
    new = tolist(histogram)

#1.2 Creating Huffman code 
    tree = build_tree(new)
    code=[]
    final = dict(huffman(tree, "", code))
    
#1.3 Printing out Huffman code 
    #print json.dumps({"Huffman code": final})

#2.1 Encoding data using the huffman code    
    encoded_file = encode(file1, final)
    encoded_string = check_length8(encoded_file) 
    #print json.dumps({"Encoded string ": encoded_string})
    
#2.2 Creating header for compressed file 
    file_size = os.path.getsize(file1)
    hash_size = hashlib.md5(open(file1, 'rb').read()).hexdigest()
    header = {"size": file_size, "hash": hash_size}
    compressed = open("compressed.bin", "wb")
    compressed.write(json.dumps(header)+"\n")
    compressed.write(json.dumps(final)+"\n")               
     
#2.3 Converting binary string to binary data and writing to output file                  
    convert_binary(encoded_string, compressed)  
    

if __name__ == '__main__':
    main()
    