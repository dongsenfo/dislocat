# This script performs a blanket search for all systems with elasticity data. 

from pymatgen import MPRester
import numpy as np
import os
key = os.environ['MAPI_KEY']

# Assuming you've done `export MAPI_KEY="USER_API_KEY"` at the command line
# See materialsproject.org/dashboard to get your API key
m = MPRester(key)
data = m.query(criteria={"elasticity": {"$exists": True}},
                         properties=["pretty_formula", "elasticity.elastic_tensor"])



