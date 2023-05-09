import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("box.sdf")

for x in range(5):
    for y in range(5):
        s = 1
        h = 0.5
        for tower in range(10):
            pyrosim.Send_Cube(name="Box" + str(tower), pos=[x,y,h] , size=[s,s,s])
            s = .9*s
            h += s  
         

pyrosim.End()
