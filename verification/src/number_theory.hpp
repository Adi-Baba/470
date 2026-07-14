#ifndef NUMBER_THEORY_HPP
#define NUMBER_THEORY_HPP

#include <vector>
#include <cstdint>
#include <cmath>
#include <iostream>

namespace nt {

    // Check if a number is prime
    bool is_prime(uint64_t n) {
        if (n <= 1) return false;
        if (n <= 3) return true;
        if (n % 2 == 0 || n % 3 == 0) return false;
        for (uint64_t i = 5; i * i <= n; i += 6) {
            if (n % i == 0 || n % (i + 2) == 0) return false;
        }
        return true;
    }

    // Get the next prime strictly greater than n
    uint64_t next_prime(uint64_t n) {
        if (n < 2) return 2;
        uint64_t p = (n % 2 == 0) ? n + 1 : n + 2;
        while (!is_prime(p)) {
            p += 2;
        }
        return p;
    }

    // Get all proper divisors of n
    std::vector<uint64_t> proper_divisors(uint64_t n) {
        std::vector<uint64_t> divs;
        for (uint64_t i = 1; i * i <= n; ++i) {
            if (n % i == 0) {
                divs.push_back(i);
                if (i * i != n && i != 1) {
                    divs.push_back(n / i);
                }
            }
        }
        return divs;
    }

    // Calculate sum of proper divisors (sigma(n) - n)
    uint64_t aliquot_sum(uint64_t n) {
        uint64_t sum = 0;
        for (uint64_t d : proper_divisors(n)) {
            sum += d;
        }
        return sum;
    }

    // Determine if n is abundant
    bool is_abundant(uint64_t n) {
        return aliquot_sum(n) > n;
    }

    // Get the excess E(N) = sigma(N) - 2N = aliquot_sum(N) - N
    uint64_t excess(uint64_t n) {
        return aliquot_sum(n) - n;
    }
}

#endif // NUMBER_THEORY_HPP
