# 34-codes-assignment
 🔢 Project: Comprehensive Number Theory Toolkit in Python
 🌟 Project Title

**Number Theory Computational Toolkit**

 💡 Overview of the Project

This project is a collection of **34 distinct Python functions** focusing on various mathematical concepts from number theory, modular arithmetic, and computational mathematics. The goal is to provide reliable, tested, and clear implementations for complex algorithms, ranging from basic digit analysis and number classification (like Harshad, Abundant, and Deficient numbers) to advanced cryptographic primitives (like Modular Inverse, Chinese Remainder Theorem, and Miller-Rabin Primality Test). The entire toolkit is contained within a single Jupyter Notebook for ease of use and experimentation.

 ✨ Features (34 Functions)

The toolkit is categorized into six high-level features:

#### 1. Prime & Factorization Analysis
* **Prime Factors**: Find all prime factors of a number.
* **Divisor Counting**: Efficiently count all divisors.
* **Miller-Rabin Test**: Probabilistic primality testing for large numbers.
* **Pollard's Rho Algorithm**: Find a non-trivial factor of a composite number.
* **Distinct Prime Factors**: Count the unique prime factors.

#### 2. Modular Arithmetic & Cryptography
* **Modular Exponentiation**: Efficiently calculate $a^b \pmod m$.
* **Modular Inverse**: Find the inverse of $a$ modulo $m$.
* **Chinese Remainder Theorem (CRT)**: Solve systems of linear congruences.
* **Quadratic Residue Check**: Determine if a number is a quadratic residue modulo a prime.
* **Multiplicative Order**: Find the order of an element modulo $n$.

#### 3. Special Number Classifiers
* **Perfect/Prime Powers**: Check if a number is $p^k$ or $a^b$.
* **Abundant/Deficient Numbers**: Classify based on the sum of proper divisors.
* **Amicable Numbers**: Check if two numbers form an amicable pair.
* **Carmichael Numbers**: Identify these pseudoprimes.
* **Harshad (Niven) Numbers**: Check divisibility by the sum of digits.
* **Pronic (Oblong) Numbers**: Check if $n = k(k+1)$.
* **Highly Composite Numbers**: Check if $n$ has more divisors than all $k < n$.

#### 4. Sequences and Series
* **Lucas Sequence**: Generate the $n$-th Lucas number.
* **Twin Primes**: Find twin prime pairs up to a limit.
* **Fibonacci Primes**: Check if a number is both Fibonacci and prime.
* **Polygonal Numbers**: Calculate the $n$-th $s$-sided polygonal number.
* **Partition Function**: Compute $p(n)$, the number of ways to partition $n$.

#### 5. Digit and Iteration Analysis
* **Factorial**: Calculate $n!$ recursively.
* **Palindrome Check**: Determine if a number reads the same backward as forward.
* **Mean of Digits**: Calculate the average of the digits.
* **Digital Root**: Find the single-digit sum.
* **Multiplicative Persistence**: Find the number of steps required to reach a single-digit number via repeated digit multiplication.

#### 6. Recreational Mathematics
* **Collatz Length**: Calculate the number of steps to reach 1 in the Collatz sequence.

---

### 🛠️ Technologies/Tools Used

| Component | Description |
| :--- | :--- |
| **Language** | Python 3.x |
| **Environment** | Jupyter Notebook (or any Python IDE) |
| **Libraries** | Standard Library (`math`, `random`) – No third-party packages required. |

---

### ⚙️ Steps to Install & Run the Project

1.  **Prerequisites:** Ensure you have **Python 3.x** installed on your system.
2.  **Install Jupyter (Optional but Recommended):** For the best interactive experience, install Jupyter Notebook or JupyterLab:
    ```bash
    pip install notebook
    # OR
    pip install jupyterlab
    ```
3.  **Download the File:** Save the notebook file named `vityarthi.ipynb` to your local machine.
4.  **Run the Notebook:**
    * Open your terminal/command prompt and navigate to the directory where you saved the file.
    * Start the Jupyter environment:
        ```bash
        jupyter notebook
        # OR
        jupyter lab
        ```
    * Your web browser will open. Click on the `vityarthi.ipynb` file to open the project.

---

### ✅ Instructions for Testing

The provided notebook is already pre-tested. Each function is followed by example usage and exception handling blocks to demonstrate its correctness and validate input constraints.

To test a specific function:

1.  **Select a Cell:** Click on the code cell containing the function definition and example usage (e.g., the cell with `def is_abundant(n):`).
2.  **Modify Test Data:** Edit the example usage lines at the bottom of the cell (e.g., change `is_abundant(12)` to `is_abundant(20)`).
3.  **Execute the Cell:** Press `Shift + Enter` or click the "Run" button in the toolbar. The output will immediately show the test result, including any caught `ValueError` for incorrect inputs.

