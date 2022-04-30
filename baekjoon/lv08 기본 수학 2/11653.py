class PrimeModule:
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

    def factorize(self, x):
        if x == 1:
            return {}
        
        if x > self._max_num:
            self._buildPrimes(x)

        result = {}
        p_idx = 0
        
        while x > 1:
            p = self._primes[p_idx]
            if x % p == 0:
                if p not in result.keys():
                    result[p] = 0
                
                result[p] += 1
                x //= p
            else:
                p_idx += 1

        return result

n = int(input())
module = PrimeModule(n)
factorize = module.factorize(n)
print('\n'.join(['\n'.join([str(prime)] * num) for prime, num in factorize.items()]))

