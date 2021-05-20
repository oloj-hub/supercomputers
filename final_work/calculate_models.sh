#!/bin/bash

mkdir lj

for diam in 2.0 2.5 3.0 3.5 4.0;
do
	cd ~/study/final_work
	mkdir lj/diam_$diam
	cd ~/study/final_work/lj/diam_$diam
	cp ~/study/final_work/in.shear.void ./
	cp ~/study/final_work/Ni_u3.eam ./
	sed "s/YYYYTEMP/$diam/g" in.shear.void > in.shear.void$diam
	rm in.shear.void
	srun -N 1 --ntasks-per-node=8 -J lammps_kalinichev --comment="Lammps melting" -p RT ~/bin/lmp_mpi -in in.shear.void$diam
done


cd ~/study/final_work

for diam in 2.0 2.5 3.0 3.5 4.0;
do
avr=$(awk -f awk.sh lj/diam_$diam/log.lammps)
echo "$avr" >> lj/diam_$diam/Eng.txt
done

cd ~/study/final_work

for diam in 2.0 2.5 3.0 3.5 4.0;
do
tail -n 50 lj/diam_$diam/tmp.rdf >> lj/diam_$diam/rdf.txt
done

cd ~/study/final_work

gnuplot gnuplot.sh

token=1677496628:AAEEavk7MpcbNTwOC0SE0whKNMwOVV-ZG7w
id=460001441
curl -s -X POST "https://api.telegram.org/bot${token}/sendPhoto?chat_id=${id}" -F photo="@ENG.png" -F caption="ENG(time)"

               
