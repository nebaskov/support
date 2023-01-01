import numpy as np
import matplotlib.pyplot as plt

ph = np.pi
x = np.arange(start=-np.pi, stop=np.pi, step=0.01)
r = np.zeros((20,))
W = np.zeros((20,))

for n in range(1, 20):

    func = np.cos(5 * x * n + ph)
    fft_ = np.fft.fft(func)

    r[n] = max(abs(fft_.real))

    w = np.divide(1, x)
    W[n] = 1 / (5*n)
    
r = np.delete(r, 0)
W = np.delete(W, 0)

fig, ax = plt.subplots(1, 2)
ax[0].plot(w, abs(fft_.real), label='harmonic pulse')
ax[0].set_xlim(-0.5, 0.5)
ax[0].set_xlabel(r'w, $- \pi < w < \pi$')
ax[0].set_ylabel('kW')
ax[0].legend(loc='upper right')

ax[1].plot(W, r, label='amplitude')
ax[1].set_xlabel(r'w, $- \pi < w < \pi$')
ax[1].set_ylabel('kW')
ax[1].legend(loc='upper right')

fig.suptitle('Harmonic pulse and its amplitude')
plt.show()
    