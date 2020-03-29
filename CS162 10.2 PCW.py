#!/usr/bin/env python
# coding: utf-8

# ### Unit testing

# In[ ]:


import math

    # BIGFACTOR represents the product of all prime factors under 100.  This allows
    # us to do a fast pre-check and immediately eliminate any numbers which are
    # divisible by a small number
    
def is_prime(x):

    '''
    Function adobted from GeeksForGeeks
    '''
    if x < 2:
         return False
    if x % 2 == 0:             
         return x == 2
    k = 3
    while k*k <= x:
        if x % k == 0:
            return False
        k += 2
    return True


def get_next_prime(x):
    ''' 
    Find the smallest prime number which is greater than or equal to x
    '''
    if x % 2 == 0:
        x = x + 1
    while not is_prime(x):
        x = x + 2

    return x


# In[ ]:


import numpy as np

# This application uses two large prime numbers to implement public key
# cryptography. It generates a public key and a private key.  The
# keys are symmetric, so if one key is used to encrypt, then the other can be
# used to decrypt.

p1 = get_next_prime(np.int64(2**63 - 1))
p2 = get_next_prime(np.int64(2**62 - 1))

print(p1)
print(p2)

# Now we have found two large prime numbers and can start to perform public
# key cryptography.
# ...
# Pretend that there was more code here.


# In[9]:


import unittest

class PrimeTests(unittest.TestCase):

    def test_is_seven_prime(self):
        self.assertTrue(is_prime(7))
        
    def test_is_two_prime(self):
        self.assertTrue(is_prime(2))

    def test_bigger_prime_of_twelve(self):
        self.assertEqual(get_next_prime(12), 13)

    def test_bigger_prime_of_thirteen(self):
        self.assertEqual(get_next_prime(13), 13)
        
    def test_bigger_prime_of_24(self):
        self.assertEqual(get_next_prime(24), 29)
        
unittest.main(argv=[''], verbosity=2, exit=False)


# ### The output of running coverage on tests.py

# In[ ]:


"""
(base) C:\Users\Taha>coverage run -m pytest tests.py
============================= test session starts =============================
platform win32 -- Python 3.7.1, pytest-4.0.2, py-1.7.0, pluggy-0.8.0
rootdir: C:\Users\Taha, inifile:
plugins: remotedata-0.3.1, pylint-0.14.1, openfiles-0.3.1, doctestplus-0.2.0, arraydiff-0.3
collected 5 items

tests.py .....                                                           [100%]

========================== 5 passed in 0.03 seconds ===========================

(base) C:\Users\Taha>coverage report -m tests.py
Name       Stmts   Miss  Cover   Missing
----------------------------------------
tests.py      30      1    97%   15

(base) C:\Users\Taha>
"""

