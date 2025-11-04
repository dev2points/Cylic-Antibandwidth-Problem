#!/bin/bash
TO="1800s"
mkdir -p results/$TO/complete_binary_trees
DATA_DIR="./graph/complete_binary_trees"
RESULT_DIR="./results/$TO/complete_binary_trees"

./runlim -r 1800 -s 30000 python3 model.py $DATA_DIR/cbt_30.txt 2>&1 | tee $RESULT_DIR/cbt_30.log
./runlim -r 1800 -s 30000 python3 model.py $DATA_DIR/cbt_31.txt 2>&1 | tee $RESULT_DIR/cbt_31.log
./runlim -r 1800 -s 30000 python3 model.py $DATA_DIR/cbt_32.txt 2>&1 | tee $RESULT_DIR/cbt_32.log
./runlim -r 1800 -s 30000 python3 model.py $DATA_DIR/cbt_33.txt 2>&1 | tee $RESULT_DIR/cbt_33.log
./runlim -r 1800 -s 30000 python3 model.py $DATA_DIR/cbt_34.txt 2>&1 | tee $RESULT_DIR/cbt_34.log
./runlim -r 1800 -s 30000 python3 model.py $DATA_DIR/cbt_35.txt 2>&1 | tee $RESULT_DIR/cbt_35.log
./runlim -r 1800 -s 30000 python3 model.py $DATA_DIR/cbt_45.txt 2>&1 | tee $RESULT_DIR/cbt_45.log
./runlim -r 1800 -s 30000 python3 model.py $DATA_DIR/cbt_46.txt 2>&1 | tee $RESULT_DIR/cbt_46.log
./runlim -r 1800 -s 30000 python3 model.py $DATA_DIR/cbt_47.txt 2>&1 | tee $RESULT_DIR/cbt_47.log
./runlim -r 1800 -s 30000 python3 model.py $DATA_DIR/cbt_48.txt 2>&1 | tee $RESULT_DIR/cbt_48.log
./runlim -r 1800 -s 30000 python3 model.py $DATA_DIR/cbt_49.txt 2>&1 | tee $RESULT_DIR/cbt_49.log
./runlim -r 1800 -s 30000 python3 model.py $DATA_DIR/cbt_50.txt 2>&1 | tee $RESULT_DIR/cbt_50.log
./runlim -r 1800 -s 30000 python3 model.py $DATA_DIR/cbt_500.txt 2>&1 | tee $RESULT_DIR/cbt_500.log
./runlim -r 1800 -s 30000 python3 model.py $DATA_DIR/cbt_510.txt 2>&1 | tee $RESULT_DIR/cbt_510.log
./runlim -r 1800 -s 30000 python3 model.py $DATA_DIR/cbt_550.txt 2>&1 | tee $RESULT_DIR/cbt_550.log
./runlim -r 1800 -s 30000 python3 model.py $DATA_DIR/cbt_600.txt 2>&1 | tee $RESULT_DIR/cbt_600.log
./runlim -r 1800 -s 30000 python3 model.py $DATA_DIR/cbt_620.txt 2>&1 | tee $RESULT_DIR/cbt_620.log
./runlim -r 1800 -s 30000 python3 model.py $DATA_DIR/cbt_630.txt 2>&1 | tee $RESULT_DIR/cbt_630.log
./runlim -r 1800 -s 30000 python3 model.py $DATA_DIR/cbt_640.txt 2>&1 | tee $RESULT_DIR/cbt_640.log
./runlim -r 1800 -s 30000 python3 model.py $DATA_DIR/cbt_730.txt 2>&1 | tee $RESULT_DIR/cbt_730.log
./runlim -r 1800 -s 30000 python3 model.py $DATA_DIR/cbt_790.txt 2>&1 | tee $RESULT_DIR/cbt_790.log
./runlim -r 1800 -s 30000 python3 model.py $DATA_DIR/cbt_880.txt 2>&1 | tee $RESULT_DIR/cbt_880.log
./runlim -r 1800 -s 30000 python3 model.py $DATA_DIR/cbt_910.txt 2>&1 | tee $RESULT_DIR/cbt_910.log
./runlim -r 1800 -s 30000 python3 model.py $DATA_DIR/cbt_950.txt 2>&1 | tee $RESULT_DIR/cbt_950.log
