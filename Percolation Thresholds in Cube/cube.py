from __future__ import division
import random
import matplotlib.pyplot as plt
import sys

def generate(N,p):
    three_d=[]
    M=[]
    list_row=[]
    for i in range(N):
        M=[]
        for j in range(N):
            list_row=[]
            for k in range(N):
                l = random.random()
                if(l<=p):
                    list_row+=[1]
                else:
                    list_row+=[0]
            M+=[list_row]
        three_d+=[M]
    return three_d

def percolate(M):
    for r in range(len(M)):
        for q in range(len(M)):
            if(M[0][r][q]==1):
                M[0][r][q]=2

    for i in range(len(M)-1):
        for j in range(len(M)):
            for k in range(len(M)):
                if(M[i+1][j][k]==1):
                    if(M[i][j][k]==2):
                        M[i+1][j][k]=2
        for g in range(len(M)):
            for h in range(len(M)):
                if(M[i+1][g][h]==1):
                    if(h-1>=0 and M[i+1][g][h-1]==2):
                        M[i+1][g][h]=2
        for a in range(len(M)):
            for b in range(len(M)):
                if(M[i+1][a][len(M)-1-b]==1):
                    if(len(M)-1-b+1<len(M) and M[i+1][a][len(M)-1-b+1]==2):
                        M[i+1][a][len(M)-1-b]=2
        for u in range(len(M)):
            for v in range(len(M)):
                if(M[i+1][v][u]==1):
                    if(v-1>=0 and M[i+1][v-1][u]==2):
                        M[i+1][v][u]=2
        for c in range(len(M)):
            for d in range(len(M)):
                if(M[i+1][len(M)-1-d][c]==1):
                    if(len(M)-1-d+1<len(M) and M[i+1][len(M)-1-d+1][c]==2):
                        M[i+1][len(M)-1-d][c]=2
                                      

    for w in range(len(M)):
        for z in range(len(M)):
            if(M[len(M)-1][w][z]==2):
                return 1
        return 0


def plot(x,y):

    min=abs(0.5-y[0])
    pos=0
    for i in range(len(x)-1):
        if(abs(0.5-y[i+1])<min):
            min=abs(0.5-y[i+1])
            pos=i+1

    plt.scatter(x, y, label= r'$p$', facecolor = 'red', edgecolor = 'black', marker= 'o', s = 30)
    plt.xlabel('Values of p')
    plt.ylabel('Probability of percolation')
    plt.legend()
    plt.axvline(x[pos],color='red',linewidth=3,linestyle='dotted')
    plt.text(x[pos],0,x[pos],fontsize=15)
    plt.savefig('probability_graph_cube.png')
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
