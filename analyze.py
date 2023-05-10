import numpy
import matplotlib.pyplot as plt


backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
plt.plot(backLegSensorValues, 
         label="BackLeg Sensor Values",
         linewidth=3)


frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")
plt.plot(frontLegSensorValues, label="FrontLeg Sensor Values")
plt.legend()
plt.show()

