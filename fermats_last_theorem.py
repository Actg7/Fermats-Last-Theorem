import math

#verify fermat's last theorem for a set range and power#

def fermat_last_theorem(bound, n):
    if(n < 3):
        return
    for a in range(1, bound + 1):
        for b in range(a, bound + 1):
            c_n = pow(a, n) + pow(b, n)
            c = pow(c_n, 1.0 / n)
            c_pow = pow(int(c), n)
            if(c_pow == c_n):
                print("Counterexample found to Fermat's Last Theorem")
                return
    print("No counterexample found within the given range")
    return
