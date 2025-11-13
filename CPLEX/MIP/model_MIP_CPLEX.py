import cplex
from cplex.exceptions import CplexSolverError
import time
import threading
import argparse
import psutil
import os
from memory_profiler import memory_usage
import math
from func_timeout import func_timeout, FunctionTimedOut

cabw_bounds = {
    "A-pores_1.mtx.rnd": (3, 8),
    "B-ibm32.mtx.rnd": (5, 9),
    "C-bcspwr01.mtx.rnd": (8, 17),
    "D-bcsstk01.mtx.rnd": (4, 9),
    "E-bcspwr02.mtx.rnd": (11, 22),
    "F-curtis54.mtx.rnd": (6, 13),
    "G-will57.mtx.rnd": (6, 14),
    "H-impcol_b.mtx.rnd": (4, 8),
    "I-ash85.mtx.rnd": (10, 27),
    "J-nos4.mtx.rnd": (16, 40),
    "K-dwt__234.mtx.rnd": (23, 58),
    "L-bcspwr03.mtx.rnd": (20, 39),
    "M-bcsstk06.mtx.rnd": (14, 72),
    "N-bcsstk07.mtx.rnd": (14, 72),
    "O-impcol_d.mtx.rnd": (46, 173),
    "P-can__445.mtx.rnd": (39, 120),
    "Q-494_bus.mtx.rnd": (110, 246),
    "R-dwt__503.mtx.rnd": (23, 71),
    "S-sherman4.mtx.rnd": (128, 272),
    "T-dwt__592.mtx.rnd": (52, 150),
    "U-662_bus.mtx.rnd": (110, 220),
    "V-nos6.mtx.rnd": (163, 337),
    "W-685_bus.mtx.rnd": (68, 136),
    "X-can__715.mtx.rnd": (56, 142),

    "3dmesh_2_2_3.txt": (2, 4),
    "3dmesh_2_2_168.txt": (2, 334),
    "3dmesh_2_2_335.txt": (2, 668),
    "3dmesh_2_2_500.txt": (2, 998),
    "3dmesh_3_3_3.txt": (2, 9),
    "3dmesh_3_3_135.txt": (2, 603),
    "3dmesh_3_3_270.txt": (2, 1211),
    "3dmesh_3_3_400.txt": (2, 1796),
    "3dmesh_4_4_5.txt": (2, 32),
    "3dmesh_4_4_68.txt": (2, 536),
    "3dmesh_4_4_137.txt": (2, 1088),
    "3dmesh_4_4_200.txt": (2, 1592),
    "3dmesh_5_5_7.txt": (2, 74),
    "3dmesh_5_5_35.txt": (2, 424),
    "3dmesh_5_5_70.txt": (2, 862),
    "3dmesh_5_5_100.txt": (2, 1237),
    "3dmesh_6_6_8.txt": (2, 125),
    "3dmesh_6_6_36.txt": (2, 629),
    "3dmesh_6_6_72.txt": (2, 1277),
    "3dmesh_6_6_100.txt": (2, 1781),

    "hypercube_4_16.txt": (2, 4),
    "hypercube_5_32.txt": (5, 9),
    "hypercube_6_64.txt": (10, 19),
    "hypercube_7_128.txt": (21, 41),
    "hypercube_8_256.txt": (43, 85),
    "hypercube_9_512.txt": (89, 178),
    "hypercube_10_1024.txt": (182, 364),

    "double_star_15_5.txt" :(2,3),
    "double_star_15_7.txt" :(2,4),
    "double_star_15_10.txt" :(2,5),
    "double_star_15_12.txt" :(2,6),
    "double_star_30_20.txt" :(2,10),
    "double_star_30_25.txt" :(2,13),
    "double_star_35_20.txt" :(2,10),
    "double_star_35_25.txt" :(2,13),
    "double_star_40_20.txt":( 2,10),
    "double_star_40_25.txt" :(2,13),
    "double_star_40_30.txt":( 2,15),
    "double_star_50_20.txt" :(2,10),
    "double_star_50_25.txt":( 2,13),
    "double_star_50_30.txt" :(2,15),
    "double_star_100_20.txt" :(2,10),
    "double_star_100_25.txt":( 2,13),
    "double_star_100_30.txt" :(2,15),
    "double_star_150_20.txt" :(2,10),
    "double_star_150_25.txt":( 2,13),
    "double_star_150_30.txt":( 2,15),

    "caterpillar_5_4.txt":(2, 20),
    "caterpillar_5_5.txt":(2, 25),
    "caterpillar_5_6.txt":(2, 30),
    "caterpillar_5_7.txt":(2, 35),
    "caterpillar_9_4.txt":(2,36),
    "caterpillar_9_5.txt":(2,45),
    "caterpillar_9_6.txt":(2,54),
    "caterpillar_9_7.txt":(2,63),
    "caterpillar_10_4.txt":(2,40),
    "caterpillar_10_5.txt":(2,50),
    "caterpillar_10_6.txt":(2,60),
    "caterpillar_10_7.txt":(2,70),
    "caterpillar_15_4.txt":(2,60),
    "caterpillar_15_5.txt":(2,75),
    "caterpillar_15_6.txt":(2,90),
    "caterpillar_15_7.txt":(2,105),
    "caterpillar_20_4.txt":(2,80),
    "caterpillar_20_5.txt":(2,100),
    "caterpillar_20_6.txt":(2,120),
    "caterpillar_20_7.txt":(2,140),
    "caterpillar_20_10.txt":(2,200),
    "caterpillar_20_15.txt":(2,300),
    "caterpillar_20_20.txt":(2,400),
    "caterpillar_20_25.txt":(2,500),
    "caterpillar_25_10.txt":(2,250),
    "caterpillar_25_15.txt":(2,375),
    "caterpillar_25_20.txt":(2,500),
    "caterpillar_25_25.txt":(2,625),
    "caterpillar_30_10.txt":(2,300),
    "caterpillar_30_15.txt":(2,450),
    "caterpillar_30_20.txt":(2,600),
    "caterpillar_30_25.txt":(2,750),
    "caterpillar_35_10.txt":(2,350),
    "caterpillar_35_15.txt":(2,525),
    "caterpillar_35_20.txt":(2,700),
    "caterpillar_35_25.txt":(2,875),
    "caterpillar_40_10.txt":(2,400),
    "caterpillar_40_15.txt":(2,600),
    "caterpillar_40_20.txt":(2,80),
    "caterpillar_40_25.txt":(2,1000),

    

    "cbt_30.txt" : (2,30),
    "cbt_31.txt" : (2,31),
    "cbt_32.txt" : (2,32),
    "cbt_33.txt" : (2,33),
    "cbt_34.txt" : (2,34),
    "cbt_35.txt" : (2,35),
    "cbt_45.txt" : (2,45),
    "cbt_46.txt" : (2,46),
    "cbt_47.txt" : (2,47),
    "cbt_48.txt" : (2,48),
    "cbt_49.txt" : (2,49),
    "cbt_50.txt" : (2,50),
    "cbt_500.txt" : (2,500),
    "cbt_510.txt" : (2,510),
    "cbt_550.txt" : (2,550),
    "cbt_600.txt" : (2,600),
    "cbt_620.txt" : (2,620),
    "cbt_630.txt" : (2,630),
    "cbt_640.txt" : (2,640),
    "cbt_730.txt" : (2,730),
    "cbt_790.txt" : (2,790),
    "cbt_880.txt" : (2,880),
    "cbt_910.txt" : (2,910),
    "cbt_950.txt" : (2,950),

    "p1_100_200" : (2, 100),
    "p2_100_200" : (2, 100),
    "p3_100_200" : (2, 100),
    "p4_100_200" : (2, 100),
    "p5_100_200" : (2, 100),
    "p6_100_200" : (2, 100),
    "p7_100_200" : (2, 100),
    "p8_100_200" : (2, 100),
    "p9_100_200" : (2, 100),
    "p10_100_200" : (2, 100),
    "p11_100_600" : (2, 100),
    "p12_100_600" : (2, 100),
    "p13_100_600" : (2, 100),
    "p14_100_600" : (2, 100),
    "p15_100_600" : (2, 100),
    "p16_100_600" : (2, 100),
    "p17_100_600" : (2, 100),
    "p18_100_600" : (2, 100),
    "p19_100_600" : (2, 100),
    "p20_100_600" : (2, 100),
    "p21_200_400" : (2, 200),
    "p22_200_400" : (2, 200),
    "p23_200_400" : (2, 200),
    "p24_200_400" : (2, 200),
    "p25_200_400" : (2, 200),
    "p26_200_400" : (2, 200),
    "p27_200_400" : (2, 200),
    "p28_200_400" : (2, 200),
    "p29_200_400" : (2, 200),
    "p30_200_400" : (2, 200),
    "p31_200_2000" : (2, 200),
    "p32_200_2000" : (2, 200),
    "p33_200_2000" : (2, 200),
    "p34_200_2000" : (2, 200),
    "p35_200_2000" : (2, 200),
    "p36_200_2000" : (2, 200),
    "p37_200_2000" : (2, 200),
    "p38_200_2000" : (2, 200),
    "p39_200_2000" : (2, 200),
    "p40_200_2000" : (2, 200),



}

