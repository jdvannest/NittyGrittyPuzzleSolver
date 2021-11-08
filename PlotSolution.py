import os,pickle,sys,time
import numpy as np 
from Scripts.GameClasses import *

pieces = np.empty(24,dtype=object)
for i in np.arange(1,25):
    s = pickle.load(open(f'Scripts/Pieces/T{i:02d}.pickle','rb'))
    pieces[i-1] = s

valid_starts = [(1,1),(2,1),(2,2),(2,3),(2,4),(4,1),(4,2),
                (4,3),(4,4),(5,1),(5,2),(8,1),(13,1),(13,2)]

loop = True
while loop:
    input_piece = int(input('Starting Tile: '))
    if input_piece in  [1,2,4,5,8,13]:
        input_position = int(input('Starting Rotation: '))
        if (input_piece,input_position) in valid_starts:
            loop = False
    if loop:
        retry = input('Invalid Starting Condition. Try again [y/n]: ')
        if retry not in ['y','Y','yes','Yes']: sys.exit()

try:
    chains = pickle.load(open(f'Successes/Chains.{input_piece}.{input_position}.pickle','rb'))
except:
    print("No file exists.\nEither this initial condition hasn't been simulated or there are no possible solutions")
    sys.exit(0)

print(f'{len(chains)} Solutions with initial piece ({input_piece},{input_position})')
loop = True
while loop:
    solution_id = int(input(f'Solution Number to plot [1-{len(chains)}]: '))
    if solution_id in range(1,len(chains)+1): loop = False
    else:
        retry = input('Invalid Entry. Try again [y/n]: ')
        if retry not in ['y','Y','yes','Yes']: sys.exit()

chain = chains[solution_id-1]
board = Board()
for piece in chain:
    while not pieces[piece[0]-1].position == piece[1]:
        pieces[piece[0]-1].rotate()
    board.addpiece(pieces[piece[0]-1])
board.plot(f'Plots/Board.{input_piece}.{input_position}.{solution_id}.png')
print(f'Plots written to Plots/Board.{input_piece}.{input_position}.{solution_id}')