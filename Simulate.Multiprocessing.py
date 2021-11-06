import os,pickle,sys,time
import numpy as np 
from Scripts.GameClasses import *
from multiprocessing import Manager,Process,Pool
def myprint(string,clear=False):
    if clear:
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K") 
    print(string)
plotting = False

pieces = np.empty(24,dtype=object)
for i in np.arange(1,25):
    s = pickle.load(open(f'Scripts/Pieces/T{i:02d}.pickle','rb'))
    pieces[i-1] = s

edge_pieces = [[[6,10,13,18],[11,12,15]],[[4,13,14],[2,3,8]],[[14,17,18,20],[21,22,23]]]

loop = True
while loop:
    input_piece = int(input('Starting Piece [1-24]: '))
    if input_piece in range(1,25):
        input_position = int(input('Starting Position [1-4]: '))
        if input_position in range(1,pieces[input_piece-1].maxpos+1):
            loop = False
    if loop:
        retry = input('Invalid Starting Condition. Try again [y/n]: ')
        if retry not in ['y','Y','yes','Yes']: sys.exit()
loop = True
while loop:
    max_proc = int(input('Maximum Number of Processors to Use [1-12]: '))
    if max_proc in range(1,13): loop = False
    else: print('Invalid Input.')

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
    num_proc = len(old_chains) if len(old_chains)<max_proc else max_proc
    with Manager() as manager:
        new_chains = manager.list()
        def FindViable(chain):
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
        p = Pool(num_proc)
        p.map(FindViable,old_chains)
        new_chains = list(new_chains)
    t2 = time.time()
    dt.append(t2-t1)
    num_options.append(len(old_chains))
    myprint(f'T{timestep}: {len(old_chains)} chains analyzed in {round((t2-t1)/60,2)} minutes',clear=True)
    LogUpdate(f'T{timestep}: {len(old_chains)} chains analyzed in {round((t2-t1)/60,2)} minutes\n',starting_piece,clear=True)
    old_chains = new_chains
    timestep+=1
    if len(old_chains)==0: failed = True
    del new_chains

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

if len(old_chains)<1000: plotting = True
if plotting and not failed:
    print('Plotting solutions...')
    LogUpdate('Plotting solutions...\n',starting_piece)
    t1 = time.time()
    n = 1
    for chain in old_chains:
        board=Board()
        for step in np.arange(len(chain)):
            while not pieces[chain[step][0]-1].position == chain[step][1]:
                pieces[chain[step][0]-1].rotate()
            board.addpiece(pieces[chain[step][0]-1])
        board.plot(f'Plots/Board.{chain[0][0]}.{chain[0][1]}.{n}.png')
        n+=1
    t2 = time.time()
    myprint(f'Solutions Plotted in {round((t2-t1)/60,2)} minutes.',clear=True)
    LogUpdate(f'Solutions Plotted in {round((t2-t1)/60,2)} minutes.\n',starting_piece,clear=True)
