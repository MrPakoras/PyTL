# Converting from .webp from MAL asset download to .jpg

import os

nth = 0
imgfiles = 0

rootdir = './images/'
for dirName, subdirList, fileList in os.walk(rootdir):
	for fname in fileList:
		if fname.endswith('.webp'):
			wp = rootdir+fname
			n = rootdir+fname.replace('.webp','.jpg')
			os.rename(wp,n) # Replaces file with renamed file
			print('>> Renamed'+wp+' to '+n)
			nth += 1
			imgfiles += 1 # Number of images to import
		elif fname.endswith('.jpg'):
			imgfiles += 1

		else:
			pass

print(f'>> {nth} files renamed.')
print(f'>> Number of Images:   {imgfiles}\n\n')