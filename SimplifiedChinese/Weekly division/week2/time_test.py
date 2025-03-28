import time
import timeit

# Method 1: Using time.time() with warmup
def sumOfN2(n):
    start = time.time()
    theSum = 0
    for i in range(1, n+1):
        theSum = theSum + i
    end = time.time()
    return theSum, end - start

# Warmup run
print("Doing warmup run...")
_ = sumOfN2(1000000)

# Actual measurements
print("\nMethod 1 - Using time.time():")
for i in range(5):
    result, time_taken = sumOfN2(1000000)
    print("Sum is %d required %10.7f seconds" % (result, time_taken))

# Method 2: Using timeit for more accurate measurements
def sumOfN2_timeit(n):
    theSum = 0
    for i in range(1, n+1):
        theSum = theSum + i
    return theSum

print("\nMethod 2 - Using timeit:")
times = timeit.repeat(
    stmt="sumOfN2_timeit(1000000)",
    setup="from __main__ import sumOfN2_timeit",
    number=1,
    repeat=5
)

for i, t in enumerate(times):
    print(f"Run {i+1}: {t:10.7f} seconds") 