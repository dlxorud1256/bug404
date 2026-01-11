import csv
import sys


import os

# 스크립트 파일이 있는 디렉토리를 기준으로 경로 설정
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JTL_FILE = os.path.join(BASE_DIR, "result_300.jtl")


latencies = []
errors = 0
total = 0

with open(JTL_FILE, newline='', encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        total += 1
        latency = int(row["elapsed"])
        latencies.append(latency)

        if row["success"] != "true":
            errors += 1



error_rate = errors / total * 100
latencies.sort()
p95 = latencies[int(len(latencies) * 0.95)] if latencies else 0

print(f"Total: {total}")
print(f"Error Rate: {error_rate:.2f}%")
print(f"P95 Latency: {p95:.2f} ms")

# ---- FAIL 조건 ----
if error_rate >= 1:
    print("❌ FAIL: Error rate too high")
    sys.exit(1)

if p95 >= 2000:
    print("❌ FAIL: P95 latency too high")
    sys.exit(1)

print("✅ PASS")
