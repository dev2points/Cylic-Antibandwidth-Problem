#!/bin/bash
TO="1800s"
DATA_DIR="./graphs/hypercube"
LOG_DIR="./results/$TO/hypercube/log"
OUT_DIR="./results/$TO/hypercube/out"

mkdir -p "$LOG_DIR"    
mkdir -p "$OUT_DIR"

./runlim -r 1800 -s 30000 -o "$LOG_DIR/hypercube_4_16-runlim.log"   oplrun -l "$OUT_DIR/hypercube_4_16-output.out"   CP-CPLEX.mod "$DATA_DIR/hypercube_4_16.dat"
./runlim -r 1800 -s 30000 -o "$LOG_DIR/hypercube_5_32-runlim.log"   oplrun -l "$OUT_DIR/hypercube_5_32-output.out"   CP-CPLEX.mod "$DATA_DIR/hypercube_5_32.dat"
./runlim -r 1800 -s 30000 -o "$LOG_DIR/hypercube_6_64-runlim.log"   oplrun -l "$OUT_DIR/hypercube_6_64-output.out"   CP-CPLEX.mod "$DATA_DIR/hypercube_6_64.dat"
./runlim -r 1800 -s 30000 -o "$LOG_DIR/hypercube_7_128-runlim.log"  oplrun -l "$OUT_DIR/hypercube_7_128-output.out"  CP-CPLEX.mod "$DATA_DIR/hypercube_7_128.dat"
./runlim -r 1800 -s 30000 -o "$LOG_DIR/hypercube_8_256-runlim.log"  oplrun -l "$OUT_DIR/hypercube_8_256-output.out"  CP-CPLEX.mod "$DATA_DIR/hypercube_8_256.dat"
./runlim -r 1800 -s 30000 -o "$LOG_DIR/hypercube_9_512-runlim.log"  oplrun -l "$OUT_DIR/hypercube_9_512-output.out"  CP-CPLEX.mod "$DATA_DIR/hypercube_9_512.dat"
./runlim -r 1800 -s 30000 -o "$LOG_DIR/hypercube_10_1024-runlim.log" oplrun -l "$OUT_DIR/hypercube_10_1024-output.out" CP-CPLEX.mod "$DATA_DIR/hypercube_10_1024.dat"
