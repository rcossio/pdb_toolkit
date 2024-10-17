import Bio.PDB as bpdb
from Bio import SeqIO
import pandas as pd
from datetime import datetime
import os

import argparse 
parser = argparse.ArgumentParser(description="Crop PDB around a position of interest")
parser.add_argument("--out_path", type=str, help="Output folder")
parser.add_argument("--prot", default="data/5k9a.pdb", type=str, help="Path to protein pdb")
parser.add_argument("--position", type=int, help="Position to center the crop")
parser.add_argument("--context", type=int, default=2, help="Number of AA at each side of the position of interest")
parser.add_argument("--chain", type=str, default="A", help="Chain containing the position of interest")
args = parser.parse_args()

position = args.position
PDB = args.prot
context = args.context
chain_id = args.chain

out_path = args.out_path
if not out_path:
    out_path = "results/" + str(datetime.today()).replace(" ", "_")

if os.path.isdir(out_path):
    print(f"Output folder {out_path} already exists.")
else:
    os.makedirs(out_path)

protname = PDB.split("/")[-1][:-4]

class ResSelect(bpdb.Select):
    def accept_residue(self, res):
        if res.id[1] >= start_res and res.id[1] <= end_res and res.parent.id == chain_id:
            return True
        else:
            return False

s = bpdb.PDBParser().get_structure("Query", f'{PDB}')

start_res = max(0,position-context)
end_res = min(position+context,len(s[0][chain_id]))

io = bpdb.PDBIO()
io.set_structure(s)

io.save(f'{out_path}/{protname}_{position}.pdb', ResSelect())
