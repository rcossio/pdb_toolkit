import sys
import os


# Ensure Modeller path is correctly appended
modeller_path = '/usr/lib/python3.10/dist-packages/'
sys.path.append(modeller_path)
from modeller import *
from modeller.automodel import *

# Set up environment
log.verbose()
env = Environ()
env.io.atom_files_directory = ['.', './pdb_files']

# Define file names
pdb_id = '3HR6'
pdb_file = f'{pdb_id}.pdb'

# Create a class for comparative modeling
class MyModel(automodel):
    def select_atoms(self):
        return selection(self.residue_range('1:A', '436:A'))

# Alignment
aln = alignment(env)
mdl = model(env, file=pdb_file)
aln.append_model(mdl, align_codes=pdb_id)
aln.append(file='sequence.ali', align_codes='target')
aln.align2d()

# Write the alignment file
aln.write(file='alignment.ali', alignment_format='PIR')

# Generate comparative model
a = MyModel(env, alnfile='alignment.ali', knowns=pdb_id, sequence='target')
a.starting_model = 1
a.ending_model = 1
a.make()

# Loop refinement
class MyLoop(loopmodel):
    def select_loop_atoms(self):
        return selection(self.residue_range('1:A', '436:A'))

a = MyLoop(env, alnfile='alignment.ali', knowns=pdb_id, sequence='target')
a.starting_model = 1
a.ending_model = 1
a.loop.starting_model = 1
a.loop.ending_model = 2
a.make()
