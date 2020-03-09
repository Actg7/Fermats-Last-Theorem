import math

#determine whether a number is prime#

def is_prime(n):
    for i in range(2, int(int(n**0.5)+1)):
        if n % i == 0:
            return False
    return True

#calculate a^b in O(log b) time#

def power(a, b):
    ans = 1
    while(b > 0):
        if(b & 1):
            ans = ans * a
        a = a * a
        b = b >> 1
    return ans

#calculate the kth fermat number#

def fermat(k):
    power2_k = power(2, k)
    power2_2_k = power(2, power2_k)
    return power2_2_k + 1

#create a list of first n fermat numbers and a list of the prime fermat numbers present#

def prime_fermat_number(n):
	new_list = []
	prime_list = []
	for i in range(n):
		x =(fermat(i))
		new_list.append(x)
	for j in new_list:
		if is_prime(j):
			prime_list.append(j)
	print("The first "+str(n)+" Fermat number are: "+str(new_list))
	print("The prime Fermat numbers in this list are: "+str(prime_list))
	return
