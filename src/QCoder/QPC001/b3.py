from qiskit import QuantumCircuit
from qiskit.circuit.library import ZGate


def solve(n: int, L: int) -> QuantumCircuit:
    qc = QuantumCircuit(n)
    # Write your code here:
    for l in range(L):
        for d in range(n):
            if (1<<d) & l == 0:
                qc.x(d)
        if n > 1:
            qc.append(ZGate().control(n-1), range(n))
        else:
            qc.z(0)
        for d in range(n):
            if (1<<d) & l == 0:
                qc.x(d)

    return qc
