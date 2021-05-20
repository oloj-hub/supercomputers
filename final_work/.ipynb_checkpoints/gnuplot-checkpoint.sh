set terminal png
set output "RDF.png"
plot for[plotname in "2.0 2.5 3.0 3.5 4.0"] "~/study/final_work/lj/diam_".plotname."/rdf.txt" using 2:3 w lp title plotname
set output "ENG.png"
plot for[plotname in "2.0 2.5 3.0 3.5 4.0"] "~/study/final_work/lj/diam_".plotname."/Eng.txt" using 1:2 w lp title plotname
set output "Temp.png"
plot 'Temp.txt' w lp title 'avr_temp'
