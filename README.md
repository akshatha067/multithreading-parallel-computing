# Multithreaded Programming Using Pthreads and OpenMP

## Experiment

**Develop Multithreaded Programs Using Parallel Programming Libraries to Understand Thread Creation, Management, and Coordination**

---

## 1. Aim

To develop multithreaded programs using **Pthreads and OpenMP** and understand:

- Thread creation
- Thread management
- Work distribution
- Race conditions
- Synchronization
- Thread coordination
- Performance improvement using multiple threads

---

## 2. Objective

This experiment demonstrates how multiple threads can be used to perform work concurrently.

Two parallel programming approaches are implemented:

1. **Pthreads (POSIX Threads)** — provides explicit control over thread creation, management, joining, and synchronization.
2. **OpenMP** — provides a higher-level approach to parallel programming using compiler directives.

The experiment progresses from basic thread creation to work distribution, race conditions, synchronization, coordination, and performance analysis.

---

## 3. Software Environment

The experiment was implemented using:

- Windows
- WSL Ubuntu
- GCC 15.2.0
- Pthreads
- OpenMP
- C programming language
- Nano editor

---


## Performance Graphs

### 1. Execution Time vs Number of Threads

<img src="graphs/execution_time_vs_threads.png" alt="Execution Time vs Number of Threads" width="700">

### 2. Speedup vs Number of Threads

<img src="graphs/speedup_vs_threads.png" alt="Speedup vs Number of Threads" width="700">

### 3. Efficiency vs Number of Threads

<img src="graphs/efficiency_vs_threads.png" alt="Efficiency vs Number of Threads" width="700">

---

## 4. Repository Structure

```text
multithreading-parallel-computing/
│
├── README.md
│
├── src/
│   ├── sequential.c
│   ├── thread1.c
│   ├── thread2.c
│   ├── thread_sum.c
│   ├── race.c
│   ├── mutex.c
│   ├── pthread_perf.c
│   ├── omp1.c
│   ├── omp_sum.c
│   ├── omp_race.c
│   ├── omp_critical.c
│   ├── omp_barrier.c
│   └── omp_perf.c
│
├── data/
│   └── .gitkeep
│
├── results/
│   └── timings.csv
│
├── graphs/
│   ├── plot_graphs.py
│   ├── execution_time_vs_threads.png
│   ├── speedup_vs_threads.png
│   └── efficiency_vs_threads.png
│
├── report/
│   └── .gitkeep
