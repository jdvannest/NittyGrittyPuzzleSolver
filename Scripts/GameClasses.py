import numpy as np
import matplotlib.pylab as plt

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

class Board:
    def __init__(self):
        self.pieces = [[np.nan]*5,[np.nan]*5,[np.nan]*5,[np.nan]*5,[np.nan]*5]
        self.pieces[2][2] = Tile(id=0,colors=np.array([[0,0],[0,0]]),position=1,maxpos=1)
        self.placed = []
    
    def printout(self):
        out = [[np.nan]*5,[np.nan]*5,[np.nan]*5,[np.nan]*5,[np.nan]*5]
        for i in np.arange(5):
            for j in np.arange(5):
                try:
                    out[i][j]=self.pieces[i][j].id
                except:
                    pass
        for i in np.arange(5): print(out[i])
    
    def addpiece(self,piece):
        self.pieces[len(self.placed)//5][len(self.placed)%5] = piece
        self.placed.append(piece.id)
        if len(self.placed)==12: self.placed.append(0)
    
    def removepiece(self):
        if self.pieces[(len(self.placed)-1)//5][(len(self.placed)-1)%5].id == 0:
            self.pieces[(len(self.placed)-2)//5][(len(self.placed)-2)%5] = np.nan
            del self.placed[-1]
            del self.placed[-1]
        else:
            self.pieces[(len(self.placed)-1)//5][(len(self.placed)-1)%5] = np.nan
            del self.placed[-1]
    
    def plot(self,filename):
        combinations = [['black','white','orange','deeppink'],
                        ['black','white','deeppink','orange'],
                        ['black','orange','white','deeppink'],
                        ['black','orange','deeppink','white'],
                        ['black','deeppink','white','orange'],
                        ['black','deeppink','orange','white']]
        for colors in combinations:
            f,ax = plt.subplots(1,1,figsize=(5,5))
            ax.tick_params(length=0,labelsize=0)
            ax.set_xlim([0,10])
            ax.set_ylim([0,10])
            for i in [0,2,4,6,8,10]:
                ax.axvline(i,c='k',linewidth=2)
                ax.plot([0,10],[i,i],c='k',linewidth=2)
            for i in np.arange(len(self.placed)):
                row,col = [i//5,i%5]
                x = 2*col
                y = 10-2*row
                points = self.pieces[row][col].colors
                ax.scatter(x+.5,y-.5,c=colors[int(points[0][0])],marker='s',s=27**2)
                ax.scatter(x+1.5,y-.5,c=colors[int(points[0][1])],marker='s',s=27**2)
                ax.scatter(x+.5,y-1.5,c=colors[int(points[1][0])],marker='s',s=27**2)
                ax.scatter(x+1.5,y-1.5,c=colors[int(points[1][1])],marker='s',s=27**2)
            fname = filename.rstrip('.png')
            fname = fname+f'.C{combinations.index(colors)+1}.png'
            f.savefig(fname,bbox_inches='tight',pad_inches=.1)
            plt.close(f)

    def EdgeCheck(self,color):
        row,col = [len(self.placed)//5,len(self.placed)%5]
        behind,above = [False,False]
        if col>0:
            if self.pieces[row][col-1].colors[0][1]==color and self.pieces[row][col-1].colors[1][1]==color: behind = True
        if row>0:
            if self.pieces[row-1][col].colors[1][0]==color and self.pieces[row-1][col].colors[1][1]==color: above = True
        if above and behind:
            return(2)
        elif (above or behind):
            return(1)
        else:
            return(0)


def Check(board,piece):
    if piece.id in board.placed: return False
    row,col = [len(board.placed)//5,len(board.placed)%5]
    checkcol,checkrow = [False,False]
    current = piece.colors
    if col>0:
        behind = board.pieces[row][col-1].colors
        if behind[0][1]==current[0][0] and behind[1][1]==current[1][0]: checkcol = True
        if behind[0][1]==0 and behind[1][1]==0: checkcol = True     
    else: checkcol=True
    if row>0:
        above = board.pieces[row-1][col].colors
        if above[1][0]==current[0][0] and above[1][1]==current[0][1]: checkrow = True
        if above[1][0]==0 and above[1][1]==0: checkrow = True
    else: checkrow=True
    return(checkrow and checkcol)


def PlotTime(numarray,dt,filename):
    f,ax=plt.subplots(1,1,figsize=(7,5))
    ax.set_xlabel('Timestep',fontsize=15)
    ax.set_ylabel(r'N$_{options}$',fontsize=15)
    ax.set_xlim([0,24])
    ax.semilogy()
    ax2 = ax.twinx()
    ax2.semilogy()
    ax2.set_ylabel(r't$_{option}$ [s]',fontsize=15)
    tarr = np.array(dt)/np.array(numarray)
    x = np.arange(len(numarray))
    ax.plot(x,numarray,c='k',marker='o')
    #ax.scatter(x,numarray,c='k')
    ax2.plot(x+1,tarr,c='g',marker='o')
    #ax2.scatter(x[1:],tarr,c='g')
    f.savefig(filename,bbox_inches='tight',pad_inches=.1)


def LogUpdate(message,sp,clear=False):
    with open(f'Logs/Log.{sp[0]}.{sp[1]}.txt') as f:
        L = f.readlines()
    if clear: del L[-1]
    L.append(message)
    out = open(f'Logs/Log.{sp[0]}.{sp[1]}.txt','w')
    out.writelines(L)
    out.close()