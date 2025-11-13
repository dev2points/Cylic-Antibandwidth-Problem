#!/bin/bash


DATA_DIR="./graph/hypercube"


./runlim python3 convert.py $DATA_DIR/hypercube_4_16.txt 
./runlim python3 convert.py $DATA_DIR/hypercube_5_32.txt 
./runlim python3 convert.py $DATA_DIR/hypercube_6_64.txt 
./runlim python3 convert.py $DATA_DIR/hypercube_7_128.txt 
./runlim python3 convert.py $DATA_DIR/hypercube_8_256.txt 
./runlim python3 convert.py $DATA_DIR/hypercube_9_512.txt 
./runlim python3 convert.py $DATA_DIR/hypercube_10_1024.txt 


