# Ergodocity

## Meaning

A markov chain is considered ergodic if it has a unique stationary distribution that each and every state converges to. Hence, there are two conditions:

1. Irreducibility
2. Aperiodicity

## Irreducibility

A chain is irreducible if you can move from one state to another state in a finite number of steps. 

## Aperiodicity

A chain is aperiodic if the Greatest Common Divisior (gcd) of return times to each state is 1. 

## Conclusion

Irreducible + Aperiodic:

    P^(m)[r, s] > pi[s] as m --> infinity 