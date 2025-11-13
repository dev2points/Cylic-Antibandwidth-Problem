import os
import sys
import argparse

def convert_graph_format(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"❌ Không tìm thấy file: {filename}")
        return

    # Bỏ dòng đầu tiên (Nombre del problema: ...)
    header = lines[0]
    data_lines = lines[1:]

    # Dòng chứa thông tin số đỉnh và cạnh
    parts = data_lines[0].split()
    num_vertices = int(parts[0])
    num_edges = int(parts[1]) if len(parts) > 1 else 0

    # Các dòng còn lại là danh sách cạnh
    edge_lines = data_lines[1:]
    edges = []
    for line in edge_lines:
        u, v = map(int, line.split())
        edges.append(f"<{u}, {v}>")

    # Tạo nội dung file .dat
    result = []
    result.append(f"num_vertices = {num_vertices};")
    result.append(f"num_edges = {len(edges)};")
    result.append("edges = {")
    for e in edges:
        result.append(f"    {e},")
    if result[-1].endswith(","):
        result[-1] = result[-1][:-1]  # bỏ dấu phẩy cuối
    result.append("};")

    # Tạo thư mục đầu ra dựa vào loại đồ thị (vd: 3dmesh_2_2_3.txt -> 3dmesh/)
    base = os.path.basename(filename)
    # graph_type = base.split("_")[0]
    graph_type = "random_generated_graph_2013"
    out_dir = os.path.join(".", graph_type)
    os.makedirs(out_dir, exist_ok=True)

    # Tạo tên file .dat đầu ra
    name_no_ext = os.path.splitext(base)[0]
    out_path = os.path.join(out_dir, f"{name_no_ext}.dat")

    # Ghi ra file .dat
    with open(out_path, "w", encoding="utf-8") as out:
        out.write("\n".join(result) + "\n")

    print(f"✅ Đã chuyển đổi {filename} ➜ {out_path}")


def main():
    parser = argparse.ArgumentParser(description="Chuyển file đồ thị sang định dạng .dat")
    parser.add_argument("input_file", type=str, help="Đường dẫn đến file đầu vào (.txt)")
    args = parser.parse_args()

    convert_graph_format(args.input_file)


if __name__ == "__main__":
    main()
