from __future__ import division
import matplotlib.pyplot as plt
import sys

def flipud(X):
    '''This function takes in a list of lists
    and flips it upside down, i.e. the first list in 
    the list of lists becomes the last, the second list
    becomes the second last and so on, while the last list
    becomes the first. None of lists are modified however.
    Eg: if X    = [[1,  2, 3], [0, 3, 5], [5, -1, 2]]
    Then output = [[5, -1, 2], [0, 3, 5], [1,  2, 3]]
    '''
    
    # Your code here
    X.reverse()
    return X

def plot(Frac, height, width):
    ''' This function just uses the matplotlib library
    to plot and make an image representation of the passed
    2D array (actually list of lists) Z, saves it and 
    displays it.
    '''
    fig = plt.figure()
    fig.set_size_inches(width / 100, height / 100)
    ax = fig.add_axes([0, 0, 1, 1], frameon=False, aspect=1)
    ax.set_xticks([])
    ax.set_yticks([])
    # For some reason we want to flip the image 
    # upside down and then plot
    plt.imshow(flipud(Frac), cmap='hot')
    plt.savefig('julia.png')
    plt.show()
    plt.close()

def compute(height, width, scale, const):
    ''' This function actually computes the fractal set
    We take the pixel sizes in each axes (height and width: integers)
    and scale as input and return the fractal set computed as described.
    It uses the complex const supplied as input as an argument as well
    '''

    # Your code here
    number=0+1j*0
    list_row=[]
    final_answer=[]
    for i in range(height):
        number=-(width/scale)+1j*((-height/scale)+i*(2*height/(scale*(height-1))))
        for k in range(width):
            if(k!=0):
                number=number+(2*width/(scale*(width-1)))
            list_row=[number]
        final_answer=[[list_row]] 

    return [[0]*width]*height

def main(const):
    # Setting the window sizes: pixels across edges
    height = 480
    width  = 720
    # This describes how zoomed in we will be
    scale  = 450
    FractalSet = compute(height, width, scale, const)
    plot(FractalSet, height, width)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print ("Wrong number of arguments! Enter complex constant: First the real part, then the complex part.\n"
               "Example Usage: python julia.py -0.4 0.6 (Complex constant, c = -0.4 + 0.6j)\n")
        sys.exit()
    try:
        Re = float(sys.argv[1])
        Im = float(sys.argv[2])
    except:
        print 'Expected input type float, obtained: ', sys.argv[1], sys.argv[2]
        sys.exit()
    c = Re + 1j * Im
    main(c)
