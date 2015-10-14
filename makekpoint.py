import numpy as np


def makekpoint(n0, Na, Nc, eta):
        ###############INPUTS###############
        #n0: number of k-points for primitive unit cell from elastic concstants calculations
        #Na:  repeat number in the supercell for e_1 and e_2
        #Nc:  repeat number in the supercell for e_3
        #eta: c/a parameter

        ###############OUTPUT###############
        # KPOINTS:  KPOINTS file containing the appropriate mesh for the size of the super
        # cell and the number of k-points in the primitive unit cell calculation

        # define polynomial
        a       = 0.59460917
        b       = 1.583984
        c       = -12.99017245
        d       = 31.23228887

        def nk(Nk):
                nkp     = a*Nk**3 + b*Nk**2 + c*Nk + d
                return nkp

        def kroot(nkp):
                p       = np.array([a, b, c, d - nkp])
                roots   = np.roots(p)

                for i in xrange(3):
                        if abs(np.imag(roots[i])) < 1e-10 and np.real(roots[i]) > 0.:
                                root    = np.real(roots[i])

                return int(np.round(root))

        # define primitive lattice vectors
        avec    = np.array([1, 0, 0])
        bvec    = np.array([-0.5, np.sqrt(3.)/2., 0])
        cvec    = np.array([0, 0, 1.58])

        # calculate primitive unit cell volume
        Vo      = np.dot(avec, np.cross(bvec, cvec))

        # define supercell lattice vectors
        aN      = Na*avec
        bN      = Na*bvec
        cN      = Nc*cvec

        VN      = np.dot(aN, np.cross(bN, cN))


        # find number of k-points desired in the supercell
        nN      = n0 / Na**3

        # define the k-point mesh
        Ka      = kroot(nN)
        Kc      = int(np.round(Ka/eta))
        if Ka < 3:
                Ka      = 3
                Kc      = 2

        print 'KPOINT MESH'
        print '{0:3d}   {0:3d}   {1:3d}'.format(Ka, Kc)

        # Make the KPOINTS file
        f       = open('KPOINTS','w')
        f.write('{0:<2d}x{0:<2d}x{1:<2d}\n'.format(Ka,Kc))
        f.write('0\n')
        f.write('Gamma\n')
        f.write('{0:<2d}  {0:<2d}  {1:<2d}\n'.format(Ka,Kc))
        f.write('0 0 0\n')
        f.close()

