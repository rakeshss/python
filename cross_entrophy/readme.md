Cross-Entropy (CE):
<br>

CE brings the concept of Probability and error Function. Through CE you can define or predict whether model is good or bad.

So on high level, idea is we should pick the model with less CE. 

Steps:

1. Define probability of the events.  
   p1 * p2 * p3 ...

2. Take the summation of probability. 
   log(p1) + log(p2) + log (p3) ...

3. Take negative of above probability value, the reason being P(0.6) ~ - 0.51 . probability of any value between 0 to 1 is negative &  
   p(1) = 0
    
    CE = - (log(p1) + log(p2) + log (p3)) 



