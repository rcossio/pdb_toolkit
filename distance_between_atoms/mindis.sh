res=141
for file in /sdb-disk/lbugnon/CdSrtA_results/rosettaRelax/fc_k${res}/relax/*/*pdb
do 
	./dist.sh $file SG 222 A NZ $res C
done
