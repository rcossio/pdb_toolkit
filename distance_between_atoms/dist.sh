#!/bin/bash

file=$1
atom1=$2
resid1=$3
chain1=$4
atom2=$5
resid2=$6
chain2=$7

if [ $# -ne 7 ]; then
    echo "Last update: 03/jul/2024"
    echo "Usage: ./$0 <file> <atomname1> <resid1> <chain1> <atomname2> <resid2> <chain2>"
    echo "Example: ./$0 1a2k.pdb CA 10 A CB 20 B"
    exit 1
fi

echo -n "File: $file  "
awk -v atom1="$atom1" -v resid1="$resid1" -v chain1="$chain1" -v atom2="$atom2" -v resid2="$resid2" -v chain2="$chain2"  '{
if ($1 == "ATOM" && $3 == atom1 && $5 == chain1 && $6+0 == resid1) {
        xA=$7; yA=$8; zA=$9
        resname1=$4
    } else if ($1 == "ATOM" && $3 == atom2 && $5 == chain2 && $6+0 == resid2) {
        xB=$7; yB=$8; zB=$9
        resname2=$4
    }
} END {
    dist = sqrt((xA-xB)^2 + (yA-yB)^2 + (zA-zB)^2)
    printf "Distance %3s%i %3s%i : %.3f\n", resname1, resid1, resname2, resid2, dist
}' $file

