#!/usr/bin/env python
# coding: utf-8

# # Task 1:
# ### Using Newton’s method choose x0 and find the root of the equation x+ex=0 with accuracy 0.01. How many iterations needed?

# # Steps Taken in this code
# #### 1. Define function as f(x)
#
# #### 2. Visualize Function with all possible x
#
# #### 3. Define first derivative of f(x) as g(x)
#
# #### 4. Input initial guess (x0), tolerable error (e) and maximum iteration (N)
#
# #### 5. Initialize iteration counter i = 1
#
# #### 6. If g(x0) = 0 then print "Mathematical Error" and goto (12) otherwise goto (7)
#
# #### 7. Calcualte x1 = x0 - f(x0) / g(x0)
#
# #### 8. Increment iteration counter i = i + 1
#
# #### 9. If i >= N then print "Not Convergent" and goto (12) otherwise goto (10)
#
# #### 10. If |f(x1)| > e then set x0 = x1 and goto (6) otherwise goto (11)
#
# #### 11. Print root as x1

# #### Import Libraries

# In[1]:


import math
import numpy as np
import matplotlib.pyplot as plt


# ### Function

# In[2]:


def f(x):
    return x + (math.e**x)


# ### Derivative

# In[3]:


def g(x):
    return 1 + (math.e**x)


# ### Newton method Solver

# In[4]:


class NewtonSolver:
    """
    Class NewtonSolver:
    A Newton’s method solver for numerically finding roots of an equation
    """
    def newton(self, x0, e, N):
        """
        A step by step solver, with iterations
        :param x0: Guessed x
        :param e: Tolerable Error
        :param N: Maximum number of iteration
        :return: Number of iteration and the required root
        """
        global x1
        print('\n\n*** NEWTON METHOD IMPLEMENTATION***')
        step = 1
        flag = 1
        condition = True

        # Iterations ( repeat until we are done)
        while condition:
            if g(x0) == 0.0:
                print('Divide by zero error!')
                break

            x1 = x0 - f(x0) / g(x0)
            print('Iteration - %d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f(x1)))
            x0 = x1
            step = step + 1

            if step > N:
                flag = 0
                break

            condition = abs(f(x1)) > e

        if flag == 1:
            print('\nRequired root is: %0.8f' % x1)
        else:
            print('\nNot Convergent.')

    def plotter(self):
        """
        Visualise the function
        :return: function graph
        """
        # define left and right boundaries for plotting
        interval_left = -2
        interval_right = 2

        # define x grid of points for computation and plotting the function
        # increase num at your convenience, but with caution. Article figure has 10 000
        xvals = np.linspace(interval_left, interval_right, num=100)
        # define y values for example function
        yvals = f(xvals)
        # create a list of startin points for Newton's method
        pointlist = xvals
        # begin figure for plotting
        plt.figure()
        # plot the function f
        plt.plot(xvals, yvals)
        plt.hlines(0, interval_left, interval_right)
        # label the axes
        plt.xlabel("$x$", fontsize=26)
        plt.ylabel("$f(x)$", fontsize=26)
        # set limits for the x and y axes in the figure
        # set x limits
        plt.xlim((interval_left, interval_right))
        # set y limits
        return plt.ylim((-5, 5))

    def solve(self):
        """
        Inputing the values
        :return: Result
        """
        # Input Numbers
        x0 = input('X0: ')
        e = input('Tolerable Error: ')
        N = input('Maximum Number of steps: ')

        x0 = float(x0)
        e = float(e)
        N = int(N)

        print('X0 = {}\nTolerable Error: = {}\nMaximum Number of steps = {}'.format(x0, e, N))
        return self.newton(x0, e, N)


# In[5]:


x = NewtonSolver()


# ### Plot the function

# In[6]:


x.plotter()


# ### Solve

# In[7]:


x.solve()

