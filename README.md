# Erdős Problem 470: c-Exceptional Numbers & Structural Constraints

This repository contains the finalized manuscript and computational verification suite for **Paper 9: c-Exceptional Numbers and Structural Constraints on Odd Weird Numbers**.

## Overview
Erdős Problem #470 asks whether any odd weird numbers exist. This paper achieves a massive **conditional reduction** of the problem, systematically narrowing the search space into an extremely tight mathematical corner.

The core results prove that any potential odd weird number must possess at least 4 distinct prime factors ($k \ge 4$) and adhere to strict "near-perfect" abundancy constraints governed by the $M$-core framework. The $c$-exceptional structure allows us to unconditionally eliminate broad classes of integers where the minimum consecutive divisor ratio is bounded by $c^* = 17/11$.

## Repository Structure

*   **`manuscript/`**
    *   `Paper9_ErdosProblem470.md`: The original markdown draft of the paper.
    *   `latex/main.tex`: The pure, finalized LaTeX source code for the submission.
    *   `latex/main.pdf`: The beautifully compiled 25-page, publication-ready manuscript.
*   **`verification/`**
    *   Modular C++ suite designed to verify pseudoperfectness bounds and the exact excess recursion algorithms ($E(M_q) = qE(M) + \sigma(M)$).
    *   Utilizes a highly optimized `std::bitset` dynamic programming approach to validate subset sums for extremely large abundancy bounds.

## Compilation Instructions

### 1. LaTeX Manuscript
The paper is written using standard LaTeX packages. To compile the source code natively into a PDF:
```bash
cd manuscript/latex
lualatex main.tex
```

### 2. C++ Verification Suite
The verification code is written in C++17. To compile and run the suite:
```bash
cd verification
make
./verify_paper9
```

## Author
*   **Aditya Kumar** (India)

---
*Note: This manuscript establishes that unconditional closure of the k ≥ 4 regime is the final barrier to a complete resolution of Erdős Problem 470.*
