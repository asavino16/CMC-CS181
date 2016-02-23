# CMC-CS181
Alex Savino
asavino16@cmc.edu
lab 2

1) 
Compression ratio:
Alice and Wonderland: 156KB/168KB=92%
Poetry-Edgar Allen Poe: 62KB/64KB=94%

Entropy: 
Alice and Wonderland: 3.217687929229665
Poetry-Edgar Allen Poe: 3.2100657597786904

It appears to not be compressing that effectively. I'm unsure why but I would guess that there would be repeated words within both Alice and Wonderland and the Poetry - perhaps sentences and words coming after one another often is not common so the compression is not that great and the algorithm is only compressing repeated words.  


2) 
Random.org 
Compression ratio: 1M/
Entropy: 5.545043246556351

3) Data that is less random might compress better, because with random data it'll take way longer to find long matches. Possibly song lytics would compress better because sentences are more likely to be repeated than in novels. 
The Random.org file took an extremely long time to compress. The Entropy is high so the compression is not that effective. The less random the file, the better the compression can be. 

4) 
Entropy of compressed A&W: 4.6574505177624
Entropy of compressed Poetry: 4.641521924179349

It makes sense that the entropy of the compressed files is higher since they will have less repeated values after the compression. 