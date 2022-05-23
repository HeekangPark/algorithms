#include <stdio.h>

int _;
int N;
int ys[15];
int count = 0;

bool canPlace(int x, int y)
{
  for (int i = 0; i < x; i++)
  {
    if (ys[i] == y)
      return false;
    if (y - ys[i] > 0 && x - i == y - ys[i])
      return false;
    if (ys[i] - y > 0 && x - i == ys[i] - y)
      return false;
  }
  return true;
}

void search(int x) {
  if (x == N) {
    count++;
    return;
  }

  for (int y = 0; y < N; y++) {
    if (canPlace(x, y)) {
      ys[x] = y;
      search(x + 1);
    }
  }
}

int main()
{
  _ = scanf("%d", &N);
  search(0);
  printf("%d\n", count);
  return 0;
}