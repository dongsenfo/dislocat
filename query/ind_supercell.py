# This script searches for the elastic tensor of the specified compound.

from pymatgen import MPRester
from pymatgen.core.periodic_table import Element
from pymatgen.core.structure import Structure
from pymatgen.analysis.defects.point_defects import *
from pymatgen.io.vasp.inputs import *

import numpy as np
import os
key = os.environ['MAPI_KEY']
m = MPRester(key)
# Assuming you've done `export MAPI_KEY="USER_API_KEY"` at the command line
# See materialsproject.org/dashboard to get your API key

def make_supercell(mp_id, scaling):
	structure = m.query(mp_id, properties=["structure"])[0]['structure']
	structure.make_supercell(scaling)
	
	return structure


#def create_defect(element, structure):
	# structure: pymatgen.core.structure.Structure
  #           valences: Dictionary of oxidation states of elements in 
  #               {el:valence} form
  	#valences = {element: 0}

  #           radii: Radii of elemnts in the structure
  	#radii = Element(element).atomic_radius

  #           site_type: "voronoi_vertex" uses voronoi nodes
  #               "voronoi_edgecenter" uses voronoi polyhedra edge centers
  #               "voronoi_facecenter" uses voronoi polyhedra face centers
  #               "all" combines vertices, edgecenters and facecenters.
  #               Default is "voronoi_vertex"
  #           accuracy: Flag denoting whether to use high accuracy version 
  #               of Zeo++. Options are "Normal" and "High". Default is normal.
  #           symmetry_flag: If True, only returns symmetrically distinct sites
  #           oxi_state: If False, input structure is considered devoid of 
  #               oxidation-state decoration. And oxi-state for each site is 
  #               determined. Use True, if input structure is oxi-state 
  #               decorated. This option is useful when the structure is 
  #               not electro-neutral after deleting/adding sites. In that
  #               case oxi-decorate the structure before deleting/adding the
  #               sites.

  # return defective supercell


def write_poscar(structure):
  pos = Poscar(structure)
  pos.write_file("POSCAR")


write_poscar(make_supercell('mp-46', 3))
write_poscar(create_defect(make_supercell('mp-46', 3)))
		





