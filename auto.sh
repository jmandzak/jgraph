cd jgr
make
cd ../

for VARIABLE in examples/ex1 examples/ex2 examples/ex3 examples/ex4 examples/ex5
do
    python parse.py $VARIABLE.txt > temp.jgr
    ./jgr/jgraph -P temp.jgr | ps2pdf - $VARIABLE.pdf
done