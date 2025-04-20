import numpy as np
from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, Slider, CheckboxButtonGroup, Button
from bokeh.plotting import figure

amp = 1.0
freq = 2.0
phase = 0.0
mean = 0.0
dis = 0.2
ctf = 0.2

t = np.linspace(0, 2 * np.pi, 1000)

def monica(t, amp, freq, phase):
    return amp * np.sin(freq * t + phase)

def myfilt(data, ctf=0.2):
    fuu = np.fft.fft(data)
    n = len(data)

    mask = np.zeros(n)
    id = int(n * ctf)
    mask[:id] = 1
    mask[n-id+1:] = 1  
    
    spec = fuu * mask
    sign = np.real(np.fft.ifft(spec))
    return sign

harm = monica(t, amp, freq, phase)
shchas = np.random.normal(mean, dis, len(t))
filt = myfilt(harm + shchas, ctf)

sharm = ColumnDataSource(dict(x=t, y=harm))
sfilt = ColumnDataSource(dict(x=t, y=filt))
snoise = ColumnDataSource(dict(x=t, y=harm + shchas))

p = figure(height=500, sizing_mode="stretch_width")
p.line('x', 'y', source=sharm, line_width=2, color="#4ac7c3")
noise = p.line('x', 'y', source=snoise, line_width=1.5, color="#a4deb6")
line2 = p.line('x', 'y', source=sfilt, line_width=2, color="#ff7f50")

p.y_range.start = -2.5
p.y_range.end = 2.5

amp_sl = Slider(start=0.1, end=2.0, value=amp, step=0.1, title="Амплітуда", width=800)
freq_sl = Slider(start=0.1, end=4.0, value=freq, step=0.1, title="Частота", width=800)
phase_sl = Slider(start=-np.pi, end=np.pi, value=phase, step=0.1, title="Фаза", width=800)
mean_sl = Slider(start=-1.0, end=1.0, value=mean, step=0.1, title="Середнє шуму", width=800)
dis_sl = Slider(start=0.0, end=1.0, value=dis, step=0.05, title="Дисперсія шуму", width=800)
filt_sl = Slider(start=0.01, end=0.5, value=ctf, step=0.01, title="Частота фільтру", width=800)


checkbox = CheckboxButtonGroup(labels=["Show noise", "Show filter"], active=[0, 1], width=300)
reset_button = Button(label="Reset", width=300)


def update1(attr, old, new):
    amp = amp_sl.value
    freq = freq_sl.value
    phase = phase_sl.value
    cutoff = filt_sl.value
    
    harm = monica(t, amp, freq, phase)
    sharm.data = dict(x=t, y=harm)
    snoise.data = dict(x=t, y=harm + shchas)
    
    filt = myfilt(harm + shchas, cutoff)
    sfilt.data = dict(x=t, y=filt)
    
    noise.visible = 0 in checkbox.active
    line2.visible = 1 in checkbox.active

def update2(attr, old, new):
    global shchas
    mean = mean_sl.value
    std = dis_sl.value
    shchas = np.random.normal(mean, std, len(t))
    update1(attr, old, new)

def check(attr, old, new):
    update1(attr, old, new)

def reset():
    global shchas

    amp_sl.value = 1.0
    freq_sl.value = 2.0
    phase_sl.value = 0.0
    mean_sl.value = 0.0
    dis_sl.value = 0.2
    filt_sl.value = 0.2
    checkbox.active = [0, 1]

    shchas = np.random.normal(mean_sl.value, dis_sl.value, len(t))

    update1(None, None, None)

amp_sl.on_change('value', update1)
freq_sl.on_change('value', update1)
phase_sl.on_change('value', update1)
filt_sl.on_change('value', update1)
mean_sl.on_change('value', update2)
dis_sl.on_change('value', update2)
checkbox.on_change('active', check)
reset_button.on_click(reset)

col1 = column(amp_sl, freq_sl, phase_sl, margin=(10, 20, 10, 50))
col2 = column(mean_sl, dis_sl, filt_sl, margin=(10, 20, 10, 50))
block = row(col1, col2, margin=(10, 0))

control = row(
    checkbox, 
    reset_button,
    margin=(5, 10, 10, 50)
)

layout = column(
    p,
    block,
    control,
    sizing_mode="stretch_both"
)

curdoc().add_root(layout)