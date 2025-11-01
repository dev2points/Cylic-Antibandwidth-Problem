#!/bin/bash

mkdir -p results/hypercube
DATA_DIR="./graph/hypercube"
RESULT_DIR="./results/hypercube"

./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/hypercube_4_16.txt 2>&1 | tee $RESULT_DIR/hypercube_4_16.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/hypercube_5_32.txt 2>&1 | tee $RESULT_DIR/hypercube_5_32.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/hypercube_6_64.txt 2>&1 | tee $RESULT_DIR/hypercube_6_64.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/hypercube_7_128.txt 2>&1 | tee $RESULT_DIR/hypercube_7_128.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/hypercube_8_256.txt 2>&1 | tee $RESULT_DIR/hypercube_8_256.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/hypercube_9_512.txt 2>&1 | tee $RESULT_DIR/hypercube_9_512.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/hypercube_10_1024.txt 2>&1 | tee $RESULT_DIR/hypercube_10_1024.log


