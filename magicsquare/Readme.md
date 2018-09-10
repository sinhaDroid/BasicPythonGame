# Magic Square

## Magic Square of size 3

    [2  7   6]

    [9  5   1]

    [4  3   8]

## Magic Square of size 5

    [9  3   22  16  15]

    [2  21  20  14  8]

    [25 19  13  7   1]

    [18 12  6   5   24]

    [11 10  4   23  17]

## Fact

M = n(nˆ2 + 1)/2

## Steps

* In any magic square, 1 is located at position (n/2, n-1).
* Let's say the position of 1 i.e. (n/2, n-1) is (p, q), then next number which is 2 is located at (p-1, q+1) position. Anytime if the calculated row position becomes -1 then make it n-1 and if column position becomes n then make it 0.
* If the calulated position already contains a number then decrement the column by 2 and increment the row by 1.
* If anytime row position becomes -1 and column becomes n, switch it to (0, n-2).