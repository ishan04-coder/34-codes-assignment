def factorial(n):
    """Calculates n! using recursion."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1
    return n * factorial(n - 1)
# Example usage
print(f"5! = {factorial(5)}")
print(f"0! = {factorial(0)}")

output:
5! = 120
0! = 1

CODE 2
def is_palindrome(n) -> bool:
    """
    Checks if an integer reads the same forwards and backwards (a palindrome).

    The function converts the number to a string and compares the string
    to its reversed version.

    Args:
        n: The integer to check.

    Returns:
        True if the number is a palindrome, False otherwise.
    """
    # Convert the integer to a string
    n_str = str(n)
    
    # Check if the string is equal to its reverse using slicing
    return n_str == n_str[::-1]

# Example usage
print(f"Is 121 a palindrome? {is_palindrome(121)}")
print(f"Is 12345 a palindrome? {is_palindrome(12345)}")
print(f"Is 1001 a palindrome? {is_palindrome(1001)}")
print(f"Is -121 a palindrome? {is_palindrome(-121)}")

OUTPUT:
Is 121 a palindrome? True
Is 12345 a palindrome? False
Is 1001 a palindrome? True
Is -121 a palindrome? False

CODE 3
def mean_of_digits(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 0.0
    
    s = str(n)
    return sum(int(d) for d in s) / len(s)

# Example usage
test_numbers = [123, 555, 9876, 0, 42]

for num in test_numbers:
    try:
        avg = mean_of_digits(num)
        print(f"Mean of digits in {num}: {avg:.2f}")
    except ValueError as e:
        print(f"Error for {num}: {e}")

try:
    mean_of_digits(-1)
except ValueError as e:
    print(f"Error for -1: {e}")

OUTPUT:
Mean of digits in 123: 2.00
Mean of digits in 555: 5.00
Mean of digits in 9876: 7.50
Mean of digits in 0: 0.00
Mean of digits in 42: 3.00
Error for -1: Input must be a non-negative integer.

CODE 4

    def digital_root(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    if n == 0:
        return 0
    
    while n >= 10:
        current_sum = 0
        
        n_str = str(n)
        
        for digit_char in n_str:
            current_sum += int(digit_char)
            
        n = current_sum
        
    return n

# Example usage
test_numbers = [123, 49, 999, 0, 7832]

print("--- Digital Root Calculation (Beginner Method) ---")

for num in test_numbers:
    try:
        root = digital_root(num)
        print(f"The digital root of {num} is: {root}")
    except ValueError as e:
        print(f"Error for input {num}: {e}")

try:
    digital_root(-50)
except ValueError as e:
    print(f"\nCaught expected error: {e}")

OUTPUT:
--- Digital Root Calculation (Beginner Method) ---
The digital root of 123 is: 6
The digital root of 49 is: 4
The digital root of 999 is: 9
The digital root of 0 is: 0
The digital root of 7832 is: 2

Caught expected error: Input must be a non-negative integer.

CODE 5

def is_abundant(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer (n > 0).")
    
    proper_divisors_sum = 0
    
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            proper_divisors_sum += i
            
    return proper_divisors_sum > n

# --- Example Usage ---

print(f"Is 12 abundant? {is_abundant(12)}")

print(f"Is 15 abundant? {is_abundant(15)}")

print(f"Is 6 abundant? {is_abundant(6)}")

try:
    is_abundant(-10)
except ValueError as e:
    print(f"\nCaught expected error: {e}")

OUTPUT:
Is 12 abundant? True
Is 15 abundant? False
Is 6 abundant? False

Caught expected error: Input must be a positive integer (n > 0).

CODE 6

def is_deficient(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer (n > 0).")
    
    proper_divisors_sum = 0
    
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            proper_divisors_sum += i
            
    return proper_divisors_sum < n

# --- Example Usage ---

print(f"Is 15 deficient? {is_deficient(15)}")

print(f"Is 12 deficient? {is_deficient(12)}")

print(f"Is 6 deficient? {is_deficient(6)}")

try:
    is_deficient(0)
except ValueError as e:
    print(f"\nCaught expected error: {e}")

OUTPUT:
Is 15 deficient? True
Is 12 deficient? False
Is 6 deficient? False

Caught expected error: Input must be a positive integer (n > 0).

CODE 7

def is_harshad(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer (n > 0).")
    
    s_digits = sum(int(d) for d in str(n))
    
    return n % s_digits == 0

# --- Example Usage ---

print(f"Is 18 a Harshad number? {is_harshad(18)}")

print(f"Is 14 a Harshad number? {is_harshad(14)}")

print(f"Is 156 a Harshad number? {is_harshad(156)}")

try:
    is_harshad(-10)
except ValueError as e:
    print(f"\nCaught expected error: {e}")

OUTPUT:
Is 18 a Harshad number? True
Is 14 a Harshad number? False
Is 156 a Harshad number? True

Caught expected error: Input must be a positive integer (n > 0).

CODE 8
def is_pronic(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer (n > 0).")
    
    k = 1
    
    while k * (k + 1) <= n:
        
        if k * (k + 1) == n:
            return True
        
        k += 1
        
    return False

# --- Example Usage ---

# 6 is Pronic (2 * 3 = 6)
print(f"Is 6 a Pronic number? {is_pronic(6)}")

# 12 is Pronic (3 * 4 = 12)
print(f"Is 12 a Pronic number? {is_pronic(12)}")

# 15 is NOT Pronic (next Pronic is 4*5=20)
print(f"Is 15 a Pronic number? {is_pronic(15)}")

# 56 is Pronic (7 * 8 = 56)
print(f"Is 56 a Pronic number? {is_pronic(56)}")

try:
    is_pronic(0)
except ValueError as e:
    print(f"\nCaught expected error: {e}")

OUTPUT:
Is 6 a Pronic number? True
Is 12 a Pronic number? True
Is 15 a Pronic number? False
Is 56 a Pronic number? True

Caught expected error: Input must be a positive integer (n > 0).

CODE 9

def prime_factors(n):
    if not isinstance(n, int) or n <= 1:
        raise ValueError("Input must be an integer greater than 1.")
    
    factors = []
    
    while n % 2 == 0:
        factors.append(2)
        n //= 2
        
    d = 3
    while d * d <= n:
        if n % d == 0:
            factors.append(d)
            n //= d
        else:
            d += 2
            
    if n > 1:
        factors.append(n)
        
    return factors

# --- Example Usage ---

print(f"Prime factors of 12: {prime_factors(12)}")

print(f"Prime factors of 36: {prime_factors(36)}")

print(f"Prime factors of 17: {prime_factors(17)}")

print(f"Prime factors of 100: {prime_factors(100)}")

try:
    prime_factors(1)
except ValueError as e:
    print(f"\nCaught expected error: {e}")

OUTPUT:
Prime factors of 12: [2, 2, 3]
Prime factors of 36: [2, 2, 3, 3]
Prime factors of 17: [17]
Prime factors of 100: [2, 2, 5, 5]

Caught expected error: Input must be an integer greater than 1.

CODE 10
def count_distinct_prime_factors(n):
    if not isinstance(n, int) or n <= 1:
        raise ValueError("Input must be an integer greater than 1.")
    
    unique_factors = set()
    
    if n % 2 == 0:
        unique_factors.add(2)
        while n % 2 == 0:
            n //= 2
        
    d = 3
    while d * d <= n:
        if n % d == 0:
            unique_factors.add(d)
            while n % d == 0:
                n //= d
        
        d += 2
            
    if n > 1:
        unique_factors.add(n)
        
    return len(unique_factors)

# --- Example Usage ---

print(f"Number of distinct prime factors for 12: {count_distinct_prime_factors(12)}")

print(f"Number of distinct prime factors for 36: {count_distinct_prime_factors(36)}")

print(f"Number of distinct prime factors for 30: {count_distinct_prime_factors(30)}")

print(f"Number of distinct prime factors for 7: {count_distinct_prime_factors(7)}")

try:
    count_distinct_prime_factors(1)
except ValueError as e:
    print(f"\nCaught expected error: {e}")

OUTPUT:
Number of distinct prime factors for 12: 2
Number of distinct prime factors for 36: 2
Number of distinct prime factors for 30: 3
Number of distinct prime factors for 7: 1

Caught expected error: Input must be an integer greater than 1.

CODE 11

def is_prime_power(n):
    if not isinstance(n, int) or n <= 1:
        raise ValueError("Input must be an integer greater than 1.")
    
    unique_factors = set()
    temp_n = n
    
    if temp_n % 2 == 0:
        unique_factors.add(2)
        while temp_n % 2 == 0:
            temp_n //= 2
        
    d = 3
    while d * d <= temp_n:
        if temp_n % d == 0:
            unique_factors.add(d)
            while temp_n % d == 0:
                temp_n //= d
        
        d += 2
            
    if temp_n > 1:
        unique_factors.add(temp_n)
        
    return len(unique_factors) == 1

# --- Example Usage ---

print(f"Is 8 a prime power? {is_prime_power(8)}")

print(f"Is 12 a prime power? {is_prime_power(12)}")

print(f"Is 49 a prime power? {is_prime_power(49)}")

print(f"Is 30 a prime power? {is_prime_power(30)}")

try:
    is_prime_power(1)
except ValueError as e:
    print(f"\nCaught expected error: {e}")

OUTPUT:

Is 8 a prime power? True
Is 12 a prime power? False
Is 49 a prime power? True
Is 30 a prime power? False

Caught expected error: Input must be an integer greater than 1.

CODE 12

import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    limit = int(math.sqrt(n))
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
            
    return True

def is_mersenne_prime(p):
    if not isinstance(p, int) or p <= 1:
        raise ValueError("Input 'p' must be an integer greater than 1.")
    
    if not is_prime(p):
        raise ValueError(f"Input {p} must be a prime number itself to form a Mersenne number.")

    mersenne_number = (2 ** p) - 1
    
    return is_prime(mersenne_number)

# --- Example Usage ---

print(f"Is M_2 (3) a Mersenne Prime? {is_mersenne_prime(2)}")

print(f"Is M_3 (7) a Mersenne Prime? {is_mersenne_prime(3)}")

print(f"Is M_5 (31) a Mersenne Prime? {is_mersenne_prime(5)}")

print(f"Is M_11 (2047) a Mersenne Prime? {is_mersenne_prime(11)}")

try:
    is_mersenne_prime(4)
except ValueError as e:
    print(f"\nCaught expected error: {e}")

OUTPUT:

Is M_2 (3) a Mersenne Prime? True
Is M_3 (7) a Mersenne Prime? True
Is M_5 (31) a Mersenne Prime? True
Is M_11 (2047) a Mersenne Prime? False

Caught expected error: Input 4 must be a prime number itself to form a Mersenne number.

CODE 13

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
            
    return True

def twin_primes(limit):
    if not isinstance(limit, int) or limit <= 1:
        raise ValueError("Limit must be an integer greater than 1.")
    
    twin_pairs = []
    
    for p in range(3, limit - 1):
        if is_prime(p):
            p_plus_2 = p + 2
            if is_prime(p_plus_2):
                twin_pairs.append((p, p_plus_2))
                
    return twin_pairs

# --- Example Usage ---

LIMIT = 50
print(f"Twin primes up to {LIMIT}: {twin_primes(LIMIT)}")

LIMIT_SMALL = 10
print(f"Twin primes up to {LIMIT_SMALL}: {twin_primes(LIMIT_SMALL)}")

try:
    twin_primes(1)
except ValueError as e:
    print(f"\nCaught expected error: {e}")

OUTPUT:

Twin primes up to 50: [(3, 5), (5, 7), (11, 13), (17, 19), (29, 31), (41, 43)]
Twin primes up to 10: [(3, 5), (5, 7)]

Caught expected error: Limit must be an integer greater than 1.

CODE 14

def count_divisors(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer (n > 0).")
    
    count = 0
    i = 1
    
    while i * i <= n:
        if n % i == 0:
            
            if i * i == n:
                count += 1
            else:
                count += 2
        
        i += 1
        
    return count

print(f"Number of divisors for 12: {count_divisors(12)}")

print(f"Number of divisors for 36: {count_divisors(36)}")

print(f"Number of divisors for 7: {count_divisors(7)}")

try:
    count_divisors(0)
except ValueError as e:
    print(f"\nCaught expected error: {e}")

OUTPUT:

Number of divisors for 12: 6
Number of divisors for 36: 9
Number of divisors for 7: 2

Caught expected error: Input must be a positive integer (n > 0).

CODE 15

def aliquot_sum(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer (n > 0).")
    
    s = 0
    i = 1
    
    while i * i <= n:
        if n % i == 0:
            d1 = i
            d2 = n // i
            
            s += d1
            
            if d2 != n:
                if d1 != d2:
                    s += d2
        
        i += 1
        
    return s

print(f"Aliquot sum of 12: {aliquot_sum(12)}")

print(f"Aliquot sum of 6: {aliquot_sum(6)}")

print(f"Aliquot sum of 10: {aliquot_sum(10)}")

try:
    aliquot_sum(0)
except ValueError as e:
    print(f"\nCaught expected error: {e}")

OUTPUT:

Aliquot sum of 12: 16
Aliquot sum of 6: 6
Aliquot sum of 10: 8

Caught expected error: Input must be a positive integer (n > 0).

CODE 16

def aliquot_sum(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer (n > 0).")
    
    s = 0
    i = 1
    
    while i * i <= n:
        if n % i == 0:
            d1 = i
            d2 = n // i
            
            s += d1
            
            if d2 != n:
                if d1 != d2:
                    s += d2
        
        i += 1
        
    return s

def are_amicable(a, b):
    if not isinstance(a, int) or not isinstance(b, int) or a <= 0 or b <= 0:
        raise ValueError("Inputs must be positive integers (a > 0, b > 0).")
    
    if a == b:
        return False
        
    sum_a = aliquot_sum(a)
    
    sum_b = aliquot_sum(b)
    
    return sum_a == b and sum_b == a

# --- Example Usage ---

print(f"Are (220, 284) amicable? {are_amicable(220, 284)}")

print(f"Are (17296, 18416) amicable? {are_amicable(17296, 18416)}")

print(f"Are (12, 18) amicable? {are_amicable(12, 18)}")

print(f"Are (6, 6) amicable? {are_amicable(6, 6)}")

try:
    are_amicable(0, 10)
except ValueError as e:
    print(f"\nCaught expected error: {e}")

OUTPUT:
Are (220, 284) amicable? True
Are (17296, 18416) amicable? True
Are (12, 18) amicable? False
Are (6, 6) amicable? False

Caught expected error: Inputs must be positive integers (a > 0, b > 0).

CODE 17

def multiplicative_persistence(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    persistence_count = 0
    
    while n >= 10:
        
        current_product = 1
        
        n_str = str(n)
        
        for digit_char in n_str:
            current_product *= int(digit_char)
            
        persistence_count += 1
        
        n = current_product
        
    return persistence_count

print(f"Persistence of 39: {multiplicative_persistence(39)}")

print(f"Persistence of 4: {multiplicative_persistence(4)}")

print(f"Persistence of 77: {multiplicative_persistence(77)}")

try:
    multiplicative_persistence(-10)
except ValueError as e:
    print(f"\nCaught expected error: {e}")

OUTPUT:

Persistence of 39: 3
Persistence of 4: 0
Persistence of 77: 4

Caught expected error: Input must be a non-negative integer.

CODE 18

    def count_divisors(n):
    if n <= 0:
        return 0
    
    count = 0
    i = 1
    
    while i * i <= n:
        if n % i == 0:
            if i * i == n:
                count += 1
            else:
                count += 2
        
        i += 1
        
    return count

def is_highly_composite(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer (n > 0).")

    divisors_of_n = count_divisors(n)
    
    for k in range(1, n):
        divisors_of_k = count_divisors(k)
        
        if divisors_of_k >= divisors_of_n:
            return False
            
    return True

print(f"Is 6 highly composite? {is_highly_composite(6)}")

print(f"Is 10 highly composite? {is_highly_composite(10)}")

print(f"Is 12 highly composite? {is_highly_composite(12)}")

print(f"Is 13 highly composite? {is_highly_composite(13)}")

try:
    is_highly_composite(0)
except ValueError as e:
    print(f"\nCaught expected error: {e}")

OUTPUT:
Is 6 highly composite? True
Is 10 highly composite? False
Is 12 highly composite? True
Is 13 highly composite? False

Caught expected error: Input must be a positive integer (n > 0).

CODE 19

def mod_exp(base, exponent, modulus):
    if not isinstance(base, int) or not isinstance(exponent, int) or not isinstance(modulus, int):
        raise ValueError("Inputs must be integers.")
    if exponent < 0:
        raise ValueError("Exponent must be non-negative.")
    if modulus <= 0:
        raise ValueError("Modulus must be positive.")
    
    result = 1
    
    base = base % modulus
    
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        
        base = (base * base) % modulus
        
        exponent //= 2
        
    return result

print(f"(4^3) % 5 = {mod_exp(4, 3, 5)}")

print(f"(2^100) % 7 = {mod_exp(2, 100, 7)}")

print(f"(1000^2) % 3 = {mod_exp(1000, 2, 3)}")

print(f"(5^0) % 13 = {mod_exp(5, 0, 13)}")

OUTPUT:

(4^3) % 5 = 4
(2^100) % 7 = 2
(1000^2) % 3 = 1
(5^0) % 13 = 1

CODE 20

def extended_gcd(a, b):
    x0, x1 = 1, 0
    y0, y1 = 0, 1

    while b != 0:
        q = a // b
        a, b = b, a % b
        
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
        
    return a, x0, y0

def mod_inverse(a, m):
    if not isinstance(a, int) or not isinstance(m, int):
        raise ValueError("Inputs must be integers.")
    if m <= 0:
        raise ValueError("Modulus m must be positive.")

    g, x, y = extended_gcd(a, m)

    if g != 1:
        raise ValueError(f"Modular inverse does not exist because {a} and {m} are not coprime (GCD != 1).")
    else:
        return x % m

print(f"Inverse of 3 mod 11: {mod_inverse(3, 11)}")

print(f"Inverse of 17 mod 43: {mod_inverse(17, 43)}")

print(f"Inverse of 5 mod 7: {mod_inverse(5, 7)}")

try:
    mod_inverse(2, 4)
except ValueError as e:
    print(f"\nCaught expected error: {e}")

OUTPUT:

Inverse of 3 mod 11: 4
Inverse of 17 mod 43: 38
Inverse of 5 mod 7: 3

Caught expected error: Modular inverse does not exist because 2 and 4 are not coprime (GCD != 1).

CODE 21

def extended_gcd(a, b):
    x0, x1 = 1, 0
    y0, y1 = 0, 1

    while b != 0:
        q = a // b
        a, b = b, a % b
        
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
        
    return a, x0, y0

def mod_inverse(a, m):
    if m <= 0:
        raise ValueError("Modulus must be positive.")

    g, x, y = extended_gcd(a, m)

    if g != 1:
        raise ValueError("Modular inverse does not exist.")
    else:
        return x % m

def crt(remainders, moduli):
    if len(remainders) != len(moduli):
        raise ValueError("Lists must have same length.")

    N = 1
    for m in moduli:
        if m <= 0:
            raise ValueError("Moduli must be positive.")
        N *= m

    total_sum = 0
    
    for r_i, m_i in zip(remainders, moduli):
        N_i = N // m_i
        
        try:
            N_i_inv = mod_inverse(N_i, m_i)
        except ValueError:
            raise ValueError("Moduli must be pairwise coprime.")

        term = r_i * N_i * N_i_inv
        
        total_sum += term

    return total_sum % N

R = [2, 3, 2]
M = [3, 5, 7]
print(f"CRT Solution: {crt(R, M)}")

R2 = [1, 4, 6]
M2 = [3, 5, 7]
print(f"CRT Solution: {crt(R2, M2)}")

try:
    R3 = [1, 2]
    M3 = [4, 6]
    crt(R3, M3)
except ValueError as e:
    print(f"Error: {e}")

OUTPUT:

CRT Solution: 23
CRT Solution: 34
Error: Moduli must be pairwise coprime.

CODE 22

import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    limit = int(math.sqrt(n))
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
            
    return True

def is_quadratic_residue(a, p):
    if not isinstance(a, int) or not isinstance(p, int) or p <= 2 or not is_prime(p):
        raise ValueError("Modulus 'p' must be an odd prime number (p > 2).")
        
    if a % p == 0:
        return True
    
    exponent = (p - 1) // 2
    
    result = pow(a, exponent, p)
    
    if result == 1:
        return True
    else:
        return False

P = 7

print(f"Is 2 a quadratic residue mod 7? {is_quadratic_residue(2, P)}")

print(f"Is 3 a quadratic residue mod 7? {is_quadratic_residue(3, P)}")

print(f"Is 9 a quadratic residue mod 13? {is_quadratic_residue(9, 13)}") 
print(f"Is 2 a quadratic residue mod 13? {is_quadratic_residue(2, 13)}")

print(f"Is 26 (0 mod 13) a quadratic residue mod 13? {is_quadratic_residue(26, 13)}")

OUTPUT:

Is 2 a quadratic residue mod 7? True
Is 3 a quadratic residue mod 7? False
Is 9 a quadratic residue mod 13? True
Is 2 a quadratic residue mod 13? False
Is 26 (0 mod 13) a quadratic residue mod 13? True

CODE 23

def extended_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def order_mod(a, n):
    if not isinstance(a, int) or not isinstance(n, int) or a <= 0 or n <= 0:
        raise ValueError("Inputs 'a' and 'n' must be positive integers.")
    
    if extended_gcd(a, n) != 1:
        raise ValueError(f"The order of {a} mod {n} does not exist because GCD({a}, {n}) != 1.")
        
    k = 1
    
    current_power = a % n 
    
    while current_power != 1:
        
        current_power = (current_power * a) % n
        
        k += 1
        
        if k > n:
            raise RuntimeError("Order check exceeded modulus n. Unexpected error.")
            
    return k

print(f"Order of 3 mod 7: {order_mod(3, 7)}")

print(f"Order of 2 mod 11: {order_mod(2, 11)}")

print(f"Order of 10 mod 11: {order_mod(10, 11)}")

try:
    order_mod(4, 8)
except ValueError as e:
    print(f"\nCaught expected error: {e}")

OUTPUT:

Order of 3 mod 7: 6
Order of 2 mod 11: 10
Order of 10 mod 11: 2

Caught expected error: The order of 4 mod 8 does not exist because GCD(4, 8) != 1.

CODE 24 

import math

def is_perfect_square(n):
    if n < 0:
        return False
    sqrt_n = int(math.sqrt(n))
    return sqrt_n * sqrt_n == n

def is_fibonacci(n):
    if n <= 0:
        return False
        
    check1 = 5 * n * n + 4
    check2 = 5 * n * n - 4
    
    return is_perfect_square(check1) or is_perfect_square(check2)

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
            
    return True

def is_fibonacci_prime(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer.")
    
    return is_fibonacci(n) and is_prime(n)

print(f"Is 3 a Fibonacci Prime? {is_fibonacci_prime(3)}")

print(f"Is 8 a Fibonacci Prime? {is_fibonacci_prime(8)}")

print(f"Is 7 a Fibonacci Prime? {is_fibonacci_prime(7)}")

print(f"Is 13 a Fibonacci Prime? {is_fibonacci_prime(13)}")

print(f"Is 21 a Fibonacci Prime? {is_fibonacci_prime(21)}")

try:
    is_fibonacci_prime(0)
except ValueError as e:
    print(f"\nCaught expected error: {e}")

OUTPUT:

Is 3 a Fibonacci Prime? True
Is 8 a Fibonacci Prime? False
Is 7 a Fibonacci Prime? False
Is 13 a Fibonacci Prime? True
Is 21 a Fibonacci Prime? False

Caught expected error: Input must be a positive integer.

CODE 25

def lucas_sequence(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    if n == 0:
        return []
    
    sequence = [2, 1]
    
    if n == 1:
        return [2]
    
    for _ in range(n - 2):
        
        next_lucas = sequence[-1] + sequence[-2]
        
        sequence.append(next_lucas)
        
    return sequence

print(f"First 5 Lucas numbers: {lucas_sequence(5)}")

print(f"First 10 Lucas numbers: {lucas_sequence(10)}")

print(f"First 1 Lucas number: {lucas_sequence(1)}")
print(f"First 0 Lucas numbers: {lucas_sequence(0)}")

try:
    lucas_sequence(-1)
except ValueError as e:
    print(f"\nCaught expected error: {e}")

OUTPUT:

First 5 Lucas numbers: [2, 1, 3, 4, 7]
First 10 Lucas numbers: [2, 1, 3, 4, 7, 11, 18, 29, 47, 76]
First 1 Lucas number: [2]
First 0 Lucas numbers: []

Caught expected error: Input must be a non-negative integer.

CODE 26

    import math

def is_perfect_power(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer (n > 0).")
    
    if n == 1:
        return True
        
    max_exponent = int(math.log2(n))
    
    for b in range(2, max_exponent + 1):
        
        a_float = n ** (1 / b)
        
        a = round(a_float)
        
        if a ** b == n:
            return True
            
    return False

print(f"Is 8 a perfect power? {is_perfect_power(8)}")

print(f"Is 9 a perfect power? {is_perfect_power(9)}")

print(f"Is 12 a perfect power? {is_perfect_power(12)}")

print(f"Is 64 a perfect power? {is_perfect_power(64)}")

print(f"Is 1 a perfect power? {is_perfect_power(1)}")

try:
    is_perfect_power(-5)
except ValueError as e:
    print(f"\nCaught expected error: {e}")

OUTPUT:

Is 8 a perfect power? True
Is 9 a perfect power? True
Is 12 a perfect power? False
Is 64 a perfect power? True
Is 1 a perfect power? True

Caught expected error: Input must be a positive integer (n > 0).

CODE 27

def collatz_length(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer (n > 0).")
    
    steps = 0
    
    while n != 1:
        
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
            
        steps += 1
        
    return steps

print(f"Collatz length of 6: {collatz_length(6)}")

print(f"Collatz length of 27: {collatz_length(27)}")

print(f"Collatz length of 1: {collatz_length(1)}")

try:
    collatz_length(0)
except ValueError as e:
    print(f"\nCaught expected error: {e}")

OUTPUT:

Collatz length of 6: 8
Collatz length of 27: 111
Collatz length of 1: 0

Caught expected error: Input must be a positive integer (n > 0).

CODE 28

def polygonal_number(s, n):
    if not isinstance(s, int) or s < 3:
        raise ValueError("The number of sides 's' must be an integer >= 3.")
    if not isinstance(n, int) or n <= 0:
        raise ValueError("The term number 'n' must be a positive integer (n >= 1).")
    
    numerator = (n * n * (s - 2)) - (n * (s - 4))
    
    result = numerator // 2
    
    return result

print(f"4th Triangular Number (s=3, n=4): {polygonal_number(3, 4)}")

print(f"5th Square Number (s=4, n=5): {polygonal_number(4, 5)}")

print(f"3rd Pentagonal Number (s=5, n=3): {polygonal_number(5, 3)}")

print(f"4th Hexagonal Number (s=6, n=4): {polygonal_number(6, 4)}")

try:
    polygonal_number(2, 5)
except ValueError as e:
    print(f"\nCaught expected error: {e}")

OUTPUT:

4th Triangular Number (s=3, n=4): 10
5th Square Number (s=4, n=5): 25
3rd Pentagonal Number (s=5, n=3): 12
4th Hexagonal Number (s=6, n=4): 28

Caught expected error: The number of sides 's' must be an integer >= 3.

CODE 29

import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
            
    return True

def is_carmichael(n):
    if not isinstance(n, int) or n <= 1:
        raise ValueError("Input must be an integer greater than 1.")

    if is_prime(n):
        return False
    
    for a in range(2, n):
        
        if gcd(a, n) == 1:
            
            if pow(a, n - 1, n) != 1:
                return False
                
    return True

print(f"Is 561 a Carmichael number? {is_carmichael(561)}")
print(f"Is 1105 a Carmichael number? {is_carmichael(1105)}") 
print(f"Is 9 a Carmichael number? {is_carmichael(9)}")
print(f"Is 17 a Carmichael number? {is_carmichael(17)}")

try:
    is_carmichael(1)
except ValueError as e:
    print(f"\nCaught expected error: {e}")

OUTPUT:

Is 561 a Carmichael number? True
Is 1105 a Carmichael number? True
Is 9 a Carmichael number? False
Is 17 a Carmichael number? False

Caught expected error: Input must be an integer greater than 1.

CODE 30

import random
import math

def get_decomposition(n):
    s = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        s += 1
    return s, d

def miller_rabin_test(n, d, s, a):
    x = pow(a, d, n)
    
    if x == 1 or x == n - 1:
        return True
    
    for _ in range(s - 1):
        x = pow(x, 2, n)
        
        if x == n - 1:
            return True
            
    return False

def is_prime_miller_rabin(n, k=5):
    if not isinstance(n, int) or n <= 1:
        raise ValueError("Input 'n' must be an integer greater than 1.")
        
    if n == 2 or n == 3:
        return True
    
    if n % 2 == 0:
        return False
        
    s, d = get_decomposition(n)
    
    for _ in range(k):
        a = random.randint(2, n - 2)
        
        if not miller_rabin_test(n, d, s, a):
            return False
            
    return True

print(f"Is 97 prime (k=5)? {is_prime_miller_rabin(97, 5)}")

print(f"Is 100 prime (k=5)? {is_prime_miller_rabin(100, 5)}")

print(f"Is 999999 prime (k=5)? {is_prime_miller_rabin(999999, 5)}")

print(f"Is 561 prime (k=5)? {is_prime_miller_rabin(561, 5)}")

OUTPUT:

Is 97 prime (k=5)? True
Is 100 prime (k=5)? False
Is 999999 prime (k=5)? False
Is 561 prime (k=5)? False

CODE 32

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def pollard_rho(n):
    if not isinstance(n, int) or n <= 1:
        raise ValueError("Input 'n' must be an integer greater than 1.")
    
    if n % 2 == 0:
        return 2

    x = 2
    y = 2
    c = 1
    d = 1

    while d == 1:
        
        x = (x * x + c) % n
        
        y = (y * y + c) % n
        y = (y * y + c) % n
        
        d = gcd(abs(x - y), n)

        if d == n:
            x = 2
            y = 2
            c += 1 
            d = 1
            if c > n:
                raise RuntimeError("Pollard's Rho failed to find a factor.")
                
    return d

print(f"A factor of 99: {pollard_rho(99)}")

print(f"A factor of 221: {pollard_rho(221)}")

try:
    print(f"A factor of 17: {pollard_rho(17)}") 
except ValueError as e:
    print("For prime numbers, the algorithm is inefficient (often returns n itself).")

OUTPUT:

A factor of 99: 3
A factor of 221: 13

CODE 33

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def pollard_rho(n):
    if not isinstance(n, int) or n <= 1:
        raise ValueError("Input 'n' must be an integer greater than 1.")
    
    if n % 2 == 0:
        return 2

    x = 2
    y = 2
    c = 1
    d = 1

    while d == 1:
        
        x = (x * x + c) % n
        
        y = (y * y + c) % n
        y = (y * y + c) % n
        
        d = gcd(abs(x - y), n)

        if d == n:
            x = 2
            y = 2
            c += 1 
            d = 1
            if c > n:
                raise RuntimeError("Pollard's Rho failed to find a factor.")
                
    return d

print(f"A factor of 99: {pollard_rho(99)}")

print(f"A factor of 221: {pollard_rho(221)}")

try:
    print(f"A factor of 17: {pollard_rho(17)}") 
except ValueError as e:
    print("For prime numbers, the algorithm is inefficient (often returns n itself).")

OUTPUT:

A factor of 99: 3
A factor of 221: 13


CODE 34

def partition_function(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input 'n' must be a non-negative integer.")

    if n == 0:
        return 1

    dp = [0] * (n + 1)
    dp[0] = 1

    for j in range(1, n + 1):
        for i in range(j, n + 1):
            dp[i] += dp[i - j]
            
    return dp[n]

print(f"The number of partitions for 4 (p(4)): {partition_function(4)}")

print(f"The number of partitions for 5 (p(5)): {partition_function(5)}")

print(f"The number of partitions for 10 (p(10)): {partition_function(10)}")

try:
    partition_function(-1)
except ValueError as e:
    print(f"\nCaught expected error: {e}")

OUTPUT:

def partition_function(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input 'n' must be a non-negative integer.")

    if n == 0:
        return 1

    dp = [0] * (n + 1)
    dp[0] = 1

    for j in range(1, n + 1):
        for i in range(j, n + 1):
            dp[i] += dp[i - j]
            
    return dp[n]

print(f"The number of partitions for 4 (p(4)): {partition_function(4)}")

print(f"The number of partitions for 5 (p(5)): {partition_function(5)}")

print(f"The number of partitions for 10 (p(10)): {partition_function(10)}")

try:
    partition_function(-1)
except ValueError as e:
    print(f"\nCaught expected error: {e}")
    
