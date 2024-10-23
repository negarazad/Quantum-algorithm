from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def phase_estimation(unitary, eigenstate, precision):
    n = len(eigenstate)
    qc = QuantumCircuit(precision + n, precision)

    # اعمال هادامارد به کیوبیت‌های محاسبه
    for q in range(precision):
        qc.h(q)

    # کپی کردن حالت ورودی به گیت‌های پشتی
    qc.append(eigenstate.to_instruction(), range(precision, precision + n))

    # اعمال گیت‌های کنترل شده
    for q in range(precision):
        qc.append(unitary.control(), [q] + list(range(precision, precision + n)))

    # اعمال QFT معکوس
    qc.append(QFT(precision).inverse(), range(precision))

    # اندازه‌گیری
    qc.measure(range(precision), range(precision))

    return qc

# مثال استفاده از الگوریتم چرخش فاز کوانتومی
unitary = QuantumCircuit(1)
unitary.p(1.23, 0)  # چرخش فاز
eigenstate = QuantumCircuit(1)
eigenstate.h(0)
qc = phase_estimation(unitary, eigenstate, precision=3)

# اجرا و نمایش نتیجه
simulator = Aer.get_backend('qasm_simulator')
result = execute(qc, simulator, shots=1024).result()
counts = result.get_counts(qc)
print(counts)
plot_histogram(counts)
plt.show()
