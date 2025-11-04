#!/bin/bash
TO="1800s"
mkdir -p results/$TO/double_star
DATA_DIR="./graph/double_star"
RESULT_DIR="./results/$TO/double_star"

./runlim -r 1800 -s 30000 python3 model.py $DATA_DIR/double_star_15_5.txt 2>&1 | tee $RESULT_DIR/double_star_15_5.log
./runlim -r 1800 -s 30000 python3 model.py $DATA_DIR/double_star_15_7.txt 2>&1 | tee $RESULT_DIR/double_star_15_7.log
./runlim -r 1800 -s 30000 python3 model.py $DATA_DIR/double_star_15_10.txt 2>&1 | tee $RESULT_DIR/double_star_15_10.log
./runlim -r 1800 -s 30000 python3 model.py $DATA_DIR/double_star_15_12.txt 2>&1 | tee $RESULT_DIR/double_star_15_12.log
./runlim -r 1800 -s 30000 python3 model.py $DATA_DIR/double_star_30_20.txt 2>&1 | tee $RESULT_DIR/double_star_30_20.log
./runlim -r 1800 -s 30000 python3 model.py $DATA_DIR/double_star_30_25.txt 2>&1 | tee $RESULT_DIR/double_star_30_25.log
./runlim -r 1800 -s 30000 python3 model.py $DATA_DIR/double_star_35_20.txt 2>&1 | tee $RESULT_DIR/double_star_35_20.log
./runlim -r 1800 -s 30000 python3 model.py $DATA_DIR/double_star_35_25.txt 2>&1 | tee $RESULT_DIR/double_star_35_25.log
./runlim -r 1800 -s 30000 python3 model.py $DATA_DIR/double_star_40_20.txt 2>&1 | tee $RESULT_DIR/double_star_40_20.log
./runlim -r 1800 -s 30000 python3 model.py $DATA_DIR/double_star_40_25.txt 2>&1 | tee $RESULT_DIR/double_star_40_25.log
./runlim -r 1800 -s 30000 python3 model.py $DATA_DIR/double_star_40_30.txt 2>&1 | tee $RESULT_DIR/double_star_40_30.log
./runlim -r 1800 -s 30000 python3 model.py $DATA_DIR/double_star_50_20.txt 2>&1 | tee $RESULT_DIR/double_star_50_20.log
./runlim -r 1800 -s 30000 python3 model.py $DATA_DIR/double_star_50_25.txt 2>&1 | tee $RESULT_DIR/double_star_50_25.log
./runlim -r 1800 -s 30000 python3 model.py $DATA_DIR/double_star_50_30.txt 2>&1 | tee $RESULT_DIR/double_star_50_30.log
./runlim -r 1800 -s 30000 python3 model.py $DATA_DIR/double_star_100_20.txt 2>&1 | tee $RESULT_DIR/double_star_100_20.log
./runlim -r 1800 -s 30000 python3 model.py $DATA_DIR/double_star_100_25.txt 2>&1 | tee $RESULT_DIR/double_star_100_25.log
./runlim -r 1800 -s 30000 python3 model.py $DATA_DIR/double_star_100_30.txt 2>&1 | tee $RESULT_DIR/double_star_100_30.log
./runlim -r 1800 -s 30000 python3 model.py $DATA_DIR/double_star_150_20.txt 2>&1 | tee $RESULT_DIR/double_star_150_20.log
./runlim -r 1800 -s 30000 python3 model.py $DATA_DIR/double_star_150_25.txt 2>&1 | tee $RESULT_DIR/double_star_150_25.log
./runlim -r 1800 -s 30000 python3 model.py $DATA_DIR/double_star_150_30.txt 2>&1 | tee $RESULT_DIR/double_star_150_30.log
