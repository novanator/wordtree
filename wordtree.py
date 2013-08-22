"""
author: Novanator 2012
Program: Wordtree2
"""

import random
from btree import Node
from btree import BinTree

class Queue(object):

    class __Node(object):
        def __init__(self,value):
            self.value = value
            self.next=None


    def  __init__(self):
            self.__first=None
            self.__last=None
            
    def put(self, x):
        p = Queue.__Node(x)
        if self.__first==None:
            self.__first = p
            self.__last = p
        else:
            tmp = self.__last 
            tmp.next = p 
            self.__last = p 
    
    def get(self):
        if self.__first!=None:
            x = self.__first.value
            self.__first = self.__first.next
            return x
        return None

    def isempty(self):
        if self.__first==None:
            return True
        else:
            return False

    def show(self):
        p=self.__first
        while p != None:
            print(p.value,end=" ")
            p = p.next


class Nodeson(object):
    def __init__(self,word):
        self.word=word
        self.father=None


def writeChain(son):
    if son.father!=None:
        writeChain(son.father)
    klist.append(son.word)

def makeSons(startword):     
        
        lista=list(startword.word)
        for x in letter:
                if tree.exists(x+lista[1]+lista[2]) and not oldwords.exists(x+lista[1]+lista[2]):
                        oldwords.put(x+lista[1]+lista[2])
                        a=Nodeson(x+lista[1]+lista[2])
                        a.father=startword
                        q.put(a)
                if tree.exists(lista[0]+x+lista[2]) and not oldwords.exists(lista[0]+x+lista[2]):
                        oldwords.put(lista[0]+x+lista[2])
                        b=Nodeson(lista[0]+x+lista[2])
                        b.father=startword
                        q.put(b)
                if tree.exists(lista[0]+lista[1]+x) and not oldwords.exists(lista[0]+lista[1]+x):
                        oldwords.put(lista[0]+lista[1]+x)
                        c=Nodeson(lista[0]+lista[1]+x)
                        c.father=startword
                        q.put(c)

                if (x+lista[1]+lista[2])==endword:
                    writeChain(a)
                    return True
                    
                if (lista[0]+x+lista[2])==endword:
                    writeChain(b)
                    return True
                
                if (lista[0]+lista[1]+x)==endword:
                    writeChain(c)
                    return True
                
        return False


endword = input("Write the end word:" )
f=open("list.txt","r")
contents = f.read ()
words = contents.split ()
tree=BinTree()
for i in words:
    tree.put(i)

random.shuffle(words)
letter=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","y","z","å","ä","ö"]

plista=[]

for x in words:
    klist=[]
    oldwords=BinTree()
    q=Queue()

    startword = Nodeson(x)
    q.put(startword)

    way=0
    while not q.isempty():
        found = makeSons(q.get())
        if found:
            way=1
            break
    
    plista.append(len(klist))
    

maxx=max(plista)

r=-1
faraway=[]
for y in plista:
    r+=1
    if y==maxx:
        faraway.append(r)
        
for j in faraway:
    print(words[j],end=" ")

if len(faraway)==1:
    print("are the words that are furthest away from",endword,"and the number of sons from", endword,"is/are",maxx-1)
else:
    print("are the words that are furthest away from",endword,"and the number of sons from", endword,"is/are",maxx-1)

