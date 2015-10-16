import numpy as np
import os
key = os.environ['MAPI_KEY']

import pymatgen as mg
from pymatgen import MPRester
from pymatgen.analysis.defects import point_defects
from pymatgen.io import vasp
from pymatgen.io.vasp.sets import MPStaticVaspInputSet
from pymatgen.io.zeoone import get_voronoi_nodes, get_void_volume_surfarea, get_high_accuracy_voronoi_nodes
try:
    from zeo.netstorage import AtomNetwork, VoronoiNetwork
    from zeo.area_volume import volume, surface_area
    from zeo.cluster import get_nearest_largest_diameter_highaccuracy_vornode,\
            generate_simplified_highaccuracy_voronoi_network, \
            prune_voronoi_network_close_node
    zeo_found = True
except ImportError:
    zeo_found = False		 

m = MPRester(key)

#def get_POSCAR(elements, interstitial, supercell_size, ):

results = m.query("Fe", ['structure'])
print(type(results[2]['structure']))
#Mg_cell = mg.Lattice.hexagonal(3.184, 5.249)

#print(Mg_cell.lengths_and_angles)

#Mg_Lattice = mg.Structure(Mg_cell, ["Mg","Mg"], [[.333333333,.66666666666,.25], [.66666666666,.33333333333333,.75]])
print(results[2]['structure'])
Mg_Lattice=results[2]['structure']
#Mg_Lattice = results[0]

Mg_Interstitial = point_defects.Interstitial(Mg_Lattice, {u"Fe":0}, {u"Fe":1.26}, 'voronoi_vertex',accuracy=u'Normal',symmetry_flag=True,oxi_state=False)

print(Mg_Interstitial.enumerate_defectsites())
print(Mg_Interstitial.defectsite_count())


print("START")

Mg_Interstitial.make_supercells_with_defects([3,3,3], "Fe")
#InterstitialElement= ["H", "He", "Li","Be","B","C","N","O","F","Ne"]
InterstitialElement= ["O"] 
Size = [2,3,4]
newpath = r'/home/handong/Documents/pymatgen/build/bdist.linux-x86_64/Fe' 
if not os.path.exists(newpath): os.makedirs(newpath)
for j in range(len(InterstitialElement)):
	newpathinterstitial = r'/home/handong/Documents/pymatgen/build/bdist.linux-x86_64/Fe/{}'.format(InterstitialElement[j]) 
	if not os.path.exists(newpathinterstitial): os.makedirs(newpathinterstitial)
	for i in range(len(Size)):
		newpathsize = r'/home/handong/Documents/pymatgen/build/bdist.linux-x86_64/Fe/{}/{}x{}'.format(InterstitialElement[j], Size[i], Size[i]) 
		if not os.path.exists(newpathsize): os.makedirs(newpathsize)
		for k in range(len(Mg_Interstitial.make_supercells_with_defects([Size[i],Size[i],Size[i]], InterstitialElement[j]))):
			newpathsite = r'/home/handong/Documents/pymatgen/build/bdist.linux-x86_64/Fe/{}/{}x{}/{}'.format(InterstitialElement[j], Size[i], Size[i], k) 
			if not os.path.exists(newpathsite): os.makedirs(newpathsite)
				#Mg_Interstitial.make_supercells_with_defects([Size[i],Size[i],Size[i]], InterstitialElement[j])[k].to(fmt = 'poscar', filename = 'TiI{}D{}POSCAR'.format(k, Size[i]))
				#shutil.move('/home/handong/Documents/pymatgen/build/bdist.linux-x86_64/MgI{}D{}POSCAR'.format(k, Size[i]), "/home/handong/Documents/pymatgen/build/bdist.linux-x86_64/Mg/{}x{}/{}/MgI{}D{}POSCAR".format(InterstitialElement[j], size[i], size[i],k, k, Size[i]))
				#Potcarfile = Potcar([InterstitialElement[j], 'Mg'], u'PBE', None )
				#Potcarfile.write_file('MgI{}D{}POTCAR'.format(k, Size[i]))
				#shutil.move('/home/handong/Documents/pymatgen/build/bdist.linux-x86_64/MgI{}D{}POSCAR'.format(k, Size[i]), "/home/handong/Documents/pymatgen/build/bdist.linux-x86_64/Mg/{}x{}/{}MgI{}D{}POTCAR".format(InterstitialElement[j], size[i], size[i], k, k, Size[i]))
			VASP_Input = MPStaticVaspInputSet(90,0.1)
			#dictionary = VASP_Input.get_all_vasp_input(Mg_Interstitial.make_supercells_with_defects([Size[i],Size[i],Size[i]], InterstitialElement[j]))
			VASP_Input.write_input(Mg_Interstitial.make_supercells_with_defects([Size[i],Size[i],Size[i]], InterstitialElement[j])[k],r'/home/handong/Documents/pymatgen/build/bdist.linux-x86_64/Fe/{}/{}x{}/{}'.format(InterstitialElement[j], Size[i], Size[i], k, True, True))

