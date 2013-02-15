set term postscript eps color 20
set pm3d map
set xlabel 'Word length'
set ylabel 'Frecuency of zeros'
set title 'Average porcentage of correct transmitions'
set output 'channel.eps'
splot 'channel.dat' using 1:2:($3*100)
