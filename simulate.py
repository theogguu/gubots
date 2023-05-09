import pybullet as p
physicsClient = p.connect(p.GUI)
for n in range(1500):
    p.stepSimulation()
    time.sleep(1/60)

p.disconnect()
