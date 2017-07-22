import numpy as np 
import matplotlib as mpl 
import matplotlib.pyplot as plt
def getDistance(dis,pos):
	for i in range(pos.shape[0]):
		for j in range(i+1,pos.shape[0]):
			dis[i][j]=(pos[i][0]-pos[j][0])**2+(pos[i][1]-pos[j][1])**2
			dis[i][j]=dis[i][j]**0.5
			dis[j][i]=dis[i][j]
def getLen(dis,gro,M):
	lens=np.zeros([M,1])
	for i in range(gro.shape[0]):
		lens[i]+=dis[gro[i][-1]][gro[i][0]]
		for j in range(1,gro.shape[1]):
			lens[i]+=dis[gro[i][j]][gro[i][j-1]]
	return lens
def getFitness(lens,fitness):
	fmax=max(lens[:][0])
	fmin=min(lens[:][0])
	total=0
	for i in range(lens.shape[0]):
		fitness[i][0]=1/lens[i][0]
		total+=fitness[i][0]
	for i in range(lens.shape[0]):
		fitness[i][0]=fitness[i][0]/total
def seletion(fitness,gro):
	rate=np.random.random()
	ac=0
	for i in range(gro.shape[0]):
		ac+=fitness[i][0]
		if ac>rate:
			return gro[i][:]
def getMostFitness(fitness,gro):
	maxf=max(fitness)
	x,y=np.where(fitness==maxf)
	return gro[x[0]][:]
minlenght=0x7fffffff
def DFS(start,dis,N,length,p,path,bestPath):
	global minlenght
	flag=False
	for i in range(N):
		if p[i]==0:
			flag=True
	if flag==False:
		if length+dis[start][0]<minlenght:
			minlenght=length+dis[start][0]
			bestPath[:]=path[:]
			print(minlenght)
			print(bestPath)
			return 
	for i in range(N):
		if p[i]==0:
			p[i]=1
			path.append(i)
			DFS(i,dis,N,dis[start][i]+length,p,path[:],bestPath)
			path.remove(i)
			p[i]=0
def plotB(pos,best,title):
	print(best)
	plt.figure('data')
	if title=='violence':
		p1=plt.subplot(221)
		plt.title(title)
	else:
		p2=plt.subplot(222)
		plt.title(title)
	for i in range(pos.shape[0]):
		mpl.pyplot.plot(pos[i][0],pos[i][1],'o')
	x=np.zeros(len(best)+1)
	y=np.zeros(len(best)+1)
	for i in range(len(best)):
		x[i]=pos[best[i]][0]
		y[i]=pos[best[i]][1]
	x[len(best)]=pos[best[0]][0]
	
	y[len(best)]=pos[best[0]][1]
	
	#plt.figure(title)

	plt.plot(x,y)

	
def violence(dis,N,pos):
	p=[0 for i in range(N)]
	p[0]=1
	path=[]
	bestPath=[]
	path.append(0)
	for i in range(N):
		if p[i]==0:
			p[i]=1
			path.append(i)
			DFS(i,dis,N,dis[0][i],p,path[:],bestPath)
			path.remove(i)
			p[i]=0
	plotB(pos,bestPath,'violence')

def genetic():
	LOP=200
	N=50
	M=100
	pc=0.4
	pm=0.1
	global RR
	variation=0.1
	np.random.seed(10)
	positions=np.random.rand(N,2)
	distances=np.zeros((N,N))
	getDistance(distances,positions)
	init=np.zeros([M,N],dtype=np.int)
	for i in range(M):
		seq=np.array(range(N))
		np.random.shuffle(seq)
		init[i]=seq
	fitness=np.zeros([M,1])
	while LOP>0:
		lens=getLen(distances,init,M)
		getFitness(lens,fitness)
		nn=0
		newgen=np.zeros([M,N],dtype=np.int)
		while nn<M-1:
			father=seletion(fitness,init)
			mother=seletion(fitness,init)
			if np.random.random()>pc:
				length=len(father)
				point1=np.random.random()*(length-1)
				point1=int(point1)
				point2=np.random.random()*(length-1)
				point2=int(point2)
				while point2==point1:
					point2=np.random.random()*(length-1)
					point2=int(point2)
				if point2<point1:
					temp=point2
					point2=point1
					point1=temp
				map=np.zeros(length)

				for i in range(point1,point2):
					map[father[i]]=mother[i]
				son=np.zeros(length,dtype=np.int)
				son[:point1]=mother[:point1]
				son[point1:point2]=father[point1:point2]
				son[point2:]=mother[point2:]
				same=True

				while same==True:
					same=False
					for i in range(point1):
						if son[i] in son[point1:point2]:
							same=True
							son[i]=map[son[i]]
					for i in range(point2,length):
						if son[i] in son[point1:point2]:
							same=True
							son[i]=map[son[i]]
				newgen[nn]=son
				#i=0
				#while i<len(father) and father[i]==mother[i]:
				# 	i+=1
				# start=np.random.random()*(len(father)-i-1)+i
				# start=int(start)
				# if start==len(father)-1:
				# 	start-=1
				# temp=father[0:start+1]
				# newgen[nn][:start+1]=temp[:]
				# newgen[nn][start+1:]=mother[start+1:]
				if np.random.random()>pm:
					start=np.random.random()*(len(father)-1)
					start=int(start)

					end=np.random.random()*(len(father)-1)
					end=int(end)
					while start==end:
						end=np.random.random()*(len(father)-1)
						end=int(end)
					temp=newgen[nn][start]
					newgen[nn][start]=newgen[nn][end]
					newgen[nn][end]=temp
				nn+=1
		newgen[M-1][:]=getMostFitness(fitness,init)
		RR=newgen[M-1][:]
		init=newgen	
		LOP-=1
	plotB(positions,RR,'genetic')
	#violence(distances,N,positions)
	mpl.pyplot.show()
genetic()



