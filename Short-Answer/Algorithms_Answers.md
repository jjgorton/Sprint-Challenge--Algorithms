#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)
Linear time - O(n)

"while" the loop is conditionally running n^3 times, which would suggest it has a polynomial time, the condition (a) is also increasing by n^2 - which would suggest Logarithmic time. However the exponents of n cancel eachother out leaving the loop running in direct proportion to the size of n - which is Linear time O(n).

b)
Polynomial time - O(n^2)

we have an outer loop occuring n times, and an inner loop accuring 1/2\*n times. Since constants don't count that inner loop can be simplified to n times. Thus multiplying the outer loop by it's body (O(n)), this gives us O(n^2).

c)
Linear O(n)

The recursive loop is running once for each input (bunnies - 1). Which makes it grow in direct proportion it's input, thus O(n).

## Exercise II
