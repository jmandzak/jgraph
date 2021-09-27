cd jgr
make
cd ../




python parse.py $IN > temp.jgr
./jgr/jgraph -P temp.jgr | ps2pdf - $OUT.pdf