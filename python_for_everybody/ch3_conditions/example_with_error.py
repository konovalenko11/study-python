import math

signal_power = 94534535
noise_power = 10333
ratio = signal_power / noise_power
decibels = 10 * math.log10(ratio)
print(decibels)
