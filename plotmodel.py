from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt

with fits.open('rrtemplate-qso6vec.fits') as h:
    
    wave = 10**(h[0].header['CRVAL1'] + np.arange(h[0].header['NAXIS1'])*h[0].header['CDELT1']) #wavelength array for model
    vectors = h['BASIS_VECTORS'].data #eigenspectra
    #redshifts = h['REDSHIFTS'].data #redshift coverage of model for running redrock

for i in range(6):
    
    plt.plot(wave, vectors[i]/np.median(vectors[i]), label=f'vector #{i}')
    
plt.xlabel(r'rest-frame wavelength [$\AA$]')
plt.ylabel('flux desnity')
plt.legend()
plt.show()
