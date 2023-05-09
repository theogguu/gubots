import pybullet as p
import pybullet_data
import time 

physicsClient = p.connect(p.GUI)

# find path to pybullet_data (for plane)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Disables sidebars on the simulation
p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

# set gravity
p.setGravity(0,0,-9.8)

# import plane
planeId = p.loadURDF("plane.urdf")

# loads sdf
p.loadSDF("box.sdf")

for n in range(1500):
    p.stepSimulation()
    time.sleep(1/60)

p.disconnect()