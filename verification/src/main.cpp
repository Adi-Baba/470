#include <iostream>
#include <vector>
#include <cmath>
#include "number_theory.hpp"
#include "subset_sum.hpp"

using namespace std;

// Generate c-exceptional prime chain
vector<uint64_t> generate_c_chain(double c, int k) {
    vector<uint64_t> chain;
    chain.push_back(3);
    for (int i = 1; i < k; ++i) {
        uint64_t target = floor(c * chain.back());
        chain.push_back(nt::next_prime(target));
    }
    return chain;
}

int main() {
    cout << "Erdos Problem 470 - Paper 9 Verification Suite" << endl;
    cout << "===============================================" << endl;
    
    // Verify L_c calculation for c = 1.4
    double c = 1.4;
    int k = 8;
    vector<uint64_t> chain = generate_c_chain(c, k);
    
    cout << "\nChain for c = " << c << " (k = " << k << "): ";
    uint64_t N = 1;
    for (uint64_t p : chain) {
        cout << p << " ";
        N *= p;
    }
    cout << "\nMinimal N: " << N << endl;
    
    if (nt::is_abundant(N)) {
        cout << "N is abundant!" << endl;
        uint64_t excess = nt::excess(N);
        cout << "Excess E(N) = " << excess << endl;
        
        vector<uint64_t> divs = nt::proper_divisors(N);
        cout << "Checking pseudoperfectness with DP bitset..." << endl;
        
        // DP check
        bool is_pseudo = dp::is_subset_sum(divs, excess);
        if (is_pseudo) {
            cout << "Verified: N is pseudoperfect." << endl;
        } else {
            cout << "Result: N is weird! (Wait, this shouldn't happen for tested bounds)" << endl;
        }
    } else {
        cout << "N is deficient." << endl;
    }
    
    return 0;
}
