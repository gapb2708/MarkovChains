# Markow Chains:

NOTE: For this I use the Quantecon Library.  

This is an example file using Markov Chains to see the dynamics of the labor market.  

Consider the following stochastic process that describes 3 states of the labor market:
1. Being employed in a formal job
2. Being employed in an informal job
3. Being unemployed

- If a person is employed in a formal job in the $t$ period: $\rho_{1}$ is the probability of staying formal in $t+1$; $s_{1}$ is the probability of moving to an informal job in $t+1$ and, finally; $1-\rho_{1}-s_{1}$ is the probability of changing to unemployed in $t+1$.  

- If a person is employed in an informal job in the $t$ period: $s_{2}$ is the probability of changing to a formal job in $t+1$; $\rho_{2}$ is the probability of staying in an informal job in $t+1$ and, finally; $1-\rho_{2}-s_{2}$ is the probability of changing to unemployed in $t+1$.  

- If a person is unemployed in in $t$: $f_{1}$ is the probability of finding a formal job in $t+1$; $f_{2}$ is the probability of finding an informal job in $t+1$ and, finally; $1-f_{1}-f_{2}$ is the probability of staying unemployed in $t+1$.

The Initial state matrix looks like:

$ \begin{bmatrix}
e \\
u \\
1-e-u
\end{bmatrix}  $
