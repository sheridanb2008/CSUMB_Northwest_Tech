# CST205
# Module 2: Lab 8
# Craig Calvert and Kevin Bentley
# 

# Reduces a sound object's volume by half
def decreaseVolume(sound):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value / 2)
  return(sound)

# Increases/decreases sound object's volume depending on factor level
def changeVolume(sound, factor):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value * factor)
  return(sound)

# Finds a sound object's maximum sample value
def maxSample(sound):
  maxValue = 0
  for sample in range(0, getLength(sound)):
    x = getSampleValueAt(sound, sample)
    y = max(x, maxValue)
    maxValue = y
  return(maxValue)

# Increases the volume based on value returned by your maxSample
def maxVolume(sound):
  sample = maxSample(sound)
  # Determine maximum sample value (8-bit or 16-bit)
  if sample <= 127:
    maxPossibleSampleValue = 127
  else:
    maxPossibleSampleValue = 32767
  factor = float(maxPossibleSampleValue) / float(sample)
  newSound = changeVolume(sound, factor)
  return newSound
  
# Take a sound object and maximizes or minimizes each sample
def goToEleven(sound):
  level = maxSample(sound)
  # Determine if level should be set for 8-bit or 16-bit audio file
  if level <= 127:
    level = 127
  else:
    level = 32767
  for sample in range(0, getLength(sound)):
    x = getSampleValueAt(sound, sample)
    if x > 0:
      setSampleValueAt(sound, sample, level)
    elif x < 0:
      negLevel = -level
      setSampleValueAt(sound, sample, negLevel)
    else:
      pass
  return(sound)

# Method Tests

def decreaseVolumeTest():
  sound = pickAFile()
  wav = makeSound(sound)
  decreaseVolume(wav)
  play(wav)

def changeVolumeTest():
  sound = pickAFile()
  wav = makeSound(sound)
  level = float(raw_input('Volume level: '))
  changeVolume(wav, level)
  play(wav)
  
def maxSampleTest():
  sound = pickAFile()
  wav = makeSound(sound)
  result = maxSample(wav)
  print(result)
  
def maxVolumeTest():
  sound = pickAFile()
  wav = makeSound(sound)
  maxVolume(wav)
  play(wav)

def goToElevenTest():
  sound = pickAFile()
  wav = makeSound(sound)
  goToEleven(wav)
  play(wav)

