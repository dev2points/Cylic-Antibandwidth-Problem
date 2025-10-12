#!/bin/bash

DATA_DIR="./graphs/harwell_boeing"
RESULT_DIR="./results/harwell_boeing"

mkdir -p $RESULT_DIR

./runlim -r 1800 -s 30000 -o $RESULT_DIR/A-pores_1.log oplrun -deploy CP-CPLEX.mod $DATA_DIR/A-pores_1.dat
./runlim -r 1800 -s 30000 -o $RESULT_DIR/B-ibm32.log oplrun -deploy CP-CPLEX.mod $DATA_DIR/B-ibm32.dat
./runlim -r 1800 -s 30000 -o $RESULT_DIR/C-bcspwr01.log oplrun -deploy CP-CPLEX.mod $DATA_DIR/C-bcspwr01.dat
./runlim -r 1800 -s 30000 -o $RESULT_DIR/D-bcsstk01.log oplrun -deploy CP-CPLEX.mod $DATA_DIR/D-bcsstk01.dat
./runlim -r 1800 -s 30000 -o $RESULT_DIR/E-bcspwr02.log oplrun -deploy CP-CPLEX.mod $DATA_DIR/E-bcspwr02.dat
./runlim -r 1800 -s 30000 -o $RESULT_DIR/F-curtis54.log oplrun -deploy CP-CPLEX.mod $DATA_DIR/F-curtis54.dat
./runlim -r 1800 -s 30000 -o $RESULT_DIR/G-will57.log oplrun -deploy CP-CPLEX.mod $DATA_DIR/G-will57.dat
./runlim -r 1800 -s 30000 -o $RESULT_DIR/H-impcolb.log oplrun -deploy CP-CPLEX.mod $DATA_DIR/H-impcolb.dat
./runlim -r 1800 -s 30000 -o $RESULT_DIR/I-ash85.log oplrun -deploy CP-CPLEX.mod $DATA_DIR/I-ash85.dat
./runlim -r 1800 -s 30000 -o $RESULT_DIR/J-nos4.log oplrun -deploy CP-CPLEX.mod $DATA_DIR/J-nos4.dat
./runlim -r 1800 -s 30000 -o $RESULT_DIR/K-dwt__234.log oplrun -deploy CP-CPLEX.mod $DATA_DIR/K-dwt__234.dat
./runlim -r 1800 -s 30000 -o $RESULT_DIR/L-bcspwr03.log oplrun -deploy CP-CPLEX.mod $DATA_DIR/L-bcspwr03.dat
./runlim -r 1800 -s 30000 -o $RESULT_DIR/M-bcsstk06.log oplrun -deploy CP-CPLEX.mod $DATA_DIR/M-bcsstk06.dat
./runlim -r 1800 -s 30000 -o $RESULT_DIR/N-bcsstk07.log oplrun -deploy CP-CPLEX.mod $DATA_DIR/N-bcsstk07.dat
./runlim -r 1800 -s 30000 -o $RESULT_DIR/O-impcol_d.log oplrun -deploy CP-CPLEX.mod $DATA_DIR/O-impcol_d.dat
./runlim -r 1800 -s 30000 -o $RESULT_DIR/P-can__445.log oplrun -deploy CP-CPLEX.mod $DATA_DIR/P-can__445.dat
./runlim -r 1800 -s 30000 -o $RESULT_DIR/Q-494_bus.log oplrun -deploy CP-CPLEX.mod $DATA_DIR/Q-494_bus.dat
./runlim -r 1800 -s 30000 -o $RESULT_DIR/R-dwt__503.log oplrun -deploy CP-CPLEX.mod $DATA_DIR/R-dwt__503.dat
./runlim -r 1800 -s 30000 -o $RESULT_DIR/S-sherman4.log oplrun -deploy CP-CPLEX.mod $DATA_DIR/S-sherman4.dat
./runlim -r 1800 -s 30000 -o $RESULT_DIR/T-dwt__592.log oplrun -deploy CP-CPLEX.mod $DATA_DIR/T-dwt__592.dat
./runlim -r 1800 -s 30000 -o $RESULT_DIR/U-662_bus.log oplrun -deploy CP-CPLEX.mod $DATA_DIR/U-662_bus.dat
./runlim -r 1800 -s 30000 -o $RESULT_DIR/V-nos6.log oplrun -deploy CP-CPLEX.mod $DATA_DIR/V-nos6.dat
./runlim -r 1800 -s 30000 -o $RESULT_DIR/W-685_bus.log oplrun -deploy CP-CPLEX.mod $DATA_DIR/W-685_bus.dat
./runlim -r 1800 -s 30000 -o $RESULT_DIR/X-can__715.log oplrun -deploy CP-CPLEX.mod $DATA_DIR/X-can__715.dat