def calculate_label_differences(labels, edges):
  label_differences = []
  for edge in edges:
    v1, v2 = edge
    label_difference = abs(labels[v1-1] - labels[v2-1])  
    label_differences.append(label_difference)
  return label_differences

class ContextTimer(object):
    def __init__(self, msg):
        self.msg = msg
        self.start = 0
        self.process = psutil.Process()
        self.start_memory = 0
        self.running = True
        
    def __enter__(self):
        self.start = time.time()
        self.start_memory = self.process.memory_info().rss
        print('--> begin {0}'.format(self.msg))
        self.thread = threading.Thread(target=self.print_time_elapsed)
        self.thread.start()
        return self  # return value is value of with ()
        
    def __exit__(self, *args):
        self.running = False
        self.thread.join()
        elapsed = time.time() - self.start
        self.msecs = math.ceil(1000 * elapsed)
        print('----- end {0},  time: {1:.0f} ms'.format(self.msg, self.msecs))

    def print_time_elapsed(self):
        while self.running:
            elapsed = time.time() - self.start
            current_memory = self.process.memory_info().rss
            memory_used = current_memory - self.start_memory
            memory_used_mb = memory_used / (1024 * 1024)
            if memory_used_mb < 0:
                memory_used_mb = 0  # Đặt giá trị bộ nhớ âm thành 0
            print(f"Time has passed: {elapsed:.2f} s, Memory used: {memory_used_mb:.2f} MB", end='\r')
            time.sleep(1)

