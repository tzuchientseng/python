"""
import java.math.BigInteger;

public class Factorial {
    public static void main(String[] args) {
        BigInteger result = factorial(1000);
        System.out.println(result);
    }

    public static BigInteger factorial(int n) {
        BigInteger fact = BigInteger.ONE;
        for (int i = 1; i <= n; i++) {
            fact = fact.multiply(BigInteger.valueOf(i));
        }
        return fact;
    }
} 
"""
"""
#recusive
def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)

print(fact(100))
"""
# 1000!
from functools import reduce
print(reduce(lambda x, y: (x * y), range(1, 1001))) # Time complexity: O(n), Space complexity O(1)。