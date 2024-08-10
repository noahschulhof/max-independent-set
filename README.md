# max-independent-set

## Problem Description

In graph theory, the ***Maximum Independent Set*** of a graph $G = (V, E)$ is defined as the largest subset of vertices $I \subseteq V$ such that no two vertices in $I$ are adjacent. Formally, it satisfies the following conditions:

1. **Independence:** For any two vertices $u, v \in I$, there is no edge $(u, v) \in E$. That is, $\forall u, v \in I, (u, v) \notin E$.
2. **Maximality:** There is no other independent set $I'$ such that $I \subset I'$. That is, $I$ is not strictly a subset of any other independent set in $G$.

The goal is to find such a set $I$ with the maximum possible number of vertices.

## Linear Optimization Formulation

### Decision Variables
Let $x = \{x_i | x_i \in \{0, 1\}\}$ be the set of binary decision variables for each vertex $i \in V$

```math
x_i = \begin{cases} 1, i \in I \\ 0, i \notin I \end{cases}
```

### Constraints
```math
\forall (i, j) \in E, x_i + x_j \leq 1
```

### Objective Function
```math
\max \left( \sum_{i \in V} x_i \right)
```