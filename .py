# Consider a sequence u where u is defined as follows:

# The number u(0) = 1 is the first one in u.
# For each x in u, then y = 2 * x + 1 and z = 3 * x + 1 must be in u too.
# There are no other numbers in u.
# Example:

# u = [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, ...]

# 1 gives 3 and 4, then 3 gives 7 and 10, 4 gives 9 and 13, then 7 gives 15 and 22 and so on...

# Task:

# Given parameter n the function dbl_linear (or dblLinear...) returns the element u(n) of the ordered sequence u (ordered with < so there are no duplicates) .

# Example:

# dbl_linear(10) should return 22

# Note:

# Focus attention on efficiency

# Solution in JavaScript #

function dblLinear(n) {
    let x = 1;
    let y = [];
    let z = [];
    for (let i = 0; i < n; i += 1) {
      y.push(x * 2 + 1);
      z.push(x * 3 + 1);
      
      let min = Math.min(y[0], z[0])
      if (min === y[0]) x = y.shift();
      if (min === z[0]) x = z.shift();
    }
    return x
}

# Solution in Python #

def dbl_linear(n):
    u = [1]
    i = 0
    j = 0
    while len(u) <= n:
        x = 2 * u[i] + 1
        y = 3 * u[j] + 1
        if x <= y:
            i += 1
        if x >= y:
            j += 1
        u.append(min(x,y))
    return u[n]

