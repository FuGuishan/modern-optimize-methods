import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import math
class BP(object):
	in_num=0
	hd_num=0
	ou_num=0
	eta_w=0.1
	eta_b=0.1

	_layer=3
	_error=0.001
	_accu=0.000001
	def createData(self):
		_file=open('test.txt','w')
		strx=['x']
		stry=['y']
		x=np.linspace(0,1,50)
		y=x*x
		for i in x:
			strx.append(str(i))
		for i in y:
			stry.append(str(i))
		for s in strx:
			_file.write(s+'\n')
		for s in stry:
			_file.write(s+'\n')

		_file.close()

	def init(self):
		#print('ads')
		self.in_num=len(self.in_data[0])
		self.ou_num=len(self.out_data[0])
		self.hd_num=int(math.sqrt(self.in_num+self.ou_num))+5
		if self.hd_num>15:
			self.hd_num=15

	def readFile(self):
		in_data=[]
		out_data=[]
		_file=open('test.txt')
		try:
			while 1:
				line=_file.readline().strip('\n')
				while line:
					line=_file.readline().strip('\n')
				#p=[]
				
					if line=='y':
						break
					p=line.split(' ')
					in_data.append(p[:])
					#print(self.in_data)
				line=_file.readline().strip('\n')
				while line:
					p=line.split(' ')
					out_data.append(p[:])
					#print(self.out_data)
					line=_file.readline().strip('\n')
				#print(line)
				if not line:
					break
				#_text=_file.read()
		#print(_text)
		finally:
			_file.close()
		self.in_data=np.array(in_data,dtype=np.float64)
		self.out_data=np.array(out_data,dtype=np.float64)


	def getError(self,index):
		t=0
		for i in range(self.ou_num):
			# print(self.x[2][i],'aaaaaaaa','mmm')
			# print(self.out_data[index][i],'adad')
			# print(self.x.dtype)
			# print(self.out_data.dtype)
			t+=(self.x[2][i]-self.out_data[index][i])**2
		t*=0.5
		return t

	def sigmoid(self,t):
		return 1/(1+math.exp(-t))

	def forwardTransfor(self):
		for i in range(self.hd_num):
			t=0
			for j in range(self.in_num):
				t+=self.w[1][j][i]*self.x[0][j]
			t+=self.b[1][i]
			self.x[1][i]=self.sigmoid(t)
		for i in range(self.ou_num):
			t=0
			for j in range(self.hd_num):
				t+=self.w[2][j][i]*self.x[1][j]
			t+=self.b[2][i]
			self.x[2][i]=self.sigmoid(t)
	def backwordTransfor(self,index):

		for i in range(self.ou_num):
			#print(self.out_data[index][i])
			self.d[2][i]=(self.x[2][i]-self.out_data[index][i])*(1-self.x[2][i])*self.x[2][i]
		for i in range(self.hd_num):
			t=0
			for j in range(self.ou_num):
				t+=self.d[2][j]*self.w[2][i][j]
			self.d[1][i]=(1-self.x[1][i])*self.x[1][i]*t
		for i in range(self.ou_num):
			for j in range(self.hd_num):
				self.w[2][j][i]-=self.x[1][j]*self.eta_w*self.d[2][i]
		for i in range(self.ou_num):
			self.b[2][i]-=self.eta_b*self.d[2][i]
		for i in range(self.in_num):
			for j in range(self.hd_num):
				self.w[1][i][j]-=self.x[0][i]*self.eta_w*self.d[1][j]
		for i in range(self.hd_num):
			self.b[1][i]-=self.eta_b*self.d[1][i]
	def getAcc(self):
		size=len(self.in_data)
		t=0
		for i in range(size):
			for j in range(self.in_num):
				self.x[0][j]=self.in_data[i][j]
			self.forwardTransfor()
			for j in range(self.ou_num):
				t+=(self.x[2][j]-self.out_data[i][j])**2
				t*=0.5
		return t/size
	def train(self):
		self.init()
		max_num=max(self.in_num,self.ou_num,self.hd_num)
		
		self.w=np.random.rand(self._layer,max_num,max_num)
		self.b=np.zeros([self._layer,max_num])
		self.d=np.zeros([self._layer,max_num])
		self.x=np.zeros([self._layer,max_num])
		C=0
		size=len(self.in_data)
		while C<50000:
			for i in range(size):

				for j in range(self.in_num):
					self.x[0][j]=self.in_data[i][j]
				while True:
					self.forwardTransfor()
					#print(self.getError(i))
					#print(self.getError(i))
					if self.getError(i)<self._error:
						break
					self.backwordTransfor(i)
			#print(self.getAcc(),'sadasda')	
			if self.getAcc()<self._accu:
				break
			C+=1


	def forcast(self,pin):
		for i in range(self.in_num):
			self.x[0][i]=pin[i]
		print(self.x)
		self.forwardTransfor()
		return self.x[2]
def main():
	
	bp=BP()
	#bp.createData()
	bp.readFile()
	bp.train()
	pin=np.array([0.7])
	print(bp.forcast(pin))
if __name__ == '__main__':
	main()
