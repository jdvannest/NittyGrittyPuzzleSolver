import os,pickle,sys,time
import numpy as np 
from Scripts.GameClasses import *
def myprint(string,clear=False):
    if clear:
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K") 
    print(string)

pieces = np.empty(24,dtype=object)
for i in np.arange(1,25):
    s = pickle.load(open(f'Scripts/Pieces/T{i:02d}.pickle','rb'))
    pieces[i-1] = s

edge_pieces = [[[6,10,13,18],[11,12,15]],[[4,13,14],[2,3,8]],[[14,17,18,20],[21,22,23]]]
valid_starts = [(1,1),(2,1),(2,2),(2,3),(2,4),(4,1),(4,2),
                (4,3),(4,4),(5,1),(5,2),(8,1),(13,1),(13,2)]

loop = True
while loop:
    input_piece = int(input('Starting Tile: '))
    if input_piece in [1,2,4,5,8,13]:
        input_position = int(input('Starting Rotation: '))
        if (input_piece,input_position) in valid_starts:
            loop = False
    if loop:
        retry = input('Invalid Starting Condition. Try again [y/n]: ')
        if retry not in ['y','Y','yes','Yes']: sys.exit()

starting_piece = (input_piece,input_position)
start = time.time()

try:
    log = open(f'Logs/Log.{starting_piece[0]}.{starting_piece[1]}.txt')
    log.close()
    os.system(f'rm Logs/Log.{starting_piece[0]}.{starting_piece[1]}.txt')
except:
    pass
os.system(f'touch Logs/Log.{starting_piece[0]}.{starting_piece[1]}.txt')

old_chains = [[starting_piece]]
num_options,dt = [[],[]]

timestep,failed = [1,False]
while timestep<24 and not failed:
    print(f'T{timestep}: Analyzing {len(old_chains)} chains...')
    LogUpdate(f'T{timestep}: Analyzing {len(old_chains)} chains...\n',starting_piece)
    t1 = time.time()
    new_chains = []
    for chain in old_chains:
        board = Board()
        for step in np.arange(len(chain)):
            while not pieces[chain[step][0]-1].position == chain[step][1]:
                pieces[chain[step][0]-1].rotate()
            board.addpiece(pieces[chain[step][0]-1])
        for piece in pieces:
            for rot in np.arange(piece.maxpos):
                piece.rotate()
                if Check(board,piece):
                    board.addpiece(piece)
                    available_edge = True
                    for color in [1,2,3]:
                        val = board.EdgeCheck(color)
                        if val>0:
                            if all(x in board.placed for x in edge_pieces[color-1][val-1]): available_edge = False
                    if available_edge:
                        new_chains.append(chain+[(piece.id,piece.position)])
                    board.removepiece()              
    t2 = time.time()
    dt.append(t2-t1)
    num_options.append(len(old_chains))
    myprint(f'T{timestep}: {len(old_chains)} chains analyzed in {round((t2-t1)/60,2)} minutes',clear=True)
    LogUpdate(f'T{timestep}: {len(old_chains)} chains analyzed in {round((t2-t1)/60,2)} minutes\n',starting_piece,clear=True)
    old_chains = new_chains
    timestep+=1
    if len(old_chains)==0: failed = True

stop = time.time()
print(f'Total computation time: {round((stop-start)/3600,2)} hrs')
print(f'{len(old_chains)} solutions found starting with {starting_piece}')
LogUpdate(f'Total computation time: {round((stop-start)/3600,2)} hrs\n'+
        f'{len(old_chains)} solutions found starting with {starting_piece}\n',starting_piece)
if not failed: 
    out = open(f'Successes/Chains.{old_chains[0][0][0]}.{old_chains[0][0][1]}.pickle','wb')
    pickle.dump(old_chains,out)
    out.close()
PlotTime(num_options,dt,f'Plots/dt.{starting_piece[0]}.{starting_piece[1]}.png')