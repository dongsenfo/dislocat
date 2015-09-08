# This script searches for the elastic tensor of the specified compound.

from pymatgen import MPRester
import numpy as np
import os
key = os.environ['MAPI_KEY']

# Assuming you've done `export MAPI_KEY="USER_API_KEY"` at the command line
# See materialsproject.org/dashboard to get your API key
def get_tensor(name):
	m = MPRester(key)
	tensor = m.query(criteria={"elasticity": {"$exists": True}, "pretty_formula": name},
                         properties=["elasticity.elastic_tensor"])
	return tensor



