from knapsack import KnapsackInstance, KnapsackSolver


class KnapsackGreedySolver(KnapsackSolver):
    

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

      liste = []
      for i in range(self._inst.size):
          liste.append((self._inst.V[i]/self._inst.W[i], i))
      liste.sort(reverse=True)
      Xopt = [0] * self._inst.size
      w = 0
      v = 0
      for i in range(self._inst.size):
          if w + self._inst.W[liste[i][1]] <= self._inst.C:
              Xopt[liste[i][1]] = 1
              w += self._inst.W[liste[i][1]]
              v += self._inst.V[liste[i][1]]
          else:
              break
      self.weight = w
      self.value = v
      return tuple(Xopt)
        





