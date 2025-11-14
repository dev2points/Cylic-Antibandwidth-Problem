#!/bin/bash
TO="1800s"
mkdir -p results/$TO/random_generated_graph_2013
DATA_DIR="./graphs/random_generated_graph_2013"
RESULT_DIR="./results/$TO/random_generated_graph_2013"

./runlim -r 1800 -s 30000 python3  model.py $DATA_DIR/p1_100_200  2>&1 | tee $RESULT_DIR/p1_100_200.log
./runlim -r 1800 -s 30000 python3  model.py $DATA_DIR/p2_100_200  2>&1 | tee $RESULT_DIR/p2_100_200.log
./runlim -r 1800 -s 30000 python3  model.py $DATA_DIR/p3_100_200  2>&1 | tee $RESULT_DIR/p3_100_200.log
./runlim -r 1800 -s 30000 python3  model.py $DATA_DIR/p4_100_200  2>&1 | tee $RESULT_DIR/p4_100_200.log
./runlim -r 1800 -s 30000 python3  model.py $DATA_DIR/p5_100_200  2>&1 | tee $RESULT_DIR/p5_100_200.log
./runlim -r 1800 -s 30000 python3  model.py $DATA_DIR/p6_100_200  2>&1 | tee $RESULT_DIR/p6_100_200.log
./runlim -r 1800 -s 30000 python3  model.py $DATA_DIR/p7_100_200  2>&1 | tee $RESULT_DIR/p7_100_200.log
./runlim -r 1800 -s 30000 python3  model.py $DATA_DIR/p8_100_200  2>&1 | tee $RESULT_DIR/p8_100_200.log
./runlim -r 1800 -s 30000 python3  model.py $DATA_DIR/p9_100_200  2>&1 | tee $RESULT_DIR/p9_100_200.log
./runlim -r 1800 -s 30000 python3  model.py $DATA_DIR/p10_100_200  2>&1 | tee $RESULT_DIR/p10_100_200.log
./runlim -r 1800 -s 30000 python3  model.py $DATA_DIR/p11_100_600  2>&1 | tee $RESULT_DIR/p11_100_600.log
./runlim -r 1800 -s 30000 python3  model.py $DATA_DIR/p12_100_600  2>&1 | tee $RESULT_DIR/p12_100_600.log
./runlim -r 1800 -s 30000 python3  model.py $DATA_DIR/p13_100_600  2>&1 | tee $RESULT_DIR/p13_100_600.log
./runlim -r 1800 -s 30000 python3  model.py $DATA_DIR/p14_100_600  2>&1 | tee $RESULT_DIR/p14_100_600.log
./runlim -r 1800 -s 30000 python3  model.py $DATA_DIR/p15_100_600  2>&1 | tee $RESULT_DIR/p15_100_600.log
./runlim -r 1800 -s 30000 python3  model.py $DATA_DIR/p16_100_600  2>&1 | tee $RESULT_DIR/p16_100_600.log
./runlim -r 1800 -s 30000 python3  model.py $DATA_DIR/p17_100_600  2>&1 | tee $RESULT_DIR/p17_100_600.log
./runlim -r 1800 -s 30000 python3  model.py $DATA_DIR/p18_100_600  2>&1 | tee $RESULT_DIR/p18_100_600.log
./runlim -r 1800 -s 30000 python3  model.py $DATA_DIR/p19_100_600  2>&1 | tee $RESULT_DIR/p19_100_600.log
./runlim -r 1800 -s 30000 python3  model.py $DATA_DIR/p20_100_600  2>&1 | tee $RESULT_DIR/p20_100_600.log
./runlim -r 1800 -s 30000 python3  model.py $DATA_DIR/p21_200_400  2>&1 | tee $RESULT_DIR/p21_200_400.log
./runlim -r 1800 -s 30000 python3  model.py $DATA_DIR/p22_200_400  2>&1 | tee $RESULT_DIR/p22_200_400.log
./runlim -r 1800 -s 30000 python3  model.py $DATA_DIR/p23_200_400  2>&1 | tee $RESULT_DIR/p23_200_400.log
./runlim -r 1800 -s 30000 python3  model.py $DATA_DIR/p24_200_400  2>&1 | tee $RESULT_DIR/p24_200_400.log
./runlim -r 1800 -s 30000 python3  model.py $DATA_DIR/p25_200_400  2>&1 | tee $RESULT_DIR/p25_200_400.log
./runlim -r 1800 -s 30000 python3  model.py $DATA_DIR/p26_200_400  2>&1 | tee $RESULT_DIR/p26_200_400.log
./runlim -r 1800 -s 30000 python3  model.py $DATA_DIR/p27_200_400  2>&1 | tee $RESULT_DIR/p27_200_400.log
./runlim -r 1800 -s 30000 python3  model.py $DATA_DIR/p28_200_400  2>&1 | tee $RESULT_DIR/p28_200_400.log
./runlim -r 1800 -s 30000 python3  model.py $DATA_DIR/p29_200_400  2>&1 | tee $RESULT_DIR/p29_200_400.log
./runlim -r 1800 -s 30000 python3  model.py $DATA_DIR/p30_200_400  2>&1 | tee $RESULT_DIR/p30_200_400.log
./runlim -r 1800 -s 30000 python3  model.py $DATA_DIR/p31_200_2000  2>&1 | tee $RESULT_DIR/p31_200_2000.log
./runlim -r 1800 -s 30000 python3  model.py $DATA_DIR/p32_200_2000  2>&1 | tee $RESULT_DIR/p32_200_2000.log
./runlim -r 1800 -s 30000 python3  model.py $DATA_DIR/p33_200_2000  2>&1 | tee $RESULT_DIR/p33_200_2000.log
./runlim -r 1800 -s 30000 python3  model.py $DATA_DIR/p34_200_2000  2>&1 | tee $RESULT_DIR/p34_200_2000.log
./runlim -r 1800 -s 30000 python3  model.py $DATA_DIR/p35_200_2000  2>&1 | tee $RESULT_DIR/p35_200_2000.log
./runlim -r 1800 -s 30000 python3  model.py $DATA_DIR/p36_200_2000  2>&1 | tee $RESULT_DIR/p36_200_2000.log
./runlim -r 1800 -s 30000 python3  model.py $DATA_DIR/p37_200_2000  2>&1 | tee $RESULT_DIR/p37_200_2000.log
./runlim -r 1800 -s 30000 python3  model.py $DATA_DIR/p38_200_2000  2>&1 | tee $RESULT_DIR/p38_200_2000.log
./runlim -r 1800 -s 30000 python3  model.py $DATA_DIR/p39_200_2000  2>&1 | tee $RESULT_DIR/p39_200_2000.log
./runlim -r 1800 -s 30000 python3  model.py $DATA_DIR/p40_200_2000  2>&1 | tee $RESULT_DIR/p40_200_2000.log
