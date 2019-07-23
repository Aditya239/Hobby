from __future__ import division
import random
import matplotlib.pyplot as plt
import sys

def generate(N,p):
    M = []
    list_row = []
    for i in range(N):
        list_row=[]
        for j in range(N):
            l = random.random()
            if(l<=p):
                list_row+=[1]
            else:
                list_row+=[0]
        M+=[list_row]		
    return M

        	
def percolate(M):
    for i in range(len(M)):
	if(M[0][i]==1):
            M[0][i]=2
         
    
    for i in range(len(M)-1):
    	for j in range(len(M)):
    	    if(M[i+1][j]==1):
    	        if(M[i][j]==2):
    		    M[i+1][j]=2
        for h in range(len(M)):
            if(M[i+1][h]==1):
                if(h-1>=0 and M[i+1][h-1]==2):
                    M[i+1][h]=2

        for g in range(len(M)):
            if(M[i+1][len(M)-1-g]==1):
                if(len(M)-1-g+1<len(M) and M[i+1][len(M)-1-g+1==2]):
                    M[i+1][len(M)-1-g]=2
                

                  
    for i in range(len(M)):
        if(M[len(M)-1][i]==2):
            return 1
    return 0
    
def plot(x,y):
    plt.scatter(x, y, label= "stars", color= "green", marker= "*", s= 30)
    plt.xlabel('Values of p')
    plt.ylabel('Probability of percolation')
    plt.legend()
    plt.show()   
    
def simulate(T,N,p):
    u=[]
    probability=0
    for i in range(T):
    	u=generate(N,p)
    	probability+=percolate(u)
    return probability/T

def main(T,N):
    y=[]
    x=[]
    for i in range(121):
        p=0.2+i*0.005
	x+=[p]
	y+=[simulate(T,N,p)]
    plot(x,y)

	
if __name__ == '__main__':
    if len(sys.argv)!=3:
        print("Wrong number of arguments") 
        sys.exit()

    try:
        T = int(sys.argv[1])
 	N = int(sys.argv[2])
 	
    except:
        print 'Expected input type integer, obtained: ', sys.argv[1], sys.argv[2]
        sys.exit()

    main(T,N)
        


