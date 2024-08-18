from qiskit import QuantumCircuit
import math


def solve() -> QuantumCircuit:
    qc = QuantumCircuit(1)
    # Write your code here:
    qc.rz(2*math.pi, 0)

    return qc
