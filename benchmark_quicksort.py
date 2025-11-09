import random, time, csv, sys
from statistics import median
from quicksort import randomized_quicksort, deterministic_quicksort, is_sorted

# Allow deep recursion for worst-case deterministic quicksort on sorted data
sys.setrecursionlimit(1_000_000)

def gen_random(n):
    return [random.randint(0, 10**6) for _ in range(n)]

def gen_sorted(n):
    return list(range(n))

def gen_reverse(n):
    return list(range(n, 0, -1))

def gen_repeated(n, k=5):
    return [random.randint(0, k-1) for _ in range(n)]

def time_once(fn, data):
    start = time.perf_counter()
    out = fn(list(data))
    elapsed = time.perf_counter() - start
    assert is_sorted(out)
    return elapsed

def run_bench(sizes=(1000, 3000, 6000), trials=3, out_csv="quicksort_results.csv"):
    rows = []
    gens = [
        ("random", gen_random),
        ("sorted", gen_sorted),
        ("reverse", gen_reverse),
        ("repeated", gen_repeated),
    ]
    algs = [
        ("randomized", randomized_quicksort),
        ("deterministic", deterministic_quicksort),
    ]
    for n in sizes:
        for gname, gfun in gens:
            data = gfun(n)
            for aname, afun in algs:
                times = [time_once(afun, data) for _ in range(trials)]
                row = {
                    "n": n,
                    "distribution": gname,
                    "algorithm": aname,
                    "trial_times": times,
                    "median_time": median(times),
                    "mean_time": sum(times)/len(times),
                }
                rows.append(row)
                print(f"n={n:6d} {gname:8s} {aname:12s} median={row['median_time']:.6f}s")
    # write CSV
    with open(out_csv, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["n","distribution","algorithm","median_time","mean_time","trial_times"])
        w.writeheader()
        for r in rows:
            r = r.copy()
            r["trial_times"] = ";".join(f"{t:.6f}" for t in r["trial_times"])
            w.writerow(r)
    return rows

if __name__ == "__main__":
    run_bench()
