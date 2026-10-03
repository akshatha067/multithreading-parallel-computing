import matplotlib.pyplot as plt

# ==========================================
# EXPERIMENT DATA
# ==========================================

threads = [1, 2, 4, 6, 16]

sequential_time = 2.965359

pthread_time = [
    3.009574,
    1.481584,
    0.924759,
    0.652311,
    0.413948
]

omp_time = [
    2.922494,
    1.483852,
    0.937276,
    0.652948,
    0.395491
]

# ==========================================
# SPEEDUP
# Speedup = Sequential Time / Parallel Time
# ==========================================

pthread_speedup = [
    sequential_time / t
    for t in pthread_time
]

omp_speedup = [
    sequential_time / t
    for t in omp_time
]

# ==========================================
# EFFICIENCY
# Efficiency = Speedup / Number of Threads
# ==========================================

pthread_efficiency = [
    (s / n) * 100
    for s, n in zip(pthread_speedup, threads)
]

omp_efficiency = [
    (s / n) * 100
    for s, n in zip(omp_speedup, threads)
]

# ==========================================
# GRAPH 1: EXECUTION TIME
# ==========================================

plt.figure(figsize=(8, 5))

plt.plot(
    threads,
    pthread_time,
    marker='o',
    label='Pthreads'
)

plt.plot(
    threads,
    omp_time,
    marker='s',
    label='OpenMP'
)

plt.xlabel('Number of Threads')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time vs Number of Threads')

plt.xticks(threads)
plt.grid(True)
plt.legend()

plt.tight_layout()

plt.savefig(
    'graphs/execution_time_vs_threads.png',
    dpi=300
)

plt.close()

# ==========================================
# GRAPH 2: SPEEDUP
# ==========================================

plt.figure(figsize=(8, 5))

plt.plot(
    threads,
    pthread_speedup,
    marker='o',
    label='Pthreads'
)

plt.plot(
    threads,
    omp_speedup,
    marker='s',
    label='OpenMP'
)

plt.xlabel('Number of Threads')
plt.ylabel('Speedup (x)')
plt.title('Speedup vs Number of Threads')

plt.xticks(threads)
plt.grid(True)
plt.legend()

plt.tight_layout()

plt.savefig(
    'graphs/speedup_vs_threads.png',
    dpi=300
)

plt.close()

# ==========================================
# GRAPH 3: EFFICIENCY
# ==========================================

plt.figure(figsize=(8, 5))

plt.plot(
    threads,
    pthread_efficiency,
    marker='o',
    label='Pthreads'
)

plt.plot(
    threads,
    omp_efficiency,
    marker='s',
    label='OpenMP'
)

plt.xlabel('Number of Threads')
plt.ylabel('Efficiency (%)')
plt.title('Efficiency vs Number of Threads')

plt.xticks(threads)
plt.grid(True)
plt.legend()

plt.tight_layout()

plt.savefig(
    'graphs/efficiency_vs_threads.png',
    dpi=300
)

plt.close()

print("Graphs generated successfully.")
