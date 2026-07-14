CXX = g++
CXXFLAGS = -O3 -std=c++17 -Wall

all: verify_paper9

verify_paper9: src/main.cpp src/number_theory.hpp src/subset_sum.hpp
	$(CXX) $(CXXFLAGS) src/main.cpp -o verify_paper9

clean:
	rm -f verify_paper9
