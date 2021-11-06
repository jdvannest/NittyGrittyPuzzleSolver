import pickle 
import numpy as np

'''
Color Guide: 
    0 - Black (Edge)
    1 - White
    2 - Orage
    3 - Magenta
'''
class Tile:
    def __init__(self,id,colors,position,maxpos):
        self.id = id
        self.colors = colors
        self.position = position
        self.maxpos = maxpos
    
    def rotate(self):
        self.position = self.position+1 if (self.position<self.maxpos) else 1
        temp = np.zeros((2,2))
        temp[0][0] = int(self.colors[0][1])
        temp[0][1] = int(self.colors[1][1])
        temp[1][0] = int(self.colors[0][0])
        temp[1][1] = int(self.colors[1][0])
        self.colors = temp

T = Tile(id=1,
            colors=np.array([[3,2],[2,3]]),
            position = 1,
            maxpos=2)
out = open('Pieces/T01.pickle','wb')
pickle.dump(T,out)
out.close()

T = Tile(id=2,
            colors=np.array([[2,2],[3,2]]),
            position = 1,
            maxpos=4)
out = open('Pieces/T02.pickle','wb')
pickle.dump(T,out)
out.close()

T = Tile(id=3,
            colors=np.array([[2,2],[2,1]]),
            position = 1,
            maxpos=4)
out = open('Pieces/T03.pickle','wb')
pickle.dump(T,out)
out.close()

T = Tile(id=4,
            colors=np.array([[2,3],[2,1]]),
            position = 1,
            maxpos=4)
out = open('Pieces/T04.pickle','wb')
pickle.dump(T,out)
out.close()

T = Tile(id=5,
            colors=np.array([[3,1],[1,2]]),
            position = 1,
            maxpos=4)
out = open('Pieces/T05.pickle','wb')
pickle.dump(T,out)
out.close()

T = Tile(id=6,
            colors=np.array([[2,3],[1,1]]),
            position = 1,
            maxpos=4)
out = open('Pieces/T06.pickle','wb')
pickle.dump(T,out)
out.close()

T = Tile(id=7,
            colors=np.array([[3,2],[1,2]]),
            position = 1,
            maxpos=4)
out = open('Pieces/T07.pickle','wb')
pickle.dump(T,out)
out.close()

T = Tile(id=8,
            colors=np.array([[2,2],[2,2]]),
            position = 1,
            maxpos=1)
out = open('Pieces/T08.pickle','wb')
pickle.dump(T,out)
out.close()

T = Tile(id=9,
            colors=np.array([[2,1],[1,2]]),
            position = 1,
            maxpos=2)
out = open('Pieces/T09.pickle','wb')
pickle.dump(T,out)
out.close()

T = Tile(id=10,
            colors=np.array([[1,1],[2,3]]),
            position = 1,
            maxpos=4)
out = open('Pieces/T10.pickle','wb')
pickle.dump(T,out)
out.close()

T = Tile(id=11,
            colors=np.array([[1,1],[1,1]]),
            position = 1,
            maxpos=1)
out = open('Pieces/T11.pickle','wb')
pickle.dump(T,out)
out.close()

T = Tile(id=12,
            colors=np.array([[1,2],[1,1]]),
            position = 1,
            maxpos=4)
out = open('Pieces/T12.pickle','wb')
pickle.dump(T,out)
out.close()

T = Tile(id=13,
            colors=np.array([[1,2],[1,2]]),
            position = 1,
            maxpos=4)
out = open('Pieces/T13.pickle','wb')
pickle.dump(T,out)
out.close()

T = Tile(id=14,
            colors=np.array([[2,3],[2,3]]),
            position = 1,
            maxpos=4)
out = open('Pieces/T14.pickle','wb')
pickle.dump(T,out)
out.close()

T = Tile(id=15,
            colors=np.array([[1,1],[3,1]]),
            position = 1,
            maxpos=4)
out = open('Pieces/T15.pickle','wb')
pickle.dump(T,out)
out.close()

T = Tile(id=16,
            colors=np.array([[2,1],[3,2]]),
            position = 1,
            maxpos=4)
out = open('Pieces/T16.pickle','wb')
pickle.dump(T,out)
out.close()

T = Tile(id=17,
            colors=np.array([[3,1],[3,2]]),
            position = 1,
            maxpos=4)
out = open('Pieces/T17.pickle','wb')
pickle.dump(T,out)
out.close()

T = Tile(id=18,
            colors=np.array([[1,1],[3,3]]),
            position = 1,
            maxpos=4)
out = open('Pieces/T18.pickle','wb')
pickle.dump(T,out)
out.close()

T = Tile(id=19,
            colors=np.array([[2,3],[3,1]]),
            position = 1,
            maxpos=4)
out = open('Pieces/T19.pickle','wb')
pickle.dump(T,out)
out.close()

T = Tile(id=20,
            colors=np.array([[3,3],[1,2]]),
            position = 1,
            maxpos=4)
out = open('Pieces/T20.pickle','wb')
pickle.dump(T,out)
out.close()

T = Tile(id=21,
            colors=np.array([[3,3],[2,3]]),
            position = 1,
            maxpos=4)
out = open('Pieces/T21.pickle','wb')
pickle.dump(T,out)
out.close()

T = Tile(id=22,
            colors=np.array([[3,3],[3,3]]),
            position = 1,
            maxpos=1)
out = open('Pieces/T22.pickle','wb')
pickle.dump(T,out)
out.close()

T = Tile(id=23,
            colors=np.array([[3,3],[3,1]]),
            position = 1,
            maxpos=4)
out = open('Pieces/T23.pickle','wb')
pickle.dump(T,out)
out.close()

T = Tile(id=24,
            colors=np.array([[3,1],[1,3]]),
            position = 1,
            maxpos=2)
out = open('Pieces/T24.pickle','wb')
pickle.dump(T,out)
out.close()