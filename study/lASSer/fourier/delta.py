import numpy as np
import matplotlib.pyplot as plt

# delta function
tau = np.arange(start=-10, stop=10, step=0.01)
t0 = tau[1000]
ampl = 1
delta = np.zeros((tau.shape[0],))
for n in range(1, tau.shape[0]):
    if tau[n] == t0:
        delta[n] = ampl
    
# spectral density of the delta function
w = np.arange(start=-100, stop=100, step=0.1)
s = np.exp(-np.imag(1) * w * t0)
    
fig, ax = plt.subplots(1, 2)
ax[0].plot(tau, delta, label='delta function')
ax[0].set_xlabel('t, s')
ax[0].set_ylabel('delta function')
ax[0].legend(loc='upper right')

ax[1].plot(w, s, label='spectral density')
ax[1].set_xlabel('w, Hr')
ax[1].set_ylabel('spectral density')
ax[1].legend(loc='upper right')
fig.suptitle('Delta function and its spectral density')
plt.show()