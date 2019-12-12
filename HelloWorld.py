from qiskit import *
import matplotlib.pyplot as plt
from qiskit.tools.visualization import plot_bloch_multivector
#print(qiskit.__qiskit_version__)

#IBMQ.save_account('91ac609d8242a851c6be3331095032c16bfddeb995d03f482ec9cafd81570246dbab4a343c0c175eb0b7cc3bf02ef5e0099610ddfe05ae756f5889ef8ce0a6eb')
#IBMQ.load_account()

qr = QuantumRegister(2)
cr = ClassicalRegister(2)

circuit = QuantumCircuit(qr, cr)

#circuit.h(qr[0])

circuit.cx(qr[0], qr[1])

circuit.measure(qr, cr)

simulator = Aer.get_backend('qasm_simulator')

result = execute(circuit, backend=simulator).result()

from qiskit.tools.visualization import plot_histogram

plot_histogram(result.get_counts(circuit))

#circuit.draw(output='mpl')
plt.show()

print(circuit)