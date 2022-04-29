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

    def getGCD(self, a, b):
        a = self.factorize(a)
        b = self.factorize(b)

        result = 1
        for p in a.keys() & b.keys():
            result *= (p ** min(a[p], b[p]))
        
        return result
    
    def getLCM(self, a, b):
        a = self.factorize(a)
        b = self.factorize(b)

        result = 1
        for p in a.keys() | b.keys():
            result *= (p ** max((a[p] if p in a.keys() else 1), (b[p] if p in b.keys() else 1)))
        
        return result

module = PrimeModule()
a, b = map(int, input().split())
print(module.getGCD(a, b))
print(module.getLCM(a, b))
