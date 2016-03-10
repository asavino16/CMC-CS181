#Alex Savino 
#CS 181
#Lab 1: Iterating over txt file and compiling statistics 
import os
import math
import sys 
import json


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


#calculates entropy given histogram of file 
def calculate_entropy(d): 
    total = sum(d.values())
    d_prob = {}
    for key in d: 
        d_prob[key]=float(d[key])/float(total) 
    d_log = {}
    for key in d_prob: 
        d_log[key]=math.log(d_prob[key]) 
    d_problog = {}
    for key in d_prob: 
        d_problog[key]=d_prob[key]*d_log[key]
    answer = sum(d_problog.values())
    return float((-1))*answer 


def convert_hex(histogram):
    d={} 
    for key in histogram: 
        if key.isalpha():
            d[key]=histogram[key]
        else: 
            d[hex(ord(key))]=histogram[key]          
    return d
       
def main():
    file1 = sys.argv[1]
    parsing = parse_file(file1)
    histogram = convert_hex(parsing)
    
    entropy=calculate_entropy(histogram)
    total = sum(histogram.values())
    histogram["total"]=total
    
    print json.dumps({"entropy": entropy})
    print json.dumps(histogram)
    
if __name__ == '__main__':
    main()