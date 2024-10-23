from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# تابع اوراکل برای جستجوی مقدار هدف
def oracle(circuit, qubits, target):
    for i, qubit in enumerate(qubits):
        if target[i] == '0':
            circuit.x(qubit)
    circuit.h(qubits[-1])
    circuit.mcx(qubits[:-1], qubits[-1])
    circuit.h(qubits[-1])
    for i, qubit in enumerate(qubits):
        if target[i] == '0':
            circuit.x(qubit)

# تابع گام گروور
def grover_step(circuit, qubits):
    circuit.h(qubits)
    for qubit in qubits:
        circuit.x(qubit)
    circuit.h(qubits[-1])
    circuit.mcx(qubits[:-1], qubits[-1])
    circuit.h(qubits[-1])
    for qubit in qubits:
        circuit.x(qubit)
    circuit.h(qubits)

# تعداد کیوبیت‌ها
n = 3

# تعریف کیوبیت‌ها و مدار کوانتومی
qubits = list(range(n))
circuit = QuantumCircuit(n, n)

# اعمال دروازه‌های هادامارد به تمام کیوبیت‌ها
circuit.h(qubits)

# اوراکل برای جستجوی مقدار هدف (مثلاً '101')
oracle(circuit, qubits, '101')

# اعمال گام گروور
grover_step(circuit, qubits)

# اندازه‌گیری کیوبیت‌ها
circuit.measure(qubits, qubits)

# اجرا در شبیه‌ساز Aer
simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit, simulator, shots=1024).result()
counts = result.get_counts(circuit)

# نمایش نتایج
print(counts)
plot_histogram(counts)
plt.show()
