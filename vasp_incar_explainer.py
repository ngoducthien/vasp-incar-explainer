import sys

# Check for correct usage
if len(sys.argv) != 2:
    print("Usage: python3 script.py <INCAR file>")
    sys.exit(1)

file_path = sys.argv[1]

# Categories of VASP tags
vasp_categories = {
    1: "General settings",
    2: "Hybrid-DFT calculations",
    3: "Optical properties & DFTP",
    4: "Parallelization",
    5: "Ionic Relaxation",
    6: "Electronic Relaxation (SCF)",
    7: "Write flags",
    8: "DOS settings",
    9: "DFT+U parameters",
    10: "Miscellaneous"
}

# Mapping VASP tags to categories and descriptions
vasp_tags = {
    # ['TAG': CATEGORY]
    # General settings
    # general_settings = [
    'SYSTEM':     (1, 'Name of System'),
    'PREC':       (1, 'Options: Normal, Medium, High, Low, Accurate'),
    'ISTART':     (1, 'Startjob: 0-new 1-cont 2-samecut'),
    'ISPIN':      (1, 'Spin polarized calculation (2-yes 1-no)'),
    'ICHARG':     (1, 'Initial charge density: 1-file 2-atom 10-cons 11-DOS'),
    'INIWAV':     (1, 'Initial electr wf. : 0-lowe 1-rand'),
    'MAGMOM':     (1, 'Initial mag moment / atom'),
    #]

    # Hybrid-DFT Calculations
    # hybrid_calculation = [
    'LHFCALC':    (2, 'Hartree Fock is set to'),
    'HFSCREEN':   (2, 'screening length'),
    'AEXX':       (2, '% HF exchange contribution - PBE0'),
    'AGGAX':      (2, 'GGA exchange part'),
    'AGGAC':      (2, 'GGA correlation'),
    'ALDAC':      (2, 'LDA correlation'),
    'PRECFOCK':   (2, 'Normal, Fast or Accurate (Low or Medium for compatibility)'),
    'ENCUTFOCK':  (2, 'apply spherical cutoff to Coloumb kernel'),
    'LMAXFOCK':   (2, 'truncation for augmentation on plane wave grid'),
    'HFLMAXF':    (2, ''),
    'LMAXFOCKAE': (2, 'truncation for all-electron charge restoration on plane wave grid'),
    'LTHOMAS':    (2, 'Thomas Fermi screening in HF'),
    'NKRED':      (2, 'specifies an uniform reduction factor for the q-point grid representation in GW calculations'),
    'NKREDX':     (2, 'Reduction factor for the q-point grid along reciprocal direction b1.'),
    'NKREDY':     (2, 'Reduction factor for the q-point grid along reciprocal direction b2.'),
    'NKREDZ':     (2, 'Reduction factor for the q-point grid along reciprocal direction b3.'),
    'EVENONLY':   (2, 'use only even q-grid points'),
    'ODDONLY':    (2, 'use only odd q-grid points'),
    'TIME':       (2, 'Special control tag'),
    #]
      
    # Optical properties & DFTP
    # optical_properties = [
    'LOPTICS':    (3, 'optical properties'),
    'CSHIFT':     (3, 'complex shift for real part using Kramers Kronig'),
    'LNABLA':     (3, 'use nabla operator in PAW spheres'),
    'LEPSILON':   (3, 'determine dielectric tensor'),
    'LRPA':       (3, 'only Hartree local field effects (RPA)'),
    #]

    # Parallelization
    # parallelization = [
    'NPAR':       (4, 'Parallelization over bands'),
    'KPAR':       (4, 'Parallelization over k-points'),
    'NCORE':      (4, 'Number of cores per group for hybrid parallelization'),
    'LPLANE':     (4, 'Use plane-wise data distribution (True/False, improves scaling for large systems)'),
    #]

    # Ionic Relaxation
    # ionic_relaxation = [
    'NSW':        (5, 'Max Number of ISC steps: 0- Single Point'),
    'IBRION':     (5, 'Ionic Relax.: 0-MD 1-qNewton-RaphsonElectronic 2-CG'),
    'ISIF':       (5, 'Stress and Relaxation: 2-Ion 3-cell+ion'),
    'EDIFFG':     (5, 'Stopping criteria for ionic self cons steps'),
    'POTIM':      (5, 'Time-step for ion-motion (fs)'),
    #]

    # Electronic Relaxation (SCF)
    # electronic_relaxation = [
    'ENCUT':      (6, 'Kinetic Energy Cut-off in eV'),
    'NELM':       (6, 'Max Number of Elec Self Cons Steps'),
    'NELMDL':     (6, 'Number of non-SC at the beginning'),
    'NELMIN':     (6, 'Min Number of ESC steps'),
    'LREAL':      (6, 'Real space projection'),
    'EDIFF':      (6, 'Stopping criteria for ESC'),
    'ALGO':       (6, 'Normal (Davidson), Fast, Very_Fast (RMM-DIIS)'),
    'IALGO':      (6, 'Electronic algorithm minimization'),
    'IMIX':       (6, 'Mixing scheme for charge density'),
    'INIMIX':     (6, 'Initial mixing scheme'),
    'MAXMIX':     (6, 'Maximum number of steps stored for Broyden mixing'),
    'AMIX':       (6, 'Linear mixing parameter for charge density'),
    'BMIX':       (6, 'Inverse Kerker length for charge mixing'),
    'AMIX_MAG':   (6, 'Linear mixing parameter for magnetization density'),
    'BMIX_MAG':   (6, 'Inverse Kerker length for magnetization density mixing'),
    'AMIN':       (6, 'Minimal mixing parameter to stabilize mixing'),
    'MIXPRE':     (6, 'Preconditioner for charge density mixing'),
    'WC':         (6, 'Weight factor for Kerker mixing'),
    #]

    # Write flags
    # write_flags = [
    'LCHARG':     (7, 'Create CHGCAR'),
    'LAECHG':     (7, 'Create AECCAR0 (core) & AECCAR2 (valence)'),
    'LWAVE':      (7, 'Create WAVECAR'),
    'LVTOT':      (7, 'Create LOCPOT, total local potential'),
    'LELF':       (7, 'Create ELFCAR'),
    'LHVAR':      (7, 'Create LOCPOT, Hartree potential only'),
    'LORBIT':     (7, 'Split the bands, create PROOUT'),
    'LORBMOM':    (7, 'specifies whether the orbital moments are written out'),
    #]
    # DOS settings
    # dos_seting = [
    'NBANDS':     (8, 'No. of bands included in the calculation'),
    'ISMEAR':     (8, '-5-DOS, 2-file, 1-Fermi, 0-Gaussian'),
    'SIGMA':      (8, 'Insulators/semiconductors [0.1]  metals [0.05]'),
    'NEDOS':      (8, 'Number of grid points in DOS'),
    'EMAX':       (8, 'Energy-range for DOSCAR file'),
    'EMIN':       (8, 'Energy-range for DOSCAR file'),
    #]
    # LDA + U parameters
    # lda_settings = [
    'LDAU':       (9, 'Enable LDA+U correction (True/False)'),
    'LDAUTYPE':   (9, 'Type of LDA+U correction (1: rotationally invariant, 2: simplified)'),
    'LDAUL':      (9, 'Orbital quantum number for each species (0: s, 1: p, 2: d, 3: f)'),
    'LDAUU':      (9, 'On-site Coulomb U parameter (eV) for each species'),
    'LDAUJ':      (9, 'Exchange interaction parameter J (eV) for each species'),
    'LDAUPRINT':  (9, 'Controls output of LDA+U-related information (0-3, higher values give more details)'),
    'LMAXMIX':    (9, 'Maximum angular momentum for charge density mixing (default depends on POTCAR)'),
    #]
    # Uncategorized/OQMD codes
    # uncategorized = [
    'PSTRESS':    (10, 'pullay stress'),
    'EPSILON':    (10, 'bulk dielectric constant'),
    'LDIPOL':     (10, 'correct potential (dipole corrections)'),
    'IDIPOL':     (10, '1-x, 2-y, 3-z, 4-all directions'),
    'MAGNETISM':  (10, ''),
    'ADDGRID':    (10, 'Improve the grid accuracy'),
    'NGXF':       (10, 'FFT mesh for charges'),
    'NGYF':       (10, 'FFT mesh for charges'),
    'NGZF':       (10, 'FFT mesh for charges'),
    'NBLK':       (10, 'Blocking for some BLAS calls'),
    'NWRITE':     (10, 'Verbosity write-flag (how much is written)'),
    'NBLOCK':     (10, 'Inner block'),
    'KBLOCK':     (10, 'Outer block'),
    'IWAVPR':     (10, 'Prediction of wf.: 0-non 1-charg 2-wave 3-comb'),
    'ISYM':       (10, 'Symmetry: 0-nonsym 1-usesym'),
    'SYMPREC':    (10, 'Precession in symmetry routines'),
    'LCORR':      (10, 'Harris-correction to forces'),
    'TEBEG':      (10, 'Temperature during run'),
    'TEEND':      (10, 'Temperature during run'),
    'SMASS':      (10, 'Nose mass-parameter (am)'),
    'NPACO':      (10, 'Distance for P.C.'),
    'APACO':      (10, 'Nr. of slots for P.C.'),
    'POMASS':     (10, 'Mass of ions in am'),
    'ZVAL':       (10, 'Ionic valence'),
    'RWIGS':      (10, 'Wigner-Seitz radii'),
    'NELECT':     (10, 'Total number of electrons'),
    'NUPDOWN':    (10, 'Fix spin moment to specified value'),
    'ROPT':       (10, 'Number of grid points for non-local proj in real space'),
    'GGA':        (10, 'XC-type: e.g. PE AM or 91'),
    'VOSKOWN':    (10, 'Use Vosko, Wilk, Nusair interpolation'),
    'DIPOL':      (10, 'Center of cell for dipol'),
    'WEIMIN':     (10, 'Special control tags'),
    'EBREAK':     (10, 'Special control tags'),
    'DEPER':      (10, 'Special control tags'),
    'LSCALAPACK': (10, 'Switch off scaLAPACK'),
    'LSCALU':     (10, 'Switch of LU decomposition'),
    'LASYNC':     (10, 'Overlap communcation with calculations'),
    'NGX':        (10, 'FFT mesh for orbitals'),
    'NGY':        (10, 'FFT mesh for orbitals'),
    'NGZ':        (10, 'FFT mesh for orbitals')
}

try:
    with open(file_path, "r") as file:
        lines = file.readlines()
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
    sys.exit(1)

uncategory_id = 10
parsed_tags = []
max_tag_len = max(len(tag) for tag in vasp_tags)
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

# Organize by categories and print
for category, category_name in sorted(vasp_categories.items()):
    matching_tags = [tag for tag in parsed_tags if tag[0] == category]
    if matching_tags:
        print(f"\n# {category_name}")
        for _, tag_name, tag_value, description in matching_tags:
            spacing1 = " " * (max_tag_len - len(tag_name) + 1)
            spacing2 = " " * (max_value_len - len(tag_value) + 1)
            print(f"{tag_name}{spacing1}= {tag_value}{spacing2}# {description}")