def build_model(vertices, edges, k, time_limit=1800):
    """
    Xây dựng mô hình MIP cho bài toán antibandwidth theo dạng (FE(k))

    Args:
        vertices: Danh sách các đỉnh
        edges: Danh sách các cạnh (cặp đỉnh)
        k: Khoảng cách tối thiểu giữa các nhãn

    Returns:
        Mô hình MIP dưới dạng đối tượng cplex.Cplex
    """
    # Số đỉnh
    n = len(vertices) 
    
    # Tạo tham số cho mô hình
    model = cplex.Cplex()
    model.parameters.timelimit.set(time_limit)
    model.parameters.clocktype.set(2)
    model.parameters.workmem.set(30000)
    model.parameters.simplex.pgradient.set(4)
    model.parameters.mip.strategy.file.set(3)
    model.parameters.mip.display.set(0) 

    model.set_results_stream(None)   # kết quả
    model.set_log_stream(None)       # log chi tiết (presolve, branch)
    model.set_warning_stream(None)   # cảnh báo
    model.set_error_stream(None)     # lỗi (có thể None nếu muốn)
    
    # Tạo biến quyết định
    var_names = [f"x_{i}_{l}" for i in vertices for l in vertices]
    model.variables.add(names=var_names, types=['B'] * len(var_names))

    rows = []
    rhs = []
    senses = []
    names = []
    
    # Ràng buộc 1: Mỗi đỉnh được gán đúng một nhãn
    for i in vertices:
        indices = [var_names[(i-1)*n + l-1] for l in vertices]
        coefficients = [1] * n
        rows.append((indices, coefficients))
        rhs.append(1)
        senses.append('E')
        names.append(f"VERTICES_{i}")
    
    # Ràng buộc 2: Mỗi nhãn được gán cho đúng một đỉnh
    for l in range(1, n + 1):
        indices = [var_names[(i-1)*n + l-1] for i in vertices]
        coefficients = [1] * n
        rows.append((indices, coefficients))
        rhs.append(1)
        senses.append('E')
        names.append(f"LABELS_{l}")
    
    # Ràng buộc OBJ-k: Không được gán nhãn quá gần nhau cho các đỉnh kề nhau
    for (i, j) in edges:
        for l2 in range(n - k):
            indices = [var_names[(i-1)*n + l] for l in range(l2, l2 + k + 1)] + \
                    [var_names[(j-1)*n + l] for l in range(l2, l2 + k + 1)]
            coefficients = [1] * (2 * (k + 1))
            rows.append((indices, coefficients))
            rhs.append(1)
            senses.append('L')
            names.append(f"NO_CLOSE_LABELS_{i}_{j}_{l2}")
            
    # --- Ràng buộc Cyclic: nối 2 đầu chu trình
    for (i, j) in edges:
        for l2 in range(n - k, n): 
            indices_i = []
            indices_j = []
            # Lấy các nhãn liên tiếp (l2, l2+1, ..., n-1, 0, 1, ...)
            for offset in range(k + 1):
                l = (l2 + offset) % n  
                indices_i.append(var_names[(i - 1) * n + l])
                indices_j.append(var_names[(j - 1) * n + l])
            indices = indices_i + indices_j
            coefficients = [1] * (2 * (k + 1))
            rows.append((indices, coefficients))
            rhs.append(1)
            senses.append('L')
            names.append(f"CYCLIC_NO_CLOSE_{i}_{j}_{l2}")
    # Tính độ đo của các đỉnh
    degree = {i: 0 for i in vertices}
    for (i, j) in edges:
        degree[i] += 1
        degree[j] += 1

    # Tìm đỉnh có độ đo lớn nhất
    max_degree_vertex = max(degree, key=degree.get)
    
    # Ràng buộc phá vỡ đối xứng
    for l in range((n // 2) + 1, n + 1):
        indices = [var_names[(max_degree_vertex-1)*n + l-1]]
        coefficients = [1]
        rows.append((indices, coefficients))
        rhs.append(0)
        senses.append('L')
        names.append(f"SYMMETRY_BREAK_{max_degree_vertex}_{l}")

    # Add constraints in batch
    model.linear_constraints.add(
        lin_expr=rows,
        senses=senses,
        rhs=rhs,
        names=names
    )

    return model



def solve_Cyclicantibandwidth(vertices, edges, UB, LB):
    """
    Giải bài toán antibandwidth sử dụng mô hình (FE(k))

    Args:
        vertices: Danh sách các đỉnh
        edges: Danh sách các cạnh (cặp đỉnh)

    Returns:
        Giá trị k lớn nhất thỏa mãn (FE(k))
    """
    k = LB + 1
    # k = 1
    labels = [None] * len(vertices)
    while True:
        print(f"(w = {k + 1}) Building and Solving")
        if k >= UB:
            print(f"w = {k + 1} larger upper bounds")
            print(f"Final result: CAB = {k}")
            print(f"Labels = {labels}")
            break
        
        model = build_model(vertices, edges, k)
        
        try:
            model.solve()
            solution = model.solution
            status = solution.get_status_string()
        except CplexSolverError as e:
            print(f"Error: {e}")
            break
        
        #print("Status of solution: ", status)
        
        if not solution.is_primal_feasible():
            print(f"Cannot find soluion with w = {k + 1}")
            print(f"Final result: CAB = {k}")
            print(f"Labels = {labels}")
            break
        
        var_values = solution.get_values()
        for i in range(len(vertices)):
            for l in range(len(vertices)):
                if var_values[i * len(vertices) + l] > 0.5:
                    labels[i] = l + 1  
                    break
                
        print(f"Value Cyclic-Antibandwidth: {k+1}")
        print("Labels:", labels)
        
        # Kiểm tra xem có phải bài toán antibandwidth
        label_differences = calculate_label_differences(labels, edges)
        if any(element < k + 1 for element in label_differences):
            print("Uncorrect solution")
        else :
            print("Correct solution")
        k += 1
    return k, labels

def read_mtx_rnd_file(file_path):
    edges = set()

    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Bỏ qua dòng đầu tiên mô tả
    size_info = lines[1].strip().split()
    num_vertices = int(size_info[0])  # Số đỉnh
    file_name = os.path.basename(file_path)
    LB, UB = cabw_bounds[file_name]
    # Đọc các cạnh từ các dòng tiếp theo
    for line in lines[2:]:
        row, col = map(int, line.strip().split())
        edges.add((row, col))
    
    return num_vertices, list(edges), UB, LB

def run_with_timeout_and_memory(vertices, edges, timeout, UB, LB):
    try:
         with ContextTimer("Time and memory usage"):
            # Đo bộ nhớ sử dụng của hàm solve_antibandwidth với giới hạn thời gian
            mem_usage = memory_usage((func_timeout, (timeout, solve_Cyclicantibandwidth), {'args': (vertices, edges, UB, LB)}))
            print(f"Memory used: {max(mem_usage) - min(mem_usage):.2f} MB")
    except FunctionTimedOut:
        print(f"Function solve_Cyclic-Antibandwidth has timed out {timeout} s")

def main():
    #Đọc dữ liệu đầu vào từ tệp .mtx.rnd
    parser = argparse.ArgumentParser(description='Giải bài toán cyclic antibandwidth trên đồ thị.')
    parser.add_argument('input_file', type=str, help='Đường dẫn đến tệp đầu vào chứa dữ liệu đồ thị .')
    args = parser.parse_args()
    
    num_vertices, edges, UB, LB = read_mtx_rnd_file(args.input_file)
    vertices = list(range(1, num_vertices+1))  # Danh sách các đỉnh từ 1 đến 48
    timeout = 1800  # Thời gian giới hạn 1800 giây
    
    #run_with_timeout_and_memory(vertices, edges, timeout, UB, LB)
    solve_Cyclicantibandwidth(vertices, edges, UB, LB)
    
if __name__ == "__main__":
    main()
