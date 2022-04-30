M = int(input())
N = int(input())

class Prime:
    def __init__(self, max_num=1000):
        self._primes = []
        self._buildPrimes(max_num)
    
    def _buildPrimes(self, max_num):
        self._max_num = max_num

        board = [True] * (max_num + 1)
        board[0] = board[1] = False

        for i in range(2, max_num + 1):
            if board[i]:
                self._primes.append(i)
                for j in range(i * i, max_num + 1, i):
                    board[j] = False

    def isPrime(self, x):
        if x > self._max_num:
            self._buildPrimes(x)

        if x in self._primes:
            return True

prime = Prime(N)
answers = [x for x in range(M, N + 1) if prime.isPrime(x)]
if len(answers) == 0:
    print(-1)
else:
    print(sum(answers))
    print(min(answers))