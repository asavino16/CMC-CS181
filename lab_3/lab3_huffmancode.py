#Alex Savino 
#CS 181
#Lab 3
import os
import sys 
import operator 
import json
from heapq import merge 
 
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

def convert_hex(histogram):
    d={} 
    for key in histogram: 
        if key.isalpha():
            d[key]=histogram[key]
        else: 
            d[hex(ord(key))]=histogram[key]          
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
    
   
def main():
    file1 = sys.argv[1]
    parsing = parse_file(file1)
    histogram = convert_hex(parsing)
    new = tolist(histogram)
    
    tree = build_tree(new)
    code=[]
    final = dict(huffman(tree, "", code))
    
    print json.dumps({"Huffman code": final})


if __name__ == '__main__':
    main()
    