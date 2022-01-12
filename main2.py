#!/usr/bin/env python
# coding: utf-8

# # Task 2
# ## Solve system of linear equations using Jacobi method with accuracy 0,1.
# ### -3x + 2y - 6z = 14
# ### 4x - 5y + 2z = -3
# ### 7x + 9y + 3z = 14

# # Steps Taken in this code
#
# #### 1. Arrange given system of linear equations in diagonally dominant form
#
#
# #### 2. Read tolerable error (e)
#
#
# #### 3. Convert the first equation in terms of first variable, second equation in terms of second variable and so on.
#
#
# #### 4. Set initial guesses for x0, y0, z0 and so on
#
#
# #### 5. Substitute value of x0, y0, z0 ... from step 5 in equation obtained in  step 4 to calculate new values x1, y1, z1 and so on
#
#
# #### 6. If| x0 - x1| > e and | y0 - y1| > e and | z0 - z1| > e and so on then goto step 9
#
#
# #### 7. Set x0=x1, y0=y1, z0=z1 and so on and goto step 6
#
#
# #### 8. Print value of x1, y1, z1 and so on

# In[1]:


# Defining equations to be solved
# in diagonally dominant form
f1 = lambda x,y,z: (14-9*y-3*z)/7
f2 = lambda x,y,z: (-3-4*x-2*z)/-5
f3 = lambda x,y,z: (14+3*x-2*y)/-6

# Initial setup
x0 = 0
y0 = 0
z0 = 0
count = 1

# Reading tolerable error
e = float(input('tolerable error: '))
print('Tolerable error = {}'.format(e))

# Implementation of Jacobi Iteration
print('\nCount\tx\ty\tz\n')

condition = True

while condition:
    x1 = f1(x0,y0,z0)
    y1 = f2(x0,y0,z0)
    z1 = f3(x0,y0,z0)
    print('%d\t%0.4f\t%0.4f\t%0.4f\n' %(count, x1,y1,z1))
    e1 = abs(x0-x1);
    e2 = abs(y0-y1);
    e3 = abs(z0-z1);

    count += 1
    x0 = x1
    y0 = y1
    z0 = z1

    condition = e1>e and e2>e and e3>e

print('\nSolution: x=%0.3f, y=%0.3f and z = %0.3f\n'% (x1,y1,z1))

