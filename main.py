import sim
import time
import math

clientID = sim.simxStart('127.0.0.1', 19997, True, True, 5000, 5)  # Connect to CoppeliaSim

try:
    if clientID != -1:
        print('Connected to remote API server')
        sim.simxStartSimulation(clientID, sim.simx_opmode_oneshot_wait)

        res, rw_joint_1 = sim.simxGetObjectHandle(clientID, 'rw_joint1', sim.simx_opmode_oneshot_wait)
        res, lw_joint = sim.simxGetObjectHandle(clientID, 'rw_joint1#0', sim.simx_opmode_oneshot_wait)
        res, rb_joint = sim.simxGetObjectHandle(clientID, 'rw_joint1#1', sim.simx_opmode_oneshot_wait)
        res, lb_joint = sim.simxGetObjectHandle(clientID, 'rw_joint1#2', sim.simx_opmode_oneshot_wait)

        res, rw_joint_2 = sim.simxGetObjectHandle(clientID, 'rw_joint2', sim.simx_opmode_oneshot_wait)

        res, rw_joint_3 = sim.simxGetObjectHandle(clientID, 'rw_joint3#2', sim.simx_opmode_oneshot_wait)

        for i in range(0, 200):
            first_cat = i
            second_cat = 130
            c = (second_cat ** 2 + first_cat ** 2) ** (0.5)
            angle = math.asin(second_cat / c)
            sim.simxSetJointTargetPosition(clientID, rw_joint_3, angle, sim.simx_opmode_oneshot)
            time.sleep(0.5)

        # for i in range(-6, 120):
        #     sim.simxSetJointTargetPosition(clientID, rw_joint_1, (i * math.pi / 180), sim.simx_opmode_oneshot)
        #     print(i)
        #     time.sleep(0.5)

        sim.simxStopSimulation(clientID, sim.simx_opmode_oneshot_wait)
    else:
        print('Error')
except KeyboardInterrupt:
    sim.simxStopSimulation(clientID, sim.simx_opmode_oneshot_wait)
