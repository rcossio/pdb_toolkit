

res=76
size=5
rm -r cut_peps/res${res}_size$size
python3 getFragmentPDB.py --prot 4CDH.pdb --position $res --chain A --context $size --out_path cut_peps/res${res}_size$size 



