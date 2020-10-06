import random, os

# z = [(0,0,0),(1,1,1)]

# a = (random.choice(z))
# print(a)
# print(type(a))


defcols = [(134, 52, 235),(52, 89, 235),(52, 235, 147),(235, 235, 52),(235, 156, 52),(235, 79, 52)] # Default colours for tiers
defranks = ['S', 'A', 'B', 'C', 'D', 'F'] # Default ranks for tiers

# tiern = [print(x) for x in defcols in defranks]
# print(tiern)

# def tiern(n):
# 	col = defcols[n-1]
# 	rank = defranks[n-1]

# 	return rank, col

# m = tiern(2)[1]

# print(m)
#print(m[0])
#print(m[1])
rootdir = './images/'
for dirName, subdirList, fileList in os.walk(rootdir):
	for fname in fileList:
		wp = rootdir+fname
		n = fname[:-5]
		jp = rootdir+n+'.jpg'

		os.replace(wp,jp)
		print('>> Renamed'+wp+' to '+jp)