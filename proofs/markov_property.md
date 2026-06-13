# Markov Property

## Setting up the Markov Property

Initialize, by fixing k, defining the state space:

    S = {0, 1, 2, ..., 2^(k)-1}

## Claim and Why?

The residue class of T^(k)(n) depends only on the residue class of n only. Hence, when we derive both the formulas: we get a main point. That is, n only appears in the term 3^(s) * n, and 3^(s) * n mod 2^(2k) depends only on mod 2^(k). Hence, the two integers in the same residue class always land in the same residue class after k number of steps.  