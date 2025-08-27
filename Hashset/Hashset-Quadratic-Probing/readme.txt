1. no linked list
2. quadratic probing
3. detetion with tombstone markers
4. better hash function to reduce clusturing
5. load factor monitoring
6. size tracking, capacity management/dynamic resizing


Why 31?
1. Prime Number Benefits
31 is a prime number, which helps distribute hash values more evenly across the table. Prime numbers reduce clustering because they don't share common factors with the table size.

2. Odd Number Property
31 is odd, which is important because multiplying by an even number could lose information (specifically, the least significant bit).

3. Performance Optimization
31 has a special property: 31 * x can be optimized by compilers/JVMs as (x << 5) - x (bit shift left by 5, then subtract x), which is faster than multiplication.

4. Empirically Good Results
31 has been tested extensively and provides good hash distribution in practice.