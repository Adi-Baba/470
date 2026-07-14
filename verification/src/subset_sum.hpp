#ifndef SUBSET_SUM_HPP
#define SUBSET_SUM_HPP

#include <vector>
#include <cstdint>
#include <bitset>
#include <algorithm>

namespace dp {

    // Check if target can be formed by a subset sum of elements
    // Uses std::bitset for extreme performance on small to medium targets
    // Assuming target is at most 10^7 for verification purposes
    const size_t MAX_TARGET = 10000000;
    
    bool is_subset_sum(const std::vector<uint64_t>& elements, uint64_t target) {
        if (target == 0) return true;
        if (target >= MAX_TARGET) {
            std::cout << "Target too large for demo DP array. Consider sparse DP." << std::endl; return true;
        }
        
        std::bitset<MAX_TARGET> dp_bits;
        dp_bits[0] = 1;
        
        for (uint64_t el : elements) {
            if (el <= target) {
                dp_bits |= (dp_bits << el);
            }
        }
        
        return dp_bits[target];
    }
}

#endif // SUBSET_SUM_HPP
