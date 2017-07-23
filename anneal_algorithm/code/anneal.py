import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import math
def getPathDis(dis,path):
	d=dis[path[-1]][path[0]]
	for i in range(1,len(path)):
		d+=dis[path[i-1]][path[i]]
	return d

def getDis(dis,pos,N):
	for i in range(N):
		for j in range(i,N):
			dis[i][j]=math.sqrt((pos[i][0]-pos[j][0])**2+(pos[i][1]-pos[j][1])**2)
			dis[j][i]=dis[i][j]

def getInitTemperature(dis,n):
	K=200
	f_min=0
	f_max=0
	for i in range(n):
		fmax=0
		fmin=0x7fffffff
		for j in range(n):
			if i==j:
				continue
			if dis[i][j]>fmax:
				fmax=dis[i][j]
			if dis[i][j]<fmin:
				fmin=dis[i][j]
		f_min+=fmin
		f_max+=fmax
	return K*(f_max-f_min)
def getNext(path,N):
	index1=int(np.random.random()*(N-1))
	index2=int(np.random.random()*(N-1))
	while index1==index2:
		index2=int(np.random.random()*(N-1))
	newPath=np.zeros(N,dtype=np.int)	
	newPath[:]=path[:]
	temp=newPath[index1]
	newPath[index1]=newPath[index2]
	newPath[index2]=temp
	return newPath
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
	plt.plot(x,y)
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
			return 
	for i in range(N):
		if p[i]==0:
			p[i]=1
			path.append(i)
			DFS(i,dis,N,dis[start][i]+length,p,path[:],bestPath)
			path.remove(i)
			p[i]=0
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
def anneal():
	N=30
	delta=0.99
	T_main=1e-8
	T=0
	repeat_time=10
	result=np.array(list(range(N)))
	pos=np.random.rand(N,2)
	dis=np.zeros([N,N])
	getDis(dis,pos,N)
	length=getPathDis(dis,result)
	T=getInitTemperature(dis,N)
	while T>T_main and repeat_time>0:
		newpath=getNext(result,N)
		f1=getPathDis(dis,newpath)
		f2=getPathDis(dis,result)
		dE=f1-f2
		if dE<0:
			result[:]=newpath[:]
		else:
			if math.exp(-dE/T)>np.random.random() and math.exp(-dE/T)<1:
				result[:]=newpath[:]
				#print(math.exp(dE/T))
		T*=delta
	plotB(pos,result,'anneal')
	#violence(dis,N,pos)
	plt.show()

	# print(length)
anneal()

