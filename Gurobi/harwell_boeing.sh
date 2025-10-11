#!/bin/bash

mkdir -p results

runlim -r 1800 -s 30000 python3 model.py A-pores_1.mtx.rnd 2>&1 | tee results/harwell_boeing/A-pores_1-output.log
runlim -r 1800 -s 30000 python3 model.py B-ibm32.mtx.rnd 2>&1 | tee results/harwell_boeing/B-ibm32-output.log
runlim -r 1800 -s 30000 python3 model.py C-bcspwr01.mtx.rnd 2>&1 | tee results/harwell_boeing/C-bcspwr01-output.log
runlim -r 1800 -s 30000 python3 model.py D-bcsstk01.mtx.rnd 2>&1 | tee results/harwell_boeing/D-bcsstk01-output.log
runlim -r 1800 -s 30000 python3 model.py E-bcspwr02.mtx.rnd 2>&1 | tee results/harwell_boeing/E-bcspwr02-output.log
runlim -r 1800 -s 30000 python3 model.py F-curtis54.mtx.rnd 2>&1 | tee results/harwell_boeing/F-curtis54-output.log
runlim -r 1800 -s 30000 python3 model.py G-will57.mtx.rnd 2>&1 | tee results/harwell_boeing/G-will57-output.log
runlim -r 1800 -s 30000 python3 model.py H-impcol_b.mtx.rnd 2>&1 | tee results/harwell_boeing/H-impcol_b-output.log
runlim -r 1800 -s 30000 python3 model.py I-ash85.mtx.rnd 2>&1 | tee results/harwell_boeing/I-ash85-output.log
runlim -r 1800 -s 30000 python3 model.py J-nos4.mtx.rnd 2>&1 | tee results/harwell_boeing/J-nos4-output.log
runlim -r 1800 -s 30000 python3 model.py K-dwt__234.mtx.rnd 2>&1 | tee results/harwell_boeing/K-dwt__234-output.log
runlim -r 1800 -s 30000 python3 model.py L-bcspwr03.mtx.rnd 2>&1 | tee results/harwell_boeing/L-bcspwr03-output.log
runlim -r 1800 -s 30000 python3 model.py M-bcsstk06.mtx.rnd 2>&1 | tee results/harwell_boeing/M-bcsstk06-output.log
runlim -r 1800 -s 30000 python3 model.py N-bcsstk07.mtx.rnd 2>&1 | tee results/harwell_boeing/N-bcsstk07-output.log
runlim -r 1800 -s 30000 python3 model.py O-impcol_d.mtx.rnd 2>&1 | tee results/harwell_boeing/O-impcol_d-output.log
runlim -r 1800 -s 30000 python3 model.py P-can__445.mtx.rnd 2>&1 | tee results/harwell_boeing/P-can__445-output.log
runlim -r 1800 -s 30000 python3 model.py Q-494_bus.mtx.rnd 2>&1 | tee results/harwell_boeing/Q-494_bus-output.log
runlim -r 1800 -s 30000 python3 model.py R-dwt__503.mtx.rnd 2>&1 | tee results/harwell_boeing/R-dwt__503-output.log
runlim -r 1800 -s 30000 python3 model.py S-sherman4.mtx.rnd 2>&1 | tee results/harwell_boeing/S-sherman4-output.log
runlim -r 1800 -s 30000 python3 model.py T-dwt__592.mtx.rnd 2>&1 | tee results/harwell_boeing/T-dwt__592-output.log
runlim -r 1800 -s 30000 python3 model.py U-662_bus.mtx.rnd 2>&1 | tee results/harwell_boeing/U-662_bus-output.log
runlim -r 1800 -s 30000 python3 model.py V-nos6.mtx.rnd 2>&1 | tee results/harwell_boeing/V-nos6-output.log
runlim -r 1800 -s 30000 python3 model.py W-685_bus.mtx.rnd 2>&1 | tee results/harwell_boeing/W-685_bus-output.log
runlim -r 1800 -s 30000 python3 model.py X-can__715.mtx.rnd 2>&1 | tee results/harwell_boeing/X-can__715-output.log
