
# Assuming you've done `export MAPI_KEY="USER_API_KEY"` at the command line
# See materialsproject.org/dashboard to get your API key

from pymatgen import MPRester
import numpy as np
import os
key = os.environ['MAPI_KEY']
m = MPRester(key)


e_cutoff = m.query("mp-46", 
	["elasticity.calculations.energy_cutoff"])[0]['elasticity.calculations.energy_cutoff'] # units (eV)

file = open("INCAR", "w")
file.write("LWAVE = .FALSE.\n")
file.write("LCHARG= .FALSE.\n")
file.write("PREC    = Accurate\n")
file.write("LREAL   = AUTO\n")
file.write("ADDGRID = .TRUE.\n")
file.write("POTIM   = 0.1\n")
file.write("SIGMA   = 0.05\n")
file.write("IBRION  = 2\n")
file.write("NSW     = 100\n")
file.write("ENCUT   ={0:3d}\n".format(int(e_cutoff)))
file.write("EDIFF   = 1e-8\n")
file.write("EDIFFG  = -1e-3\n")
file.write("ISIF    = 3\n")
file.close()



