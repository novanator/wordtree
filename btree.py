"""
Author: Novanator 2012
Program: Translation2
"""

class Node:
    def __init__(self,load=0):
        self.load=load
        self.left=None
        self.right=None
    
class BinTree:
    def __init__(self):
        self.root=None

    def exists(self,load):
        return self.__exist(load, self.root)
    
    
    #iterative function
    def __exist(self, load, r):
        while r!=None :
            if load < r.load:
                r = r.left
            elif load > r.load:
                r = r.right
            else:
                return True
        return False

    def put(self,item):
        if self.exists(item)==True:
            print("double: ",item)
            
        new=Node()
        new.load=item
        
        if self.root==None:
            self.root=new
            return
        p=self.root
        q=0
        while item!=p.load:
            if item<p.load:
                if p.left==None:
                    p.left=new
                    q=1
                else:
                    p=p.left
                    
            elif item>p.load:
                if p.right==None:
                    p.right=new
                    q=1
                else:
                    p=p.right
                        
        if q==0:
            print("double: ",item)
        
    #recursive function
    def __write(self, r):
        if r == None:
            return
        self.__write(r.left)
        print(r.load)
        self.__write(r.right)

    def write2(self):
        self.__write(self.root)

    def nElements(self):
        return self.__antalElementer(self.root)

    #recursiv function
    def __numberElements(self,p):
        if p == None:
            return 0;
        return 1+self.__numberElements(p.left)+self.__numberElements(p.right);
        
        
        
        
