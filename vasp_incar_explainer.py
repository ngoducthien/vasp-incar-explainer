import sys

# Check for correct usage
if len(sys.argv) != 2:
    print("Usage: python3 script.py <INCAR file>")
    sys.exit(1)

file_path = sys.argv[1]

# Categories of VASP tags
vasp_categories = {
    1: "General Settings",
    2: "Hybrid-DFT Calculations",
    3: "Optical Properties & Time-Dependent DFT",
    4: "Parallelization Settings",
    5: "Ionic Relaxation & Molecular Dynamics",
    6: "Electronic Relaxation (SCF Settings)",
    7: "File Output Flags",
    8: "DOS & Band Structure Settings",
    9: "LDA+U Settings",
    10: "Miscellaneous"
}

# Mapping VASP tags to categories and descriptions
vasp_tags = {
    # General Settings
    'ICHARG':     (1, 'Initial charge density: 1-file, 2-atom, 10-constant, 11-DOS'),
    'INIWAV':     (1, 'Initial wavefunction: 0-from file, 1-random'),
    'ISPIN':      (1, 'Spin polarization: 1-no, 2-yes'),
    'ISTART':     (1, 'Job start mode: 0-new, 1-continue, 2-same cutoff'),
    'MAGMOM':     (1, 'Initial magnetic moments per atom'),
    'PREC':       (1, 'Precision: Normal, Medium, High, Low, Accurate'),
    'SYSTEM':     (1, 'System name'),

    # Hybrid-DFT Calculations
    'AEXX':       (1, 'HF exchange fraction (PBE0: 0.25)'),
    'AGGAC':      (1, 'GGA correlation contribution'),
    'AGGAX':      (1, 'GGA exchange contribution'),
    'ALDAC':      (1, 'LDA correlation contribution'),
    'ENCUTFOCK':  (1, 'Energy cutoff for Coulomb kernel'),
    'EVENONLY':   (2, 'Use only even q-grid points'),
    'HFLMAXF':    (1, 'Maximum L value in Fock matrix'),
    'HFSCREEN':   (1, 'Screening length in hybrid functionals'),
    'LHFCALC':    (1, 'Enable Hartree-Fock: True/False'),
    'LMAXFOCK':   (1, 'Augmentation function cutoff'),
    'LMAXFOCKAE': (1, 'AE augmentation truncation'),
    'LTHOMAS':    (2, 'Thomas-Fermi screening in HF'),
    'NKRED':      (2, 'Reduction factor for q-point grid in GW'),
    'NKREDX':     (2, 'Reduction factor for b1 direction'),
    'NKREDY':     (2, 'Reduction factor for b2 direction'),
    'NKREDZ':     (2, 'Reduction factor for b3 direction'),
    'ODDONLY':    (2, 'Use only odd q-grid points'),
    'PRECFOCK':   (1, 'Fock matrix precision: Normal, Fast, Accurate'),
    'TIME':       (2, 'Special control tag'),

    # Optical Properties & Time-Dependent DFT
    'CSHIFT':     (3, 'Complex shift for Kramers-Kronig'),
    'LEPSILON':   (3, 'Compute dielectric tensor'),
    'LNABLA':     (3, 'Use nabla operator in PAW spheres'),
    'LOPTICS':    (3, 'Calculate optical properties'),
    'LRPA':       (3, 'Include only Hartree local-field effects'),

    # Parallelization Settings
    'KPAR':       (4, 'Parallelization over k-points'),
    'LPLANE':     (4, 'Use plane-wise distribution (improves scaling)'),
    'NCORE':      (4, 'Cores per group for hybrid parallelization'),
    'NPAR':       (4, 'Parallelization over bands'),

    # Ionic Relaxation & Molecular Dynamics
    'EDIFFG':     (5, 'Convergence criterion for ionic relaxation'),
    'IBRION':     (5, 'Ionic relaxation: 0-MD, 1-quasi-Newton, 2-CG'),
    'ISIF':       (5, 'Relaxation mode: 2-ions, 3-cell+ions'),
    'NSW':        (5, 'Max ionic steps (0 for single point)'),
    'POTIM':      (5, 'Ionic time step (fs)'),

    # Electronic Relaxation (SCF Settings)
    'ALGO':       (6, 'SCF algorithm: Normal | VeryFast | Fast | Conjugate | All | Damped | Exact'),
    'AMIN':       (6, 'Minimum mixing parameter'),
    'AMIX':       (6, 'Linear mixing parameter'),
    'AMIX_MAG':   (6, 'Linear mixing for magnetization density'),
    'BMIX':       (6, 'Inverse Kerker length for charge mixing'),
    'BMIX_MAG':   (6, 'Inverse Kerker length for magnetization mixing'),
    'EDIFF':      (6, 'SCF convergence criterion'),
    'ENCUT':      (6, 'Energy cutoff (eV)'),
    'IALGO':      (6, 'Electronic minimization algorithm'),
    'IMIX':       (6, 'Charge density mixing scheme'),
    'INIMIX':     (6, 'Initial mixing scheme'),
    'LREAL':      (6, 'Real-space projection'),
    'MAXMIX':     (6, 'Max steps stored for Broyden mixing'),
    'MIXPRE':     (6, 'Preconditioner for mixing'),
    'NELM':       (6, 'Max electronic SCF steps'),
    'NELMDL':     (6, 'Non-SCF steps at the start'),
    'NELMIN':     (6, 'Min electronic SCF steps'),
    'WC':         (6, 'Weight factor for Kerker mixing'),

    # File Output Flags
    'LAECHG':     (7, 'Write AECCAR0 (core) & AECCAR2 (valence)'),
    'LCHARG':     (7, 'Write CHGCAR'),
    'LELF':       (7, 'Write ELFCAR'),
    'LHVAR':      (7, 'Write LOCPOT (Hartree potential only)'),
    'LORBIT':     (7, 'Write PROOUT (band splitting)'),
    'LORBMOM':    (7, 'Write orbital moments'),
    'LVTOT':      (7, 'Write LOCPOT (total local potential)'),
    'LWAVE':      (7, 'Write WAVECAR'),

    # DOS & Band Structure Settings
    'EMAX':       (8, 'DOS upper energy limit'),
    'EMIN':       (8, 'DOS lower energy limit'),
    'ISMEAR':     (8, 'Smearing: -5-DOS, 2-file, 1-Fermi, 0-Gaussian'),
    'NBANDS':     (8, 'Number of bands'),
    'NEDOS':      (8, 'DOS grid points'),
    'SIGMA':      (8, 'Smearing width: Insulators [0.1], Metals [0.05]'),

    # LDA+U Settings
    'LDAU':       (9, 'Enable LDA+U'),
    'LDAUJ':      (9, 'Exchange interaction J (eV)'),
    'LDAUL':      (9, 'Orbital quantum number (0-s, 1-p, 2-d, 3-f)'),
    'LDAUPRINT':  (9, 'LDA+U output verbosity (0-3)'),
    'LDAUTYPE':   (9, 'LDA+U type: 1-rotationally invariant, 2-simplified'),
    'LDAUU':      (9, 'On-site Coulomb U (eV)'),
    'LMAXMIX':    (9, 'Max angular momentum for charge mixing'),

    # Miscellaneous
    'ADDGRID':    (10, 'Improve FFT grid accuracy'),
    'DIPOL':      (10, 'Dipole center'),
    'EPSILON':    (10, 'Bulk dielectric constant'),
    'GGA':        (10, 'XC functional (e.g., PBE, AM, 91)'),
    'IDIPOL':     (10, 'Dipole correction direction: 1-x, 2-y, 3-z, 4-all'),
    'ISYM':       (10, 'Symmetry: 0-none, 1-use'),
    'LASYNC':     (10, 'Asynchronous communication'),
    'LCORR':      (10, 'Harris correction to forces'),
    'LDIPOL':     (10, 'Enable dipole corrections'),
    'LSCALAPACK': (10, 'Enable ScaLAPACK'),
    'LSCALU':     (10, 'Enable LU decomposition'),
    'MAGNETISM':  (10, 'Magnetic settings'),
    'NELECT':     (10, 'Total number of electrons'),
    'NGXF':       (10, 'FFT mesh for charge density'),
    'NGYF':       (10, 'FFT mesh for charge density'),
    'NGZF':       (10, 'FFT mesh for charge density'),
    'NUPDOWN':    (10, 'Fixed spin moment'),
    'NWRITE':     (10, 'Output verbosity level'),
    'POMASS':     (10, 'Atomic mass (amu)'),
    'PSTRESS':    (10, 'Pulay stress'),
    'SMASS':      (10, 'Nose-Hoover mass parameter'),
    'SYMPREC':    (10, 'Symmetry precision'),
    'TEBEG':      (10, 'Initial temperature (K)'),
    'TEEND':      (10, 'Final temperature (K)'),
    'ZVAL':       (10, 'Ionic valence'),
}

