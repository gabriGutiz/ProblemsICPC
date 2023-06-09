
#include <iostream>

int factorial(int n) {
  return n <= 1 ? 1 : n * factorial(n - 1);
}

int numberFactorial(int input) {
  int result = 0;
  while (input > 0) {
    int aux = factorial(input);
    int i = 0;
    while (aux > input) {
      i++;
      aux = factorial(input - i);
    }
    result++;
    input = input - aux;
  }
  return result;
}

int main () {
  int N;

  std::cin >> N;
  std::cout << numberFactorial(N) << std::endl;

  return 0;
}
