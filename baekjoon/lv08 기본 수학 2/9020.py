class PrimeModule:
    def __init__(self, max_num=10000):
        self._primes = [False, False]
        self._max_num = 1
        self._buildPrimes(max_num)
    
    def _buildPrimes(self, max_num):
        self._primes += [True] * ((max_num - self._max_num))
        self._primes[0] = False
        self._primes[1] = False

        for i in range(self._max_num + 1, max_num + 1):
            if self._primes[i]:
                for j in range(i * i, max_num + 1, i):
                    self._primes[j] = False

        self._max_num = max_num

    def isPrime(self, x):
        if x > self._max_num:
            self._buildPrimes(x)

        return self._primes[x]

    def factorize(self, x):
        if x == 1:
            return {}
        
        if x > self._max_num:
            self._buildPrimes(x)

        result = {}
        primes = self.getPrimes()
        p_idx = 0
        
        while x > 1:
            p = primes[p_idx]
            if x % p == 0:
                if p not in result.keys():
                    result[p] = 0
                
                result[p] += 1
                x //= p
            else:
                p_idx += 1

        return result

    def getPrimes(self):
        return [i for i in range(len(self._primes)) if self._primes[i]]

module = PrimeModule()

T = int(input())
for t in range(T):
    n = int(input())

    x = n // 2
    while x > 1:
        if module.isPrime(x) and module.isPrime(n - x):
            print(x, n - x)
            break
        x -= 1