# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 06:41:56 2018

@author: King
"""

import numpy as np
array = np.arange(10)**3

#array(''.join(l+'-10'*(n%3 == 2))for n,l  in enumerate(array))

 
array[0:10:2] = -10


