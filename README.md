# Warehouse Project

This project is built by Christian Madsen.


## General Introduction

This project is a work in progress prototype for a automatic warehouse sorting application. The gist is to be able to input data from a warehouse system, extract the info, and calculate the most suitable placement for each ware in terms of multiple factors. 

### Mathmatical Basis

For the prototype version 1.0, the sorting is based on a simple cost reduction function. It calculates the cost of each individual location and ware in terms of a given starting point. It favours placing large-high sales wares closer to the starting point. 

Initially, the algorithm calculates a $D_l$ and $R_l$ of which the $D_l$ value which is the normalized cost value of each location based on the distance from the given start point. The $R_l$ value is the normalized cost value of each location based on the total amount of positions in the warehouse with reference to the given start point. This gives a 2D mapping in which $D_l$ will all have a value of 0 in every location that is right next to the starting point (in this case a main road stretching beside the rows of shelves) and an $R_l$ value that starts at 0 for the very first location (given a certain start point) and increases afterwards.

$D_l$ calculations as such:

$$
D_l = \frac{d_l-d_{min}}{d_{max}-d_{min}}
$$

where:

$$
d_l = \text{distance to given location}
$$

$$
d_{min}\hspace{1mm}  \text{and} \hspace{1mm} d_{max} = \text{minimum and maximum distance respectively}
$$

Similarly calculations for $R_l$ follows the same logic:

$$
R_l = \frac{r_l-r_{min}}{r_{max}-r_{min}}
$$

where: 

$$
r_l = \text{given location}$$

$$
r_{min}\hspace{1mm}  \text{and} \hspace{1mm} r_{max} = \text{minimum and maximum amount of locations}
$$

**Cost Function**

Current weights of the cost function only includes weights for weight of the ware and sales numbers $\alpha$ and $\beta$ respectively of which:

$$
\alpha \hspace{1mm} \& \hspace{1mm} \beta \in [0,1]
$$

The cost function is built around minimizing the cost of the location based on the wares weight and sales number per month (this is subject to change as multiple other parameters such as dimensions could be important). 


