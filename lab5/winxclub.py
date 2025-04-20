import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, CheckButtons
from scipy import signal


amp = 1.0
freq = 2.0
phase = 0.0
mean = 0.0
dis = 0.2
cutf = 0.2
show1 = False
show2 = True


fig, ah = plt.subplots(figsize=(10, 6))
plt.subplots_adjust(left=0.1, bottom=0.35, right=0.9, top=0.95)
t = np.linspace(0, 2 * np.pi, 1000)

def monica(t, amp, freq, phase):
    return amp * np.sin(freq * t + phase)

def filter_signal(data, cutoff, order=3):
    b, a = signal.butter(order, cutoff, 'low')
    return signal.filtfilt(b, a, data)

shchas = np.random.normal(mean, dis, len(t))

harm = monica(t, amp, freq, phase)
filtr = filter_signal(harm + shchas, cutf)

line, = ah.plot(t, harm, lw=2, color='#4ac7c3')
noise, = ah.plot(t, harm + shchas, lw=1, color='#a4deb6', alpha=0)
line2, = ah.plot(t, filtr, lw=2, color='#ff7f50', alpha=1.0)

ah.set_ylim(-2.5, 2.5)


s = [
    ('Амплітуда', 0.1, 2.0, amp, [0.15, 0.25, 0.6, 0.03]),
    ('Частота', 0.1, 4.0, freq, [0.15, 0.21, 0.6, 0.03]),
    ('Фаза', -np.pi, np.pi, phase, [0.15, 0.17, 0.6, 0.03]),
    ('Середнє шуму', -1.0, 1.0, mean, [0.15, 0.13, 0.6, 0.03]),
    ('Дисперсія шуму', 0.0, 1.0, dis, [0.15, 0.09, 0.6, 0.03]),
    ('Частота фільтру', 0.01, 0.5, cutf, [0.15, 0.05, 0.6, 0.03])
]

slider = {}
for label, min, mah, vin, pos in s:
    ah_slider = plt.axes(pos)
    slider[label] = Slider(ah_slider, label, min, mah, valinit=vin)


button = Button(plt.axes([0.82, 0.13, 0.1, 0.04]), 'Reset')
check = CheckButtons(plt.axes([0.82, 0.05, 0.15, 0.07]), ['Show Noise', 'Show filter'], [show1, show2])


def update1(val):
    global harm
    amp = slider['Амплітуда'].val
    freq = slider['Частота'].val
    ph = slider['Фаза'].val
    harm = monica(t, amp, freq, ph)
    line.set_ydata(harm)

    if show1:
        noise.set_ydata(harm + shchas)
        noise.set_alpha(0.7)
    else:
        noise.set_alpha(0)

    filtr = filter_signal(harm + shchas, slider['Частота фільтру'].val)
    line2.set_ydata(filtr)
    line2.set_alpha(1.0 if show2 else 0)

    fig.canvas.draw_idle()


def update2(val):
    global shchas
    mean = slider['Середнє шуму'].val
    dis = slider['Дисперсія шуму'].val
    shchas = np.random.normal(mean, dis, len(t))
    update1(val)


def checkbox(label):
    global show1, show2
    if label == 'Show Noise':
        show1 = not show1
    elif label == 'Show filter':
        show2 = not show2
    update1(None)


def reset(fe):
    global show1, show2, shchas
    for s in slider.values():
        s.reset()
    shchas = np.random.normal(mean, dis, len(t))
    if check.get_status()[0]:
        check.set_active(0)
    if not check.get_status()[1]:
        check.set_active(1)
    show1 = False
    show2 = True
    update1(None)


slider['Амплітуда'].on_changed(update1)
slider['Частота'].on_changed(update1)
slider['Фаза'].on_changed(update1)
slider['Середнє шуму'].on_changed(update2)
slider['Дисперсія шуму'].on_changed(update2)
slider['Частота фільтру'].on_changed(update1)
check.on_clicked(checkbox)
button.on_clicked(reset)

plt.show()
