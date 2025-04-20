import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, CheckButtons

amp = 1.0
freq = 2.0
phase = 0.0
mean = 0.0
dis = 0.2
show = False 

fig, ah = plt.subplots(figsize=(10, 6))
plt.subplots_adjust(0.1, 0.35, 0.9, 0.95)
t = np.linspace(0, 2*np.pi, 1000)

def monica(t, amp, freq, phase):
    return amp * np.sin(freq * t + phase)

shchas = np.random.normal(mean, dis, len(t))

harm = monica(t, amp, freq, phase)
line, = ah.plot(t, harm, lw=2, color='#4ac7c3')
noise, = ah.plot(t, harm + shchas, lw=1, color='#a4deb6', alpha=0)

ah.set_ylim(-2.5 , 2.5)

s = [
    ('Амплітуда', 0.1, 2.0, amp, [0.15, 0.25, 0.6, 0.03]),
    ('Частота', 0.1, 4.0, freq, [0.15, 0.20, 0.6, 0.03]),
    ('Фаза', -np.pi, np.pi, phase, [0.15, 0.15, 0.6, 0.03]),
    ('Середнє шуму', -1.0, 1.0, mean, [0.15, 0.10, 0.6, 0.03]),
    ('Дисперсія шуму', 0.0, 1.0, dis, [0.15, 0.05, 0.6, 0.03])
]

slider = {}
for label, min, mah, vin, pos in s:
    slider[label] = Slider(plt.axes(pos), label, min, mah, valinit=vin)

button = Button(plt.axes([0.82, 0.11, 0.1, 0.04]), 'Reset')
check = CheckButtons(plt.axes([0.82, 0.05, 0.12, 0.05]), ['Show Noise'], [show])

def update1(val):
    amp = slider['Амплітуда'].val
    freq = slider['Частота'].val
    phase = slider['Фаза'].val

    harm = monica(t, amp, freq, phase)
    line.set_ydata(harm)

    if show:
        noise.set_ydata(harm + shchas)
        noise.set_alpha(0.7)
    else:
        noise.set_alpha(0)
    fig.canvas.draw_idle()

def update2(val):
    global shchas
    mean = slider['Середнє шуму'].val
    dis = slider['Дисперсія шуму'].val
    shchas = np.random.normal(mean, dis, len(t))
    update1(val)

def checkbox(label):
    global show
    if label == 'Show Noise':
        show = not show
    update1(None)

def reset(fe):
    global show, shchas
    for s in slider.values():
        s.reset()
    shchas = np.random.normal(mean, dis, len(t))
    if check.get_status()[0]:  
        check.set_active(0)
    show = False
    update1(None)

slider['Амплітуда'].on_changed(update1)
slider['Частота'].on_changed(update1)
slider['Фаза'].on_changed(update1)
slider['Середнє шуму'].on_changed(update2)
slider['Дисперсія шуму'].on_changed(update2)
check.on_clicked(checkbox)
button.on_clicked(reset)

plt.show()
