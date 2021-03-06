#!/usr/bin/env python

"""The purpose of this test is to provide coverage of energy distributions that
are not covered in other tests. It has a single material with the following
nuclides:

U-233: Only nuclide that has a Watt fission spectrum

H-2: Only nuclide that has an N-body phase space distribution, in this case for
(n,2n)

Na-23: Has an evaporation spectrum and also has reactions that have multiple
angle-energy distributions, so it provides coverage for both of those
situations.

Ta-181: One of a few nuclides that has reactions with Kalbach-Mann distributions
that use linear-linear interpolation.

"""

import glob
import os
import sys
sys.path.insert(0, os.pardir)
from testing_harness import TestHarness


if __name__ == '__main__':
    harness = TestHarness('statepoint.10.*')
    harness.main()
