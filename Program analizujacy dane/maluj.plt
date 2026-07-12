set terminal postscript eps enhanced solid lw 2.2 color font "Helvetica,22"
set out "wykres.eps"
set xlabel "Lata" font "Helvetica,22"
set ylabel "Liczba zgonow" font "Helvetica,22"
set boxwidth 0.7 relative
set style fill solid 0.8
plot 'wykres.txt' u 1:2 w boxes lc rgb '#2342ba' title '' 
