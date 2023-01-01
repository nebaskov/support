import numpy as np
import matplotlib.pyplot as plt

t = np.arange(start=0, stop=100, step=0.1)
step = 0.1

tau = 20
T = 30
U = 4

# rectangular pulse
rect = np.zeros((t.shape[0]))
k=1

for n in range(1, t.shape[0]):
    if t[n] <= (t[int(k)] + tau):
        rect[n] = U
    elif t[n] <= (t[int(k)] + T):
        rect[n] = 0
    else:
        k += T / step
    
# spectral density of rect pulse
w = np.arange(start=-100, stop=100, step=0.1)
k1 = 6
s = np.zeros((w.shape[0],))

for i in range(1, w.shape[0]):
    if w[i] == 0:
        s[i] = (tau * U * np.sin(k1 * w[i-1] * tau / (T * 2))) / (T * k1 * w[i-1] * tau / 2)
    else:
        s[i] = (tau * U * np.sin(k1 * w[i] * tau / (T * 2))) / (T * k1 * w[i] * tau / 2)

fig, ax = plt.subplots(1, 2)
ax[0].plot(t, rect, label='rectangular pulse')
ax[0].set_ylim(0, U+0.5)
ax[0].set_xlabel('t, ms')
ax[0].set_ylabel('rectangle pulse')
ax[0].legend(loc='upper right')

ax[1].plot(w, abs(s.real), label='spectral density')
ax[1].set_xlabel('w, MHz')
ax[1].set_ylabel('spectral density')
ax[1].legend(loc='upper right')

fig.suptitle('Rectangular pulse and its spectral density')
plt.show()