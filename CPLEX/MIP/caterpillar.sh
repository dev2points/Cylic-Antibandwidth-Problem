#!/bin/bash
TO="150s"
mkdir -p results/$TO/caterpillar
DATA_DIR="./graph/caterpillar"
RESULT_DIR="./results/$TO/caterpillar"

./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/caterpillar_5_4.txt 2>&1 | tee $RESULT_DIR/caterpillar_5_4.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/caterpillar_5_5.txt 2>&1 | tee $RESULT_DIR/caterpillar_5_5.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/caterpillar_5_6.txt 2>&1 | tee $RESULT_DIR/caterpillar_5_6.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/caterpillar_5_7.txt 2>&1 | tee $RESULT_DIR/caterpillar_5_7.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/caterpillar_9_4.txt 2>&1 | tee $RESULT_DIR/caterpillar_9_4.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/caterpillar_9_5.txt 2>&1 | tee $RESULT_DIR/caterpillar_9_5.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/caterpillar_9_6.txt 2>&1 | tee $RESULT_DIR/caterpillar_9_6.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/caterpillar_9_7.txt 2>&1 | tee $RESULT_DIR/caterpillar_9_7.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/caterpillar_10_4.txt 2>&1 | tee $RESULT_DIR/caterpillar_10_4.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/caterpillar_10_5.txt 2>&1 | tee $RESULT_DIR/caterpillar_10_5.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/caterpillar_10_6.txt 2>&1 | tee $RESULT_DIR/caterpillar_10_6.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/caterpillar_10_7.txt 2>&1 | tee $RESULT_DIR/caterpillar_10_7.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/caterpillar_15_4.txt 2>&1 | tee $RESULT_DIR/caterpillar_15_4.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/caterpillar_15_5.txt 2>&1 | tee $RESULT_DIR/caterpillar_15_5.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/caterpillar_15_6.txt 2>&1 | tee $RESULT_DIR/caterpillar_15_6.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/caterpillar_15_7.txt 2>&1 | tee $RESULT_DIR/caterpillar_15_7.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/caterpillar_20_4.txt 2>&1 | tee $RESULT_DIR/caterpillar_20_4.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/caterpillar_20_5.txt 2>&1 | tee $RESULT_DIR/caterpillar_20_5.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/caterpillar_20_6.txt 2>&1 | tee $RESULT_DIR/caterpillar_20_6.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/caterpillar_20_7.txt 2>&1 | tee $RESULT_DIR/caterpillar_20_7.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/caterpillar_20_10.txt 2>&1 | tee $RESULT_DIR/caterpillar_20_10.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/caterpillar_20_15.txt 2>&1 | tee $RESULT_DIR/caterpillar_20_15.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/caterpillar_20_20.txt 2>&1 | tee $RESULT_DIR/caterpillar_20_20.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/caterpillar_20_25.txt 2>&1 | tee $RESULT_DIR/caterpillar_20_25.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/caterpillar_25_10.txt 2>&1 | tee $RESULT_DIR/caterpillar_25_10.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/caterpillar_25_15.txt 2>&1 | tee $RESULT_DIR/caterpillar_25_15.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/caterpillar_25_20.txt 2>&1 | tee $RESULT_DIR/caterpillar_25_20.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/caterpillar_25_25.txt 2>&1 | tee $RESULT_DIR/caterpillar_25_25.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/caterpillar_30_10.txt 2>&1 | tee $RESULT_DIR/caterpillar_30_10.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/caterpillar_30_15.txt 2>&1 | tee $RESULT_DIR/caterpillar_30_15.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/caterpillar_30_20.txt 2>&1 | tee $RESULT_DIR/caterpillar_30_20.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/caterpillar_30_25.txt 2>&1 | tee $RESULT_DIR/caterpillar_30_25.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/caterpillar_35_10.txt 2>&1 | tee $RESULT_DIR/caterpillar_35_10.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/caterpillar_35_15.txt 2>&1 | tee $RESULT_DIR/caterpillar_35_15.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/caterpillar_35_20.txt 2>&1 | tee $RESULT_DIR/caterpillar_35_20.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/caterpillar_35_25.txt 2>&1 | tee $RESULT_DIR/caterpillar_35_25.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/caterpillar_40_10.txt 2>&1 | tee $RESULT_DIR/caterpillar_40_10.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/caterpillar_40_15.txt 2>&1 | tee $RESULT_DIR/caterpillar_40_15.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/caterpillar_40_20.txt 2>&1 | tee $RESULT_DIR/caterpillar_40_20.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/caterpillar_40_25.txt 2>&1 | tee $RESULT_DIR/caterpillar_40_25.log
