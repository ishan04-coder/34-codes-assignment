🔢 Project: Comprehensive Number Theory Toolkit in Python

 💡 Problem Statement

Many fundamental concepts in number theory, discrete mathematics, and computational mathematics require specialized algorithms (e.g., modular exponentiation, prime factorization, primality testing, sequence generation) that are often challenging to implement correctly and efficiently from scratch. The goal of this project is to provide a single, well-documented, and robust Python library of numerical functions to calculate these properties and solve common number-theoretic problems accurately.

 🔭 Scope of the Project

The project encompasses the implementation and verification of **34 distinct mathematical functions** covering four major domains of number theory and related computation:

1.  **Basic Arithmetic & Digit Analysis**: Functions for digit-level calculations (e.g., mean, root, persistence) and basic number sequences (e.g., factorial).
2.  **Number Classification**: Functions to identify special number types (e.g., prime, abundant, deficient, Harshad, Pronic, Highly Composite, Carmichael).
3.  **Advanced Prime & Factor Analysis**: Algorithms for factorization and primality testing (e.g., Miller-Rabin, Pollard's Rho) and prime number relationships (e.g., twin primes, Mersenne primes, prime powers).
4.  **Modular Arithmetic & Cryptography Primitives**: Core functions for modern cryptography and abstract algebra (e.g., modular inverse, Chinese Remainder Theorem, quadratic residues, order).

The project scope is limited to pure numerical algorithms and does not include external libraries (beyond standard `math`, `random`, and integer arithmetic) or complex data visualization.

👤 Target Users

* **Students & Educators**: Those studying or teaching introductory and advanced Number Theory, Discrete Mathematics, and Computer Science courses.
* **Competitive Programmers**: Individuals needing fast, reliable implementations of core number-theoretic algorithms for coding contests.
* **Cryptography Developers**: Engineers and researchers requiring foundational building blocks like modular inverse and CRT for cryptographic applications.
* **Data Scientists & Researchers**: Professionals who need specialized number properties for analytical or statistical modeling.

---

 ✨ High-Level Features

The codebase offers a suite of functionalities organized into the following major features:

| Feature Category | Description & Key Functions |
| :--- | :--- |
| **Prime & Factorization** | Accurate and efficient algorithms for decomposing numbers. Includes `prime_factors`, `count_divisors`, `is_prime_miller_rabin`, and `pollard_rho`. |
| **Modular Algebra Tools** | Essential cryptographic and abstract algebra utilities. Includes `mod_exp`, `mod_inverse`, and the **Chinese Remainder Theorem** (`crt`). |
| **Number Type Checkers** | Functions for classifying a number based on its mathematical properties. Includes `is_abundant`, `is_harshad`, `is_pronic`, and `is_carmichael`. |
| **Special Sequences** | Generation and identification of numbers in famous sequences. Includes `twin_primes`, `lucas_sequence`, and `is_fibonacci_prime`. |
| **Digit & Iteration Analysis** | Tools for working with the digits of a number. Includes `digital_root`, `mean_of_digits`, and `multiplicative_persistence`. |
| **Geometric & Recreational** | Functions for non-standard number patterns. Includes `polygonal_number` and the **Collatz conjecture** length (`collatz_length`). |
