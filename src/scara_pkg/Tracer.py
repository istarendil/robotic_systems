import numpy as np


class Tracer():

    def __init__(self):
        pass

    def jTraj3(self, tf, dt, q0, qf, v0, vf):
        
        # Time vector
        t = np.arange(0, tf+dt, dt)

        # Polynomia coefficients
        C0 = q0
        C1 = v0
        C2 = (3*(qf - q0)/tf**2) - ((vf + 2*v0)/tf)
        C3 = -(2*(qf -q0)/tf**3) + ((vf + v0)/tf**2)

        # Resulting trajectories
        q = np.dot(np.array([t**0, t, t**2, t**3]).transpose(), np.array([C0, C1, C2, C3]))
        v = np.dot(np.array([t**0, t, t**2]).transpose(), np.array([C1, 2*C2, 3*C3]))
        a = np.dot(np.array([t**0, t]).transpose(), np.array([2*C2, 6*C3]))

        return a, v, q

    def cTrajLine(self, tf, dt, q0, qf):
        
        # Auxiliar vector coefficients
        v = qf - q0
        
        # Coordinates
        a = np.linspace(q0[3], qf[3], dt)
        x = np.linspace(q0[0], qf[0], dt)
        t = (x - q0[0])/ v[0]
        
        y = q0[1] + v[1]*t
        z = q0[2] + v[2]*t
                        
        return x, y, z, a

if __name__=='__main__':
    my_tracer = Tracer()

    q0 = np.array([0, 15])
    qf = np.array([33, 75])
    v0 = np.array([0, 0])
    vf = np.array([3, 0])
    tf = 3
    dt = 0.2

    a, v, q = my_tracer.jTraj3(tf, dt, q0, qf, v0, vf)
    print('Position path:')
    print(q)

    print('Velocity: ')
    print(v)

