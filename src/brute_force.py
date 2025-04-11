# Exercice https://courses.21-learning.com/runestone/books/published/oci-2224-donc/classic-problems/01-knapsack-short.html#force-brute

from knapsack import KnapsackInstance, KnapsackSolver
from itertools import product


class BruteforceKnapsackSolver(KnapsackSolver):
    """
    >>> kp = KnapsackInstance(W=[13, 13, 13, 10, 24, 11], V=[2600, 2600, 2600, 500, 4500, 960], C=50)
    >>> bfs = BruteforceKnapsackSolver(kp)
    >>> Xopt = bfs.solve()
    >>> Xopt in [(0, 1, 1, 0, 1, 0), (1, 0, 1, 0, 1, 0), (1, 1, 0, 0, 1, 0)]
    True
    >>> bfs.value(Xopt)
    9700
    >>> bfs.weight(Xopt)
    50
    >>> bfs.weight(Xopt) <= bfs._inst.C
    True

    """
    
    def __init__(self, instance:KnapsackInstance) -> None:
        # TODO: write the constructor by calling the parent class constructor
        super().__init__(instance)
        self.weight = None
        self.value = None
        self._inst = instance

    
    def solve(self) -> tuple[int, ...]:
        
        possibilities = list(product([0,1], repeat = self._inst.size))
        Xopt = None
        v_Xopt = 0
        w_Xopt = 0


        w = 0
        v = 0

        for pos in possibilities:
            for i,x in enumerate(pos) :
                w += self._inst.W[i] * x
                v += self._inst.V[i] * x

                if w <= self._inst.C:
                    if v > v_Xopt:
                        v_Xopt = v
                        w_Xopt = w
                        Xopt = pos
        
        self.weight = w_Xopt
        self.value = v_Xopt
        return Xopt