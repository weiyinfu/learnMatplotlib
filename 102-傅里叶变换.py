import wave
import matplotlib.pyplot as plt
import numpy as np

# 打开WAV文档
f = wave.open("0.wav", "rb")

# 读取格式信息
# (nchannels, sampwidth, framerate, nframes, comptype, compname)
params = f.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]
print(params)
# 读取波形数据
str_data = f.readframes(nframes)
f.close()

# 将波形数据转换为数组
wave_data = np.fromstring(str_data, dtype=np.short)
print(len(wave_data))
time = np.arange(0, nframes) * (1.0 / framerate)

# 绘制波形
plt.subplot(311)#开始画三行一列的第一幅图
plt.plot(time, wave_data)
plt.title("Time-Waves")
plt.xlabel("time")
plt.ylabel("amptitude")
frequency = np.fft.fft(wave_data)
#使用subplot的方式可以一直只使用plt对象进行操作
plt.subplot(312)
plt.plot(time, np.abs(frequency), c="g")
plt.title("Frequency-Amptitude")
plt.xlabel("frequency")
plt.ylabel("amptitude")
plt.subplot(313)
y=np.fft.ifft(frequency)
plt.plot(time, y.real, c="r")
plt.xlabel("time (seconds)")
plt.show()
