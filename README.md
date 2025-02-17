# VASP INCAR Explainer

A Python script to explain the function of VASP tags in an INCAR file.

## Features

Parses an INCAR file and extracts VASP tags.

Provides descriptions for each tag.

Helps users understand INCAR parameters quickly.


## Usage
```python
python vasp_incar_explainer.py <INCAR file>
```

This script reads an INCAR file, identifies the VASP tags used, and provides a brief explanation of each tag.


## Example

Given an INCAR file:
```
ISMEAR  = 0
SIGMA   = 0.01
GGA     = PE
ENCUT   = 520
ALGO    = Exact
NBANDS  = 48
EDIFF   = 1.E-6
NELM    = 256
LOPTICS = .TRUE.
NEDOS   = 2000
```
### Running the script:
```python
python vasp_incar_explainer.py INCAR
```

### Output:
```
# Optical properties & DFTP
LOPTICS    = .TRUE. # optical properties

# Electronic Relaxation (SCF)
ENCUT      = 520    # Kinetic Energy Cut-off in eV
ALGO       = Exact  # Normal (Davidson), Fast, Very_Fast (RMM-DIIS)
EDIFF      = 1.E-6  # Stopping criteria for ESC
NELM       = 256    # Max Number of Elec Self Cons Steps

# DOS settings
ISMEAR     = 0      # -5-DOS, 2-file, 1-Fermi, 0-Gaussian
SIGMA      = 0.01   # Insulators/semiconductors [0.1]  metals [0.05]
NBANDS     = 48     # No. of bands included in the calculation
NEDOS      = 2000   # Number of grid points in DOS

# Miscellaneous
GGA        = PE     # XC-type: e.g. PE AM or 91
```