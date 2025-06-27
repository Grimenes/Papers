#!/usr/bin/env python3

from amset.core.run import Runner
import numpy as np
import h5py

# Load material constants from h5
h5 = h5py.File('const.h5')
el_const = np.array(h5['elastic_tensor'][:])
static_diel = np.array(h5['static_dielectric_tensor'][:])
hf_diel = np.array(h5['high_frequenzy_dielectric_tensor'][:])
pop_freq = np.array(h5['polar_optical_frequency'][()])

# Scattering types
types = ['ADP','POP','IMP']

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
            'write_mesh':True,
            'fd_tol':0.005,
            'nworkers':10,
            'free_carrier_screening':True,
            'energy_cutoff':0.5,
            'deformation_potential':'deformation.h5',
            'wavefunction_coefficients':'wavefunction.h5',
            'unity_overlap':True,
            'high_frequency_dielectric':hf_diel,
            'pop_frequency':pop_freq,
            'static_dielectric':static_diel,
            'elastic_constant':el_const}


if __name__ == '__main__':
    runner = Runner.from_vasprun('vasprun.xml',settings)
    amset_data = runner.run()
