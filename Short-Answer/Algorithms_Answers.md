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

This is a binary search algorithm. This works since, by definition, the "floors" are already sorted lowest to highest.

The Big O is Logarithmic - O(log n)

```
function(n = floors, f = lowest floor that egg breaks)

lowest_floor = 0
highest_floor = n # number of floors given to us

middle = (highest_floor - lowest_floor) // 2 #splitting in half with int div. (finding the middle)

if middle == f: # egg doesn't break below this point
return middle # this is the answer!

elif middle < f: # egg doesn't break
return function(n[:middle]) #recursive call to check the bottom half of floors using a slice

else:
return function(n[middle:]) #recursice call to check the top half of floors using a slice
```
