
#include <iostream>

int getGrade(int gradeOne, int avg) {
  return 2*avg - gradeOne;
}

int main () {
  int A, M;

  std::cin >> A >> M;
  std::cout << getGrade(A, M) << std::endl;
  
  return 0;
}
