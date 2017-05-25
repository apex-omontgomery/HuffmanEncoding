 
import math # for the theoretical min calc. 

# Need to create the heap class
T = {}

class Node:
    def __init__(self, freq):
        self.char = None         # value of index corresponding to array S
        self.freq = freq       # equivalent to  f[char]
        self.left = None         # Left child
        self.right = None      # Right child
        # no need for a parent. 
        
    


    
class MinHeap:
    def __init__(self):
        #array of nodes
        self.array = [Node(1000)]
        self.heap_size = -1
        self.min_size = 0
        self.root = None
        
    def Parent(self, i):
        # Unlike Left and Right, Parent will encounter non-intenger values. 
        # Need to create a floor function that gives correct parent value. 
        # We know the parent for a log2(n) tree = i/2. So for i =1, we have a left = 
        if (i % 2 == 0):
            p = i/2 -1            
            return int(p)
        else: 
            p = (i+1)/2 -1
            return int(p)
            
    def Left(self, i):
        l = (i + 1)*2 -1
        return(int(l))
    
    def Right(self, i):    
        r = (i+1)*2 
        return (int(r))

        
    def HeapInsert(self, char, freq, S):
        
        #location should be the self.heap_size
        #change heap size
        if (self.heap_size == -1):   # After initialization-- first run
           self.heap_size = 0        # Sets to length of 1 
        else:
           self.heap_size += 1       # Increases size by one
           self.array.append(Node(10000))  #adds a big value       
        self.HeapIncKey(self.heap_size, freq, S[char])
        
    def NHeapInsert(self, Node): #when insertin a node during the huffman instead of inserting values. 
        self.heap_size +=1
        freq = Node.freq                        # Mimic behavior above, save freq 
        Node.freq = 10000                       # Reset node freq like above. 
        self.array.append(Node)                 # Add the new node. 
        #for i in range(0, self.heap_size, 1):
            #print((self.array[i]).freq)
        
        self.HeapIncKey(self.heap_size, freq, Node.char)     #add this value. 
        if (len(self.array)==1):  # If this is true, we have one node, this only happens during the node insert
            self.root = Node
            return (self.root)
            
        
    def HeapIncKey(self, i, key, char):  #(self, char, freq)
        
        if (key > (self.array[i]).freq):       #this checks to see if the new frequency is bigger than 100000
            
            print('error: new key larger than current key')
        self.array[i].freq = key             # Replaces the current 10000 value with freq
        self.array[i].char = char            # Inserts character
        while ((i > 1) and (self.array[self.Parent(i)].freq > self.array[i].freq)):
            Temp = self.array[i]
            self.array[i] = self.array[self.Parent(i)]
            self.array[self.Parent(i)] = Temp                
            i = self.Parent(i)
         
        
    # Pulls minimum value from priority queue
    # Must be O( nlogn))
    def Hdeletemin(self):
        if (self.heap_size < 0):
            print('heap underflow')
        min = self.array[0]
        
        
        self.array[0] = self.array[self.heap_size]  # Sets old min value to one of the larger values. 
        self.array = self.array[0:-1]               # Remove last node from array. 
        self.heap_size -= 1                         # Decrease heap size counter
        self.MinHeapify(0)
        return min
        

    # Returns element in H with the minimum value
    def HMinimum(self):
        return self.array[0]
        
        
# Maintains property- A[Parent(i)<= A(i)] following a delete or insert.     

    def MinHeapify(self, i ):
        l = self.Left(i)
        r = self.Right(i)
        #max property
        if (l <= self.heap_size and (self.array[l]).freq < (self.array[i]).freq):
            smallest = l
        else:
            smallest = i
        if (r <= self.heap_size and (self.array[r]).freq < (self.array[smallest]).freq):
            smallest = r
        if (smallest != i):
            Temp = self.array[i]
            self.array[i]= self.array[smallest]
            self.array[smallest] =Temp
            self.MinHeapify( smallest )
            
    def PostOrder(self, Node): #check to see if lost nodes. 
        if (Node != None):
            self.PostOrder(Node.left)
            self.PostOrder(Node.right)
            #print(Node.char)
            




