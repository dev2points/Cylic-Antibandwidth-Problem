#!/bin/bash
TO="150s"
mkdir -p results/$TO/3dmesh
DATA_DIR="./graph/3dmesh"
RESULT_DIR="./results/$TO/3dmesh"

./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/3dmesh_2_2_3.txt 2>&1 | tee $RESULT_DIR/3dmesh_2_2_3.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/3dmesh_2_2_168.txt 2>&1 | tee $RESULT_DIR/3dmesh_2_2_168.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/3dmesh_2_2_335.txt 2>&1 | tee $RESULT_DIR/3dmesh_2_2_335.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/3dmesh_2_2_500.txt 2>&1 | tee $RESULT_DIR/3dmesh_2_2_500.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/3dmesh_3_3_3.txt 2>&1 | tee $RESULT_DIR/3dmesh_3_3_3.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/3dmesh_3_3_135.txt 2>&1 | tee $RESULT_DIR/3dmesh_3_3_135.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/3dmesh_3_3_270.txt 2>&1 | tee $RESULT_DIR/3dmesh_3_3_270.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/3dmesh_3_3_400.txt 2>&1 | tee $RESULT_DIR/3dmesh_3_3_400.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/3dmesh_4_4_5.txt 2>&1 | tee $RESULT_DIR/3dmesh_4_4_5.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/3dmesh_4_4_68.txt 2>&1 | tee $RESULT_DIR/3dmesh_4_4_68.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/3dmesh_4_4_137.txt 2>&1 | tee $RESULT_DIR/3dmesh_4_4_137.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/3dmesh_4_4_200.txt 2>&1 | tee $RESULT_DIR/3dmesh_4_4_200.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/3dmesh_5_5_7.txt 2>&1 | tee $RESULT_DIR/3dmesh_5_5_7.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/3dmesh_5_5_35.txt 2>&1 | tee $RESULT_DIR/3dmesh_5_5_35.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/3dmesh_5_5_70.txt 2>&1 | tee $RESULT_DIR/3dmesh_5_5_70.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/3dmesh_5_5_100.txt 2>&1 | tee $RESULT_DIR/3dmesh_5_5_100.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/3dmesh_6_6_8.txt 2>&1 | tee $RESULT_DIR/3dmesh_6_6_8.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/3dmesh_6_6_36.txt 2>&1 | tee $RESULT_DIR/3dmesh_6_6_36.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/3dmesh_6_6_72.txt 2>&1 | tee $RESULT_DIR/3dmesh_6_6_72.log
./runlim -r 150 -s 30000 python3 model_MIP_CPLEX.py $DATA_DIR/3dmesh_6_6_100.txt 2>&1 | tee $RESULT_DIR/3dmesh_6_6_100.log

