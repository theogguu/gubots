import pybullet as p
import time 
physicsClient = p.connect(p.GUI)

# Disables sidebars on the simulation
# p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

# loads sdf
p.loadSDF("box.sdf")

for n in range(1500):
    p.stepSimulation()
    time.sleep(1/60)

p.disconnect()