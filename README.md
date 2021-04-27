# PFSP_OPTIMISATION

## Abstract
The Permutation Flow Shop Problem is a data science problem with multiple different possible ways to approach. We were elected to utilise random search and genetic algorithms to find the most efficient way to set up a car manufacturing flowshop. We found that genetic algorithm takes longer to run but produces more accurate result than random search.

## PFSP
The permutation flowshop problem (PFSP) is one of the most studied problems in Operational Research (OP). Understanding and solving this kind of problems is essential to businesses in various industries to optimise their production times. Including manufacturing, transportation, healthcare, etc. The PFSP is a type of scheduling optimisation problem, where a set N of n jobs must be processed on a set M of m machines. Each job must visit all machines in the same order (Benbouzid-Si, et al., 2017). In such problems, the design of the system would enable a certain schedule to be the most efficient out of all the possible scheduling scenarios. Hence, the goal of the PFSP is to minimise the maximum completion time, also known as makespan, by finding the best sequence (π).

The aim of this project is to provide an optimal sequence or permutation which generates the least amount of production time to a car manufacturing company, BWM. The original dataset contains 800 jobs and 60 machines.

In order to achieve the objective, extensive data wrangling and analysis must be done. Firstly, the dataset must be cleared out from any inconsistencies the original dataset presents, and be divided into smaller data samples to facilitate the speed and the efficiency of finding the optimal solution. Secondly, to start the optimisation process, two metaheuristics are applied into each of the data samples: the random search algorithm & the genetic algorithm. 



