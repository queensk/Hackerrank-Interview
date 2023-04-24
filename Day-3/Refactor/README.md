# optimize code
given this 
```
var yourself = {
    fibonacci : function(n) {
        if (n === 0) {
            return 0;
        } else if (n === 1) {
            return 1;
        } else {
            return this.fibonacci(n - 1) +
                this.fibonacci(n - 2);
        }
    }
};
```
The given code implements the Fibonacci sequence using a recursive function. However, the code can be refactored to make it more efficient by using memoization. Memoization is a technique where the result of a function call is cached so that subsequent calls with the same arguments can be returned from the cache instead of recalculating the result.