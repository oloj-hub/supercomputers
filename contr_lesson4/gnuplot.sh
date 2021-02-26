set terminal png
set output "RDF.png"
plot for[plotname in "0 0.5 1.0 1.5 2.0"] "~/study/contr_lesson4/lj/temp_".plotname."/rdf.txt" using 2:3 w lp title plotname
set output "Temp.png"
plot 'Temp.txt' w lp title 'avr_temp'