def huffmanEncode(S, f):
    n = len(S)
    H = MinHeap() #initialize empty heap of type none with length of the input char list.
    for i in range(0, n, 1):
       
        H.HeapInsert(i, f[i],S)   #at location i, with value f[i]   
    
    #print('built base')
    treearray=[]
    chararray = []
    #for k in range (n+1, 2*n-1, 1 ):
    for k in range (n+1, 2*n, 1 ): #Changed from 2n-1 to 2n, so that I can get the tree root. 
        
        
        l = H.Hdeletemin()        
        m = H.Hdeletemin()
        treearray.append(l)
        treearray.append(m)
        if (len(l.char)==1):
            chararray.append(l)
        if (len(m.char)==1):
            chararray.append(m)
            
        
        #if (len(l.char)== 1):
         #   print(l.char)
        #if (len(m.char) ==1 ):
        #    print(m.char)
         
        #characteristics of new node
        nN = Node((l.freq+m.freq))
        nN.char = l.char + m.char  
        nN.left = l
        nN.right = m
        # Insert new node
        H.NHeapInsert(nN)
       
    #print('built tree')  

    #H.PostOrder(H.root)
    #create and return codebook T
    print(len(chararray))
    print(len(treearray))
    makeTree(chararray, treearray)
        
    
    
    HuffCodebook(H.root, '')
    #print(T)
    return T
    
def MakeTree(chararray, treearray):
    
    count = len(treearray)-1
    while( len(treearray) > 0):
        
        
    
    
    
def HuffCodebook(Node, code):
        # 1 if left, 0 if right
        
    if ((Node.right == None) and (Node.left == None)):  #Base condition- we found a leaf
        T[Node.char] = code #add to dict from above. 
        
        
    if (Node.left): #If there is a node on the left, go left and increase your string by 1
        code += '1'
        HuffCodebook(Node.left, code)
        
    if (Node.right):#If there is a node on the left, go left and increase your string by 1
        code += '0'
        HuffCodebook(Node.right, code)
    
    
    
    

       
 

def EncodeString( x, T):
    y = ''  #declare empty string
    for i in range(0, len(x), 1):
        y += T[x[i]]  
    return y

   
    

# input: A string X of length M
# output: 1. list/vector S of length N <= M of unique characters in string X with indices i. 
#         2. vector of list N <= M that corresponds to indices i in S with frequency k
def string2freq(x):

    pre_array = [0]*125 #create blank array of length 125, unicode char 122 is the lowercase z. 
    for i in range(0, len(x), 1):
        val = ord(x[i]) #finds unicode integer
        try: #limit initial array size so we don't have huge empty array. 
            pre_array[val] +=1  #increases count at array. 
        except IndexError: #if we have 'normal' chars this allows a shorter array. 
            pre_array.extend([0]*(val - len(pre_array) + 1))  
            # finds current size, then how big the curren val is, adds one to prevent index error. 
            pre_array[val]+=1
            
    # Python list comprehension:
    # Remove locations where = 0. but we can enumerate this location, to convert to char. 
    # This output gives us ordered char list. 
   
    # enumerate(pre_array) gives tuple: (indice, value). chr(indice)= original unicode char.    
    S = [ chr(i) for i,j in enumerate(pre_array) if j != 0] 
    
    # Now uses values in s, converts to unicode, then looks in full array for the frequency.
    f = [ pre_array[ord(value)] for value  in S]
    
    return [S, f]
      
x = 'the road not taken by robert frost two roads diverged in a yellow wood, and sorry i could not travel both and be one traveler, long i stood and looked down one as far as i could to where it bent in the undergrowth; then took the other, as just as fair, and having perhaps the better claim, because it was grassy and wanted wear; though as for that the passing there had worn them really about the same, and both that morning equally lay in leaves no step had trodden black. oh, i kept the first for another day! yet knowing how way leads on to way, i doubted if i should ever come back. i shall be telling this with a sigh somewhere ages and ages hence: two roads diverged in a wood, and i- i took the one less traveled by, and that has made all the difference.'


(a,b) = string2freq(x)
book = huffmanEncode(a,b)
#x = 'hi how are you mr butters'
#print(len(EncodeString(x, book)))
#print(len(x)*8)

minbits = ['']*len(b) 
#print(b)
bitsum = 0
l = len(x)
#print(len(b))
for i in range(0,len(b), 1):
   # print(i)
    minbits[i] = -(b[i]/l)*math.log(b[i]/l, 2)
    bitsum += minbits[i]
    
#print(bitsum)
#print(minbits)   

