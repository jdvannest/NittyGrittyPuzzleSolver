import os,pickle

files = os.listdir('Successes')
n_complete = 0
n_solutions = 0

for f in files:
    if f.split('.')[0]=='Chains':
        n_complete+=1
        chains = pickle.load(open('Successes/'+f,'rb'))
        n_solutions+=len(chains)

if n_complete<14:
    print(f'{n_solutions} found after simulating {n_complete} initial conditions')
else:
    print(f'{n_solutions} exist')