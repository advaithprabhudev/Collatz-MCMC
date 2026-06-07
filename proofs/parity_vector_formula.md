# Parity Vector Formula

## Definitions and What it really is

When you apply a Collatz Map T repeatedly for an integer n, each step n is either odd or even. If we record these outputs into a form of a binary string, we can get what we call as *parity vectors*.

## Setup

The accelerated collatz map is defined as:

    T(n) = n / 2            if n = 0 (mod 2)
    T(n) = (3n + 1)/ 2      if n = 1 (mod 2)

We, then, fix an integer "n" and apply to T formula. And at every step, we record a parity:

    v_i = T^(i-1)(n) (mod 2)    for i = 1, 2, 3, ..., k

This basically makes the parity vector v = (v_1, v_2, v_3, ... , v_k) till the point of (0, 1)^(k)

## Formula 

Let s = v_1 + v_2 + v_3 + .... + v_k be the number of odd steps required in the first iterations. Then, the formula appears as:

    T^(k)(n) = (3 ^(s) * n + c(v)) / 2^(k)

where:

s - number of 1 in the parity vector
c - a constant that depends only on the vector itself

## Why we need this?

This formula is used for the Markov States, where T^(k)(n) mod 2^(k) depends only on mod 2^(k). Hence, the residue is preserved during the hidden states transitions.

