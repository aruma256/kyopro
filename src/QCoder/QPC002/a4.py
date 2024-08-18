from qiskit import QuantumCircuit


def solve(n: int) -> QuantumCircuit:
    qc = QuantumCircuit(n)
    # Write your code here:
    qc.h(0)
    d = 1
    while d < n:
        for i in range(0, d):
            if i + d < n:
                qc.cx(i, i + d)
        d *= 2
    qc.z(0)

    return qc

# solve(15).draw('mpl').show()
