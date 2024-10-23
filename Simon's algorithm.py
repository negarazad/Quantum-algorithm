from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def simons_algorithm(secret):
    n = len(secret)
    qc = QuantumCircuit(n*2, n)

    # اعمال گیت های هادامارد
    for qubit in range(n):
        qc.h(qubit)
    
    # اعمال گیت های اوراکل
    qc.barrier()
    for i in range(n):
        if secret[i] == '1':
            qc.cx(i, i+n)

    # اعمال گیت های هادامارد به نیمه اول کیوبیت ها
    qc.barrier()
    for qubit in range(n):
        qc.h(qubit)
    
    # اندازه گیری
    qc.measure(range(n), range(n))

    # اجرا و نمایش نتیجه
    simulator = Aer.get_backend('qasm_simulator')
    result = execute(qc, simulator, shots=1024).result()
    counts = result.get_counts(qc)
    print(counts)
    plot_histogram(counts)
    plt.show()

# مثال استفاده از تابع با رشته دوره ای "110"
simons_algorithm("110")
