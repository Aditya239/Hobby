# Hobby
### Python related coding exercises with real-life applications.

## Julia Fractals

**What are Fractals**

A fractal is a never-ending pattern. Fractals are infinitely complex patterns that are self-similar across different scales.They are created by repeating a simple process over and over in an ongoing feedback loop.

**Julia Set Fractals**

The Julia set is named after the French mathematician Gaston Julia who investigated their properties circa 1915 and culminated in his famous paper in 1918. While the Julia set is now associated with a simpler polynomial, Julia was interested in the iterative properties of a more general expression, namely ![equation](https://latex.codecogs.com/png.latex?z%5E4%20&plus;%20z%5E3/%28z-1%29%20&plus;%20z%5E2/%28z%5E3%20&plus;%204%20z%5E2%20&plus;%205%29%20&plus;%20c) .The Julia set is now associated with those points ![equation](https://latex.codecogs.com/png.latex?x&plus;iy) on the complex plane for which the series ![equation](https://latex.codecogs.com/png.latex?z_%7Bn&plus;1%7D%20%3D%20z_%7Bn%7D%5E2%20&plus;%20c) does not tend to infinity. ![equation](https://latex.codecogs.com/png.latex?c) is a complex constant, one gets a different Julia set for each ![equation](https://latex.codecogs.com/png.latex?c).The initial value ![equation](https://latex.codecogs.com/png.latex?z_0) for the series is each point in the image plane. In the broader sense the exact form of the iterated function may be anything, the general form being ![equation](https://latex.codecogs.com/png.latex?z_%7Bn&plus;1%7D%20%3D%20f%28z_n%29), interesting sets arise with non-linear functions ![equation](https://latex.codecogs.com/png.latex?f%28z%29). The image is created by mapping each pixel to a rectangular region of the complex plane. Each pixel then represents the starting point for the series, ![equation](https://latex.codecogs.com/png.latex?z_0). The series is computed for each pixel and if it diverges to infinity it is drawn in white, if it doesn't then it is drawn black.Another property of Julia sets relates to the various domains of ![equation](https://latex.codecogs.com/png.latex?c). If ![equation](https://latex.codecogs.com/png.latex?c) is real then the Julia set is mirrored about the real axis. Other values of ![equation](https://latex.codecogs.com/png.latex?c) with a non-zero imaginary component have 180 degree rotational symmetry.

Some of the patterns obtained for different values of ![equation](https://latex.codecogs.com/png.latex?c) are shown below:

| | |
|:-------------------------:|:-------------------------:|
|<img width="400" src="Julia/julia.png">   ![equation](https://latex.codecogs.com/png.latex?c%20%3D%200.37&plus;0.1i) |  <img width="400" src="Julia/julia_0.4_0.59.png">    ![equation](https://latex.codecogs.com/png.latex?c%20%3D%20-0.4&plus;-0.59i)|
|<img width="400" src="Julia/julia_0.355_0.355.png">  ![equation](https://latex.codecogs.com/png.latex?c%20%3D%200.355&plus;0.355i)|  <img width="400" src="Julia/julia_0.54_0.54.png">   ![equation](https://latex.codecogs.com/png.latex?c%20%3D%20-0.54&plus;0.54i)|

## **Percolation Thresholds in Square and Cubic Lattices**

The percolation threshold is a mathematical concept in percolation theory that describes the formation of long-range connectivity in random systems. Below the threshold a giant connected component does not exist; while above it, there exists a giant component of the order of system size. In engineering and coffee making, percolation represents the flow of fluids through porous media, but in the mathematics and physics worlds it generally refers to simplified lattice models of random systems or networks (graphs), and the nature of the connectivity in them. The percolation threshold is the critical value of the occupation probability p, or more generally a critical surface for a group of parameters p1, p2, ..., such that infinite connectivity (percolation) first occurs.

Here we consider only Square and Simple Cubic percolation models.

**Simplifying Assumption**

While in the general case, percolation path from the first row to the last can be such that vacant sites on the path can lie on any adjacent edge, we will make the assumption that percolation is forward only.

Site percolation threshold plots for simple square and cubic lattice models against site vacancy probability is given below:

| | |
|:-------------------------:|:-------------------------:|
|<img width="400" src="Percolation Thresholds in Square/probability_graph.png">   Site percolation threshold for Simple Square Lattice |  <img width="400" src="Percolation Thresholds in Cube/probability_graph_cube.png">    Site percolation threshold for Simple Cubic Lattice|
