This repository contains input files necessary to reproduce the data generated and analyzed in the article *Exceptional thermoelectric properties in Na₂TlSb enabled by quasi-1D band structure*. Included are stripped versions of *vaspout.h5* files from VASP and python scripts for running AMSET.

### Description  
 - vaspout_01.h5: 1st relaxation of crystal structure
 - vaspout_02.h5: 2nd relaxation of crystal structure
 - vaspout_03.h5: HSE06 calculation with dense band structure and wavefunction for transport
 - vaspout_04.h5: 1st HSE06 calculation used for deformation potentials
 - vaspout_05.h5: 2nd HSE06 calculation used for deformation potentials
 - vaspout_06.h5: 3rd HSE06 calculation used for deformation potentials
 - vaspout_07.h5: 4th HSE06 calculation used for deformation potentials
 - vaspout_08.h5: Finite differences calculation for elastic constants
 - vaspout_09.h5: DFPT calculation for phonon frequencies
 - vaspout_10.h5: HSE06 calculation for projected DOS
 - vaspout_11.h5: HSE06 calculation for projected bands
 - run_amset_01.py: Standard AMSET run
 - run_amset_02.py: Unity wavefunction overlap AMSET run
 - run_amset_03.py: CRTA AMSET run
 - run_amset_04.py: No free-carrier screening AMSET run

### Author
The above files are curated and maintained by Øven A. Grimenes

### Cite
TBA
