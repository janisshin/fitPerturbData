#!/bin/bash 

# This script generates the mass action equation for each reaction in an antimony file. 
# input file is an antimony file with a .py extension 

# need to first create a file listing all enzymes
# sed -n '/Reactions/,/Species initializations/{//!p;}' putida_shikimate_clean.py > tmp.txt
# while IFS= read -r line
# do
#    echo "$line" | cut -d \: -f 1 >> enzymes.txt
# done < tmp.txt
# rm tmp.txt

antimony_file="$1"

if [[ -e rateLaws.list ]]; then rm rateLaws.list; fi

# extract all the reactions to form a list of reactions
IFS=$'\n'
reactions=($(sed -n '/Reactions/,/Species initializations/{//!p;}' "$antimony_file")) 
unset IFS

for lineA in "${reactions[@]}"
do 
	if [[ ! "$lineA" = *"#"*  ]] # if lineA is not commented out
	then
		# pare down the line to just the reaction equation
		reaction=`echo "$lineA" | cut -d \: -f 1 | cut -c 5- ` 
		equation=`echo "$lineA" | cut -d \: -f 2 | cut -d \; -f 1`
		reactants=`echo "$equation" | awk -F '-> || => ' '{print $1}'`

		# pare down the line to just the product equation
		products=`echo "$equation" | awk -F '-> || => ' '{print $2}'`

		# send reactant part of equation to Python for writing into mass action equation
		python3 _MM-writer.py "$reactants" "$products"

	fi
done < enzymes.txt