from qiskit import QuantumCircuit


def solve() -> QuantumCircuit:
    qc = QuantumCircuit(2)
    # Write your code here:
    import math
    qc.ry(4 * math.atan(math.sqrt(6) / (3 + math.sqrt(3))), 0)
    qc.ch(0, 1)
    qc.cx(1, 0)
    return qc
