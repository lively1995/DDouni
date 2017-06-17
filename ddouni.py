import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
from scipy.fftpack import fft, fftfreq
import numpy as np
import json

Type = ['hungry', 'discomfort', 'sleepy', 'bored', 'stress']

rate, data = wav.read('baby1.wav')
rdata = data.T[0]
n = len(data)
Y = fft(data)

nUniquePts = int(np.ceil((n + 1) / 2.0))
p = Y[0:nUniquePts]
p = abs(p)

p=p/float(n)
p=p**2

if n%2>0:
	p[1:len(p)] = p[1:len(p)]*2
else :
	p[1:len(p)-1]=p[1:len(p)-1]*2

freqArray = np.arange(0, nUniquePts, 1.0) * (rate/n)

maxvalue = p.max()
num=0


for pvalue in p:
	try:
		if pvalue==maxvalue:
			print(freqArray[num])
			if freqArray[num] >= 100:
				customer = { 'iscrying' : 1, 'type' : Type[0]}
				jsonString = json.dumps(customer)

	except ValueError:
		if pvalue[0]==maxvalue:
			print(freqArray[num])
	num+=1

dejson = json.loads(jsonString)
print(dejson['iscrying'])
print(dejson['type'])

plt.plot(freqArray, p)
plt.show()