from qiskit import QuantumCircuit


def solve(n: int) -> QuantumCircuit:
    qc = QuantumCircuit(n)
    # Write your code here:
    qc.h(0)
    qc.cx(0, range(1, n))
    qc.z(0)

    return qc
