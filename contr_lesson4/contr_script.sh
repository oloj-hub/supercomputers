#!/bin/bash

mkdir lj

for temp in 0 0.5 1.0 1.5 2.0;
do
	cd ~/study/contr_lesson4
	mkdir lj/temp_$temp
	cd ~/study/contr_lesson4/lj/temp_$temp
	cp ~/study/contr_lesson4/in.melt ./
	sed "s/YYYYTEMP/$temp/g" in.melt > in.melt$temp
	rm in.melt
	srun -N 1 --ntasks-per-node=8 -J lammps_kalinichev --comment="Lammps melting" -p RT ~/bin/lmp_mpi -in in.melt$temp
done

cd ~/study/contr_lesson4

echo "#Temp_initial Temp_average" > Temp.txt

for temp in 0 0.5 1.0 1.5 2.0;
do
avr=$(awk -f awk.sh lj/temp_$temp/log.lammps)
echo "$temp $avr" >> Temp.txt
done

cd ~/study/contr_lesson4

for temp in 0 0.5 1.0 1.5 2.0;
do
tail -n 50 lj/temp_$temp/tmp.rdf >> lj/temp_$temp/rdf.txt
done

cd ~/study/contr_lesson4

gnuplot gnuplot.sh

curl -s -X POST https://api.telegram.org/bot1677496628:AAEEavk7MpcbNTwOC0SE0whKNMwOVV-ZG7w/sendMessage -d chat_id=460001441 -d text="server calculate smt"
               
