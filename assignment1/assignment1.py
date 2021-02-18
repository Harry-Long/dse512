import os
import numpy as np
import time
from multiprocessing import Pool


def my_pid(x):
    pid = os.getpid() 
    print(f"Hi, I'm worker {x} (with {pid})")


def py_pi(N):
    start = time.perf_counter()
    approx = 0    
    for i in range(1, N+1):
        approx += 4/N * (1 / (1 + ((i-0.5)/N)**2))
    
    real = np.pi
    print(f"Pi({N}) = {approx} (Real is {real}, difference is {real-approx})")
    
    end = time.perf_counter()
    print(f"Runtime for N = {N}: {end-start} seconds\n")


def py_pi_better(N, i_start, i_stop):
    partial = 0
    for i in range(i_start, i_stop):
        partial += 1 / (1 + ((i-0.5)/N)**2)
    
    return partial   


def main():
    print("\n====================Problem 1====================")
    pool = Pool(4)
    pool.map(my_pid, [x for x in range(10)])
    pool.close()

    print("\n====================Problem 2====================")
    N_list = [10 * 5 ** (i-1) for i in range(1,10)]
    pool = Pool(4)
    pool.map(py_pi, N_list)
    pool.close()

    print("\n====================Problem 3====================")
    # for N in [100, 500, 1000, 2000, 10000, 50000]:
    # use pool.starmap()    
    # loop over
    for N in [100, 500, 1000, 2000, 10000, 50000]:
        # N = 10    
        start = time.perf_counter()
        exp_list = [(N, int(i/4*N+1), int((i+1)/4*N+1)) for i in range(4)]
        pool = Pool(4)
        results_list = pool.starmap(py_pi_better, exp_list)
        approx = 4/N * sum(results_list)
        print(f"Pi({N}) = {approx} (Real is {np.pi}, difference is {np.pi-approx})")
        pool.close()
        end = time.perf_counter()
        print(f"Runtime for N = {N}: {end-start} seconds\n")


if __name__ == "__main__":
    main()


