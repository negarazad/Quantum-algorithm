from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# ایجاد مدار کوانتومی
qc = QuantumCircuit(3, 2)

# درهم‌تنیدگی جفت کیوبیت‌ها
qc.h(1)
qc.cx(1, 2)

# آماده‌سازی کیوبیت داده و اعمال گیت‌های لازم
qc.cx(0, 1)
qc.h(0)

# اندازه‌گیری کیوبیت‌ها و ارسال نتایج به گیرنده
qc.measure([0, 1], [0, 1])

# مدار کوانتومی برای اعمال گیت‌های اصلاحی
def apply_correction(qc):
    qc.cx(1, 2)
    qc.cz(0, 2)

# افزودن گیت‌های اصلاحی به مدار
apply_correction(qc)

# اجرا در شبیه‌ساز
simulator = Aer.get_backend('qasm_simulator')
result = execute(qc, simulator, shots=1024).result()
counts = result.get_counts(qc)

# نمایش نتایج
print(counts)
plot_histogram(counts)
plt.show()
