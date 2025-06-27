#!/usr/bin/env python3

from amset.core.run import Runner
import numpy as np

# Scattering types
types = ['CRT']

# Carrier concentration
d = np.logspace(17,22,50).tolist()[-1::-1]
d += (-np.logspace(17,22,50)).tolist()

# Temperatures
Temps = [200,250,300,350,400,450,500,550,600,650,700]

# Interpolation coefficient
n_interpol = 5

settings = {'doping':d,
            'temperatures':Temps,
            'scattering_type':types,
            'interpolation_factor':n_interpol,
            'constant_relaxation_time':1E-14,
            'nworkers':10,
            'energy_cutoff':0.5,
            'wavefunction_coefficients':'wavefunction.h5'}


if __name__ == '__main__':
    runner = Runner.from_vasprun('vasprun.xml',settings)
    amset_data = runner.run()
