import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time 
import numpy

physicsClient = p.connect(p.GUI)

# find path to pybullet_data (for plane)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Disables sidebars on the simulation
p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

# set gravity
p.setGravity(0,0,-9.8)

# load URDFs: plane and robot
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

# load SDFs: world
p.loadSDF("world.sdf")

# prepare robot for simulation
pyrosim.Prepare_To_Simulate(robotId)

# numpy vector of zeros to store sensor values
backLegSensorValues = numpy.zeros(300)
frontLegSensorValues = numpy.zeros(300)

for n in range(300):
    p.stepSimulation()
    backLegSensorValues[n] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[n] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    time.sleep(1/60)


# print(backLegSensorValues)
numpy.save("data/backLegSensorValues.npy", backLegSensorValues)
numpy.save("data/frontLegSensorValues.npy", frontLegSensorValues)
p.disconnect()