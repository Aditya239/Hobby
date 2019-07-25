                                          #Hobby
## Python related coding exercises with real-life applications.
**What are FRACTALS**

A fractal is a never-ending pattern. Fractals are infinitely complex patterns that are self-similar across different scales.They are created by repeating a simple process over and over in an ongoing feedback loop.

**Julia Set FRACTALS**
The Julia set is named after the French mathematician Gaston Julia who investigated their properties circa 1915 and culminated in his famous paper in 1918.While the Julia set is now associated with a simpler polynomial, Julia was interested in the iterative properties of a more general expression, namely z4 + z3/(z-1) + z2/(z3 + 4 z2 + 5) + c.The Julia set is now associated with those points z = x + iy on the complex plane for which the series zn+1 = zn2 + c does not tend to infinity. c is a complex constant, one gets a different Julia set for each c.The initial value z0 for the series is each point in the image plane. In the broader sense the exact form of the iterated function may be anything, the general form being zn+1 = f(zn), interesting sets arise with non-linear functions f(z). The image is created by mapping each pixel to a rectangular region of the complex plane. Each pixel then represents the starting point for the series, z0. The series is computed for each pixel and if it diverges to infinity it is drawn in white, if it doesn't then it is drawn black.Another property of Julia sets relates to the various domains of c. If c is real then the Julia set is mirrored about the real axis. Other values of c with a non-zero imaginary component have 180 degree rotational symmetry.

Some of the patterns obtained for different values of c are shown below:
For c = 0.37+0.1i :
<img src="Julia/julia.png" width="400"/>
For c = -0.4+-0.59i :
<img src="Julia/julia_0.4_0.59.png" width="400"/>
For c = 0.355+0.355i :
<img src="Julia/julia_0.355_0.355.png" width="400"/>
For c = -0.54+0.54i :
<img src="Julia/julia_0.54_0.54.png" width="400"/>


Graph of probability generated from program:

<img src="Percolation Thresholds in Square/probability_graph.png" width="400"/>
