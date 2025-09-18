"""
Módulo que implementa el algoritmo de Torres de Hanói.
Muestra paso a paso cómo mover los discos entre las torres.
"""

NUMBER_OF_DISKS = 5
A = list(range(NUMBER_OF_DISKS, 0, -1))
B = []
C = []

def move(n, source, auxiliary, target):
    """
    Mueve "n" discos de la torre "source" a la torre "target" 
    usando "auxiliary" como torre auxiliar.

    Args:
        n (int): número de discos a mover
        source (list): torre de origen
        auxiliary (list): torre auxiliar
        target (list): torre de destino
    """
    if n <= 0:
        return
    # move n - 1 disks from source to auxiliary, so they are out of the way
    move(n - 1, source, target, auxiliary)
    # move the nth disk from source to target
    target.append(source.pop())
    # display our progress
    print(A, B, C, '\n')
    # move the n - 1 disks that we left on auxiliary onto target
    move(n - 1,  auxiliary, source, target)
# initiate call from source A to target C with auxiliary B
move(NUMBER_OF_DISKS, A, B, C)
