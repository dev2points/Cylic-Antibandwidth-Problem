
#!/bin/bash
TO="150s"
mkdir -p results/$TO/harwell_boeing
DATA_DIR="./graph/harwell_boeing"
RESULT_DIR="./results/$TO/harwell_boeing"

./runlim -r 150 -s 30000 python3 model.py $DATA_DIR/A-pores_1.mtx.rnd 2>&1 | tee $RESULT_DIR/A-pores_1.log
./runlim -r 150 -s 30000 python3 model.py $DATA_DIR/B-ibm32.mtx.rnd 2>&1 | tee $RESULT_DIR/B-ibm32.log
./runlim -r 150 -s 30000 python3 model.py $DATA_DIR/C-bcspwr01.mtx.rnd 2>&1 | tee $RESULT_DIR/C-bcspwr01.log
./runlim -r 150 -s 30000 python3 model.py $DATA_DIR/D-bcsstk01.mtx.rnd 2>&1 | tee $RESULT_DIR/D-bcsstk01.log
./runlim -r 150 -s 30000 python3 model.py $DATA_DIR/E-bcspwr02.mtx.rnd 2>&1 | tee $RESULT_DIR/E-bcspwr02.log
./runlim -r 150 -s 30000 python3 model.py $DATA_DIR/F-curtis54.mtx.rnd 2>&1 | tee $RESULT_DIR/F-curtis54.log
./runlim -r 150 -s 30000 python3 model.py $DATA_DIR/G-will57.mtx.rnd 2>&1 | tee $RESULT_DIR/G-will57.log
./runlim -r 150 -s 30000 python3 model.py $DATA_DIR/H-impcol_b.mtx.rnd 2>&1 | tee $RESULT_DIR/H-impcol_b.log
./runlim -r 150 -s 30000 python3 model.py $DATA_DIR/I-ash85.mtx.rnd 2>&1 | tee $RESULT_DIR/I-ash85.log
./runlim -r 150 -s 30000 python3 model.py $DATA_DIR/J-nos4.mtx.rnd 2>&1 | tee $RESULT_DIR/J-nos4.log
./runlim -r 150 -s 30000 python3 model.py $DATA_DIR/K-dwt__234.mtx.rnd 2>&1 | tee $RESULT_DIR/K-dwt__234.log
./runlim -r 150 -s 30000 python3 model.py $DATA_DIR/L-bcspwr03.mtx.rnd 2>&1 | tee $RESULT_DIR/L-bcspwr03.log
./runlim -r 150 -s 30000 python3 model.py $DATA_DIR/M-bcsstk06.mtx.rnd 2>&1 | tee $RESULT_DIR/M-bcsstk06.log
./runlim -r 150 -s 30000 python3 model.py $DATA_DIR/N-bcsstk07.mtx.rnd 2>&1 | tee $RESULT_DIR/N-bcsstk07.log
./runlim -r 150 -s 30000 python3 model.py $DATA_DIR/O-impcol_d.mtx.rnd 2>&1 | tee $RESULT_DIR/O-impcol_d.log
./runlim -r 150 -s 30000 python3 model.py $DATA_DIR/P-can__445.mtx.rnd 2>&1 | tee $RESULT_DIR/P-can__445.log
./runlim -r 150 -s 30000 python3 model.py $DATA_DIR/Q-494_bus.mtx.rnd 2>&1 | tee $RESULT_DIR/Q-494_bus.log
./runlim -r 150 -s 30000 python3 model.py $DATA_DIR/R-dwt__503.mtx.rnd 2>&1 | tee $RESULT_DIR/R-dwt__503.log
./runlim -r 150 -s 30000 python3 model.py $DATA_DIR/S-sherman4.mtx.rnd 2>&1 | tee $RESULT_DIR/S-sherman4.log
./runlim -r 150 -s 30000 python3 model.py $DATA_DIR/T-dwt__592.mtx.rnd 2>&1 | tee $RESULT_DIR/T-dwt__592.log
./runlim -r 150 -s 30000 python3 model.py $DATA_DIR/U-662_bus.mtx.rnd 2>&1 | tee $RESULT_DIR/U-662_bus.log
./runlim -r 150 -s 30000 python3 model.py $DATA_DIR/V-nos6.mtx.rnd 2>&1 | tee $RESULT_DIR/V-nos6.log
./runlim -r 150 -s 30000 python3 model.py $DATA_DIR/W-685_bus.mtx.rnd 2>&1 | tee $RESULT_DIR/W-685_bus.log
./runlim -r 150 -s 30000 python3 model.py $DATA_DIR/X-can__715.mtx.rnd 2>&1 | tee $RESULT_DIR/X-can__715.log