if [ "$#" -ne 2 ]; then
    echo "Usage: create.sh [input file name] [output file name (no extension)]>"
    exit
fi

cd jgr
make
cd ../

IN=$1
OUT=$2

python parse.py $IN > temp.jgr
./jgr/jgraph -P temp.jgr | ps2pdf - $OUT.pdf