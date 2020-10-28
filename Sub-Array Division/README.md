# Sub Array Division

Given a chocolate bar, two children, Lily and Ron, are determining how to share it. Each of the squares has an integer on it. <br/>
Lily decides to share a contiguous segment of the bar selected such that:

* The length of the segment matches Ron's birth month, and,
* The sum of the integers on the squares is equal to his birth day.

We must determine how many ways she can divide the chocolate.

Consider the chocolate bar as an array of squares, s=[2,2,1,3,2] . She wants to find segments summing to Ron's birth day, d=4  with a length equalling his birth month, m=2 .
In this case, there are two segments meeting her criteria: [2,2] and [1,3].

Need to complete the birthday function. It should return an integer denoting the number of ways Lily can divide the chocolate bar.

The function birthday has the following parameter(s):

* s: an array of integers, the numbers on each of the squares of chocolate
* d: an integer, Ron's birth day
* m: an integer, Ron's birth month

![Chocolate](https://i.ndtvimg.com/i/2015-06/chocolate_625x350_81434346507.jpg)