try:
    with open(file_path, "r") as file:
        lines = file.readlines()
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
    sys.exit(1)

uncategory_id = 10
parsed_tags = []
max_tag_len = 0
max_value_len = 0

for line in lines:
    line = line.strip()
    if not line or line.startswith("#"):  # Skip empty lines and comments
        continue
    
    # Split line into individual tag entries if multiple tags are present
    tag_entries = line.split(";")
    for entry in tag_entries:
        if "=" in entry:
            tag_name, tag_value = map(str.strip, entry.split("=", 1))
            if tag_name in vasp_tags:
                category, description = vasp_tags[tag_name]
                max_value_len = max(max_value_len, len(tag_value))
                parsed_tags.append((category, tag_name, tag_value, description))
            else:
                # If the tag is not found in the variable vasp_tags
                parsed_tags.append((uncategory_id, tag_name, tag_value, "No description"))
            max_tag_len = max(max_tag_len, len(tag_name))

# Organize by categories and print
for category, category_name in sorted(vasp_categories.items()):
    matching_tags = [tag for tag in parsed_tags if tag[0] == category]
    if matching_tags:
        print(f"\n# {category_name}")
        for _, tag_name, tag_value, description in matching_tags:
            spacing1 = " " * (max_tag_len - len(tag_name) + 1)
            spacing2 = " " * (max_value_len - len(tag_value) + 1)
            print(f"{tag_name}{spacing1}= {tag_value}{spacing2}# {description}")

