import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import math
def distance(pos,dis,n):
	for i in range(n):
		for j in range(i,n):
			dis[i][j]=math.sqrt((pos[i][0]-pos[j][0])**2+(pos[i][1]-pos[j][1])**2)
			dis[j][i]=dis[i][j]
def initPheromen(T,dis,n):
	for i in range(n):
		for j in range(n):
			if i==j:
				T[i][j]=0
			else:
				T[i][j]=1/dis[i][j]
def check(path,n):
	for i in range(n):
		if path[i]==0:
			return False
	return True
def getNext(path,N,T,start):
	rate=np.zeros(N)
	total=0
	for i in range(N):
		if path[i]==1 or start==i:
			rate[i]=0
		else:
			total+=T[start][i]

	for i in range(N):
		if path[i]==1 or start==i:
			rate[i]=0
		else:
			rate[i]=T[start][i]/total
	sel=np.random.random()
	sel_cur=0
	for i in range(N):
		sel_cur+=rate[i]
		if sel_cur>=sel:
			return i
minlenght=0x7fffffff		
def checkAll(path,M,N):
	for i in range(M):
		if len(path[i])!=N:
				return False
	return True
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
	#plt.show()
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
def ant():
	N=25
	M=5
	C=0
	limit=20
	bestPath=[0 for i in range(N)]
	#
	pos=np.random.rand(N,2)
	#
	dis=np.zeros([N,N])
	#
	T=np.zeros([N,N])
	#


	distance(pos,dis,N)
	initPheromen(T,dis,N)
	#
	maxWeight=0x7fffffff
	maxI=0
	while limit>0:
		mark=np.zeros([M,N])
		path=[[0] for i in range(M)]
		while checkAll(path,M,N)==False:
			for i in range(M):
				if check(mark[i],N)==True:
					continue
				else:
					mark[i][0]=1
					j=getNext(mark[i],N,T,path[i][-1])
					path[i].append(j)
					mark[i][j]=1	
		weight=[0 for i in range(M)]

		for i in range(M):
			if len(path[i])!=N:
				weight[i]=0x7fffffff
				continue
			_dis=dis[path[i][0]][path[i][-1]]
			for j  in range(1,N):
				_dis+=dis[path[i][j-1]][path[i][j]]
			if _dis<maxWeight:
				limit=20
				maxWeight=_dis
				maxI=i
				bestPath[:]=path[i]

		pk=0
		arc=[]
		arc.append((bestPath[0],bestPath[-1]))
		arc.append((bestPath[-1],bestPath[0]))
		for i in range(1,N):
			arc.append((bestPath[i],bestPath[i-1]))
			arc.append((bestPath[i-1],bestPath[i]))
		if C==0:
			pk=0.1
		else:
			pk=1-(math.log(C,math.e))/(math.log(C+1,math.e))
		pc=0.1
		for i in range(N):
			for j in range(i+1):
				if (i,j) in arc:
					#print((i,j))
					T[i][j]=T[j][i]=(1-pk)*T[i][j]+pk/maxWeight
				else:
					T[i][j]=T[j][i]=(1-pk)*T[i][j]
		limit-=1
	plotB(pos,bestPath,'ant')
	#violence(dis,N,pos)
	plt.show()
ant()





