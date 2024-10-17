import os
import sys
from Bio import PDB
import subprocess

# Function to create Pymol script for alignment and RMSD calculation
def create_pymol_script(ref_pdb, target_pdb, pymol_script, chains):

    #from chains "ABC" convert to list ["chain A", "chain B", "chain C"]
    chains_string = " or ".join([f"chain {chain}" for chain in chains])

    with open(pymol_script, 'w') as script:
        script.write(f"""
load {ref_pdb}, ref
load {target_pdb}, target
align target and ({chains_string}), ref
rmsd = cmd.get_rms("target", "ref")
print("RMSD:", rmsd)
quit
""")

# Function to run Pymol script and get RMSD
def run_pymol_script(pymol_path, pymol_script):
    result = subprocess.run([pymol_path, '-cq', pymol_script], capture_output=True, text=True)
    return result.stdout

def main(ref_pdb_id, target_pdb_path,  pymol_path, chains):
    ref_pdb_filename = f"{ref_pdb_id}.pdb"

    pymol_script = 'align_and_rmsd.pml'
    create_pymol_script(ref_pdb_filename, target_pdb_path, pymol_script, chains)
    
    output = run_pymol_script(pymol_path, pymol_script)
    os.remove(pymol_script)
    
    print(output)

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Usage: python rmsd.py <ref_pdb_id> <target_pdb_path> <pymol_path> <chains>")
        sys.exit(1)

    ref_pdb_id = sys.argv[1]
    target_pdb_path = sys.argv[2]
    pymol_path = sys.argv[3]
    chains = sys.argv[4]

    main(ref_pdb_id, target_pdb_path, pymol_path, chains)
