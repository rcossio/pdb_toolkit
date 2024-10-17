Requirements: pymol and biopython

To install biopython:

```bash
pip install biopython
```

Usage:
```bash
python rmsd.py <ref_pdb_id> <target_pdb_path> <pymol_path> <chains>
```

Example:

```bash
python rmsd.py 4cdh colabfold.pdb "/usr/pymol" "AB"
```
This will use chaind A and B from colabfold.pdb and align it to 4cdh using PyMOL.
