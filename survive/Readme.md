# Problem Statement

You are a poor person in an island. There is only one shop in this island, this shop is open on all days of the week except for Sunday. Consider following constraints:

N – Maximum unit of food you can buy each day.
S – Number of days you are required to survive.
M – Unit of food required each day to survive.
Currently, it’s Monday, and you need to survive for the next S days. 
**Find the minimum number of days (ceil value) on which you need to buy food from the shop so that you can survive the next S days,** or determine that it isn’t possible to survive.

Input Format:
The first line of the input contains three numbers S, N and M separated by space.

Output Format:
If it is possible to survive the print the number of days, otherwise print 'NO' without quotes.

Example-1

Input:
10 16 2

Output:
2


Example-2

Input:
10 20 30

Output:
NO

Explanation 1: One possible solution is to buy a box on the first day (Monday), it’s sufficient to eat from this box up to 8th day (Monday) inclusive. Now, on the 9th day (Tuesday), you buy another box to survive the 9th and 10th day.

Explanation 2: You can’t survive even if you buy food because the maximum number of units you can buy in one day is less the required food for one day.