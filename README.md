# Markow Chains:

NOTE: For this I use the Quantecon Library.  
This is an example file using Markov Chains to see the dynamics of the labor
market.  

Consider the following stochastic process that describes 3 states of the labor
market:
1. Being employed in a formal job
2. Being employed in an informal job
3. Being unemployed

- If a person is employed in a formal job in the t period: $/rho_1$ is the probability
of staying formal in t+1; s1 is the probability of moving to an informal job in
t+1 and, finally; 1-p1-s1 is the probability of changing to unemployed in t+1.  

- If a person is employed in a formal job in the t period: p1 is the probability
of staying formal in t+1; s1 is the probability of moving to an informal job in
t+1 and, finally; 1-p1-s1 is the probability of changing to unemployed in t+1.  
