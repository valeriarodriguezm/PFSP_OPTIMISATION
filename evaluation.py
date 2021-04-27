import numpy as np

def makespan(s, P):
    """Calculate the makespan given a sequence of jobs and a matrix of processing
   times. This function can also compute the makespan of a partial sequence but P must be the complete matrix.

    Arguments:
    s -- numpy vector containing a sequence of jobs. It must be a (possibly a subset) of a permutation of 0, 1, ..., number of jobs.
    P -- a NumPy matrix of shape (number of jobs, number of machines).
    """
    # We index the processing time matrix by s so that we can simply use 0 to
    # refer to s[0], 1 to refer to s[1], etc in the completion times matrix.
    # Otherwise we would have to use C[s[i], j] later.
    # This also allows handling partial sequences. In that case, C will contain fewer rows.
    C = P[s, :]  #first job (row for job1), all columns. We need to change from wide to long format
    # n: jobs (Rows)
    # m: machines (columns)
    n, m = C.shape
    # Eq 1: Completion time of first job on all machines.
    # Note: np.cumsum is much faster than a loop.
    C[0, :] = np.cumsum(C[0, :]) 
    # Eq 2: Completion time of each job k on first machine.
    C[:, 0] = np.cumsum(C[:, 0]) #first machine, all jobs
    #print(C[0,:])
    # It may be possible to remove these two loops with fancy indexing, but
    # let's keep it simple.
    for i in range(1, n):
        for j in range(1, m):
            # Eq 3. C[i,j] already contains P[s[i], j]
            # Note: np.maximum is faster than max()
            C[i, j] += np.maximum(C[i - 1, j], C[i, j - 1])
        #print(C[i,:])
        
    # We only need the makespan (completion time of the last job on the last
    # machine).
    return C[-1, -1]


# Example in coursework brief
P0 = np.transpose(np.array([[3,3,4,2,3],[2,1,3,3,1],[4,2,1,2,3]]))
s0 = np.arange(P0.shape[0])
print(makespan(s0, P0))

# Larger examples.
# To get reproducible results.
np.random.seed(42)
n = 10
m = 100
P = np.random.randint(1, 10, (n, m))
s = np.random.permutation(np.arange(n))
print(s)
print(P)
# This takes 1.98 ms ± 14.7 µs in my computer and returns 653 for me.
print(makespan(s,P))

