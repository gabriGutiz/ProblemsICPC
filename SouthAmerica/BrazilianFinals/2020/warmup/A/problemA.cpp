
#include <cmath>
#include <iostream>

int minTravels(int maxPopulation, int studentPopulation) {
  if (maxPopulation <= 1)
    return 0;
  return std::ceil((float)studentPopulation / (float)(maxPopulation - 1));
}

int main () {
  int C, A;
  std::cin >> C >> A;

  std::cout << minTravels(C, A) << std::endl;
  return 0;
}

