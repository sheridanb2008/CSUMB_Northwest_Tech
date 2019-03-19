# Samuel Pearce and Brian Sheridan
# CST 205
# Lab 8 


def get_file():
  file = pickAFile()
  sound = makeSound(file)
  choice = raw_input("What would you like to do? Increase Volume(I), Decrease Volume(D), Change Volume(C), MaxSample(MS), MaxVolume(MV), or GoToEleven(E)")
  print sound
  if choice == 'I':
    val1 = getSampleValueAt(sound, 10730)
    val2 = getSampleValueAt(sound, 20350)
    newSound = increaseVolume(sound)
    val3 = getSampleValueAt(newSound, 10730)
    val4 = getSampleValueAt(newSound, 20350)
    print val1, val3, val2, val4
    explore (newSound)
  if choice == 'D':
    newSound = decreaseVolume(sound)
    explore (newSound)
  if choice == 'C':
    change = changeVolume(sound)
    explore (change)
  if choice == 'MS':
    new = maxSample(sound)
    print new
  if choice == 'MV':
    newSound = maxVolume(sound)
    explore (newSound)
  if choice == 'E':
    newSound = goToEleven(sound)
    explore (newSound)
  
def increaseVolume(sound):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value*2)
  return sound

def decreaseVolume(sound):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value/2)
  return sound

def changeVolume(sound):
  choice = raw_input("Would you like to increase or decrease the volume? (I or D)")
  if choice == 'I':
    amt = raw_input("What amount would you like to increase the volume by?")
    num = int(amt)
    for sample in getSamples(sound):
      value = getSampleValue(sample)
      setSampleValue(sample, value*num)
  elif choice == 'D':
    amt = raw_input("What amount would you like to decrease the volumet by?")
    num = int(amt)
    for sample in getSamples(sound):
      value = getSampleValue(sample)
      setSampleValue(sample, value/num)
  return sound
  
def maxSample(sound):
  maxNum = 0
  for sample in range(1, getLength(sound)):
    val = getSampleValueAt(sound, sample)
    if val > maxNum:
      maxNum = val
  return maxNum

def maxVolume(sound):
  maxPossibleSampleValue = 32767
  largest = maxSample(sound)
  factor = float(maxPossibleSampleValue)/largest
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value*factor)
  return (sound)

def goToEleven(sound):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    if value > 0:
      setSampleValue(sample, 32767)
    elif value < 0:
      setSampleValue(sample, -32768)
  return sound

#Results
#Get sample value at location 10,000: 50
#What does this function do the the sound wav? This process increases the sample
#values by double which increases the size of the wav.
#How do you know it is working? A simple test would be to explore the sound file
#before and after you increase the volume. You can see the change on the pop-up screen
#Sample values at 10730 and 20350 before and after: 10730 Before: 1 10730 After: 2
#20350 Before: 0 20350 After: 0
