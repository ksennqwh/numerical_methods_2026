import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# 1. Функція
# -------------------------------
def M(t):
    return 50 * np.exp(-0.1 * t) + 5 * np.sin(t)

# аналітична похідна
def dM_exact(t):
    return -5 * np.exp(-0.1 * t) + 5 * np.cos(t)

# -------------------------------
# 2. Центральна різниця
# -------------------------------
def central_diff(f, t, h):
    return (f(t + h) - f(t - h)) / (2 * h)

# -------------------------------
# 3. Обчислення
# -------------------------------
t0 = 1

exact = dM_exact(t0)
print("Точне значення:", exact)

h_values = [0.1, 0.01, 0.001]

for h in h_values:
    approx = central_diff(M, t0, h)
    error = abs(approx - exact)
    print(f"h={h} → {approx}, похибка={error}")

# -------------------------------
# 4. Рунге-Ромберг
# -------------------------------
h = 0.01

D_h = central_diff(M, t0, h)
D_h2 = central_diff(M, t0, h / 2)

D_rr = D_h2 + (D_h2 - D_h) / (2**2 - 1)

print("\nРунге-Ромберг:", D_rr)
print("Похибка RR:", abs(D_rr - exact))

# -------------------------------
# 5. Ейткен
# -------------------------------
h1 = 0.1
h2 = 0.05
h3 = 0.025

D1 = central_diff(M, t0, h1)
D2 = central_diff(M, t0, h2)
D3 = central_diff(M, t0, h3)

D_aitken = D1 - ((D2 - D1)**2) / (D3 - 2*D2 + D1)

print("\nЕйткен:", D_aitken)
print("Похибка Ейткена:", abs(D_aitken - exact))

# -------------------------------
# 6. Графік функції
# -------------------------------
t = np.linspace(0, 20, 100)

plt.figure()
plt.plot(t, M(t))
plt.title("M(t)")
plt.grid()

# -------------------------------
# 7. Графік похибки
# -------------------------------
errors = []

for h in np.logspace(-3, -1, 10):
    errors.append(abs(central_diff(M, t0, h) - exact))

plt.figure()
plt.plot(np.logspace(-3, -1, 10), errors, marker='o')
plt.xscale('log')
plt.title("Похибка від h")
plt.grid()

plt.show()