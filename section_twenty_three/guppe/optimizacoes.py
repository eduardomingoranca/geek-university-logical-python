import collections
from timeit import timeit

import sys

Pessoa = collections.namedtuple('Pessoa', 'nome email')

felicity = Pessoa('Felicity Jones', 'felicity@gmail.com')

print(timeit('felicity.email', globals=globals()))

print(sys.getsizeof(list(range(29082020))))
