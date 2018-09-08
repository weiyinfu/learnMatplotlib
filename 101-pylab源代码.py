"""
pylab模块就是一堆import
"""

from matplotlib.externals import six

import sys, warnings

from matplotlib.cbook import flatten, is_string_like, exception_to_str, \
     silent_list, iterable, dedent

import matplotlib as mpl
# make mpl.finance module available for backwards compatability, in case folks
# using pylab interface depended on not having to import it
import matplotlib.finance

from matplotlib.dates import date2num, num2date,\
        datestr2num, strpdate2num, drange,\
        epoch2num, num2epoch, mx2num,\
        DateFormatter, IndexDateFormatter, DateLocator,\
        RRuleLocator, YearLocator, MonthLocator, WeekdayLocator,\
        DayLocator, HourLocator, MinuteLocator, SecondLocator,\
        rrule, MO, TU, WE, TH, FR, SA, SU, YEARLY, MONTHLY,\
        WEEKLY, DAILY, HOURLY, MINUTELY, SECONDLY, relativedelta

import matplotlib.dates  # Do we need this at all?

# bring all the  symbols in so folks can import them from
# pylab in one fell swoop


## We are still importing too many things from mlab; more cleanup is needed.

from matplotlib.mlab import griddata, stineman_interp, slopes, \
    inside_poly, poly_below, poly_between, \
    is_closed_polygon, path_length, distances_along_curve, vector_lengths

from matplotlib.mlab import window_hanning, window_none,  detrend, demean, \
     detrend_mean, detrend_none, detrend_linear, entropy, normpdf, \
     find, longest_contiguous_ones, longest_ones, \
     prctile, prctile_rank, \
     center_matrix, rk4, bivariate_normal, get_xyz_where, \
     get_sparse_matrix, dist, \
     dist_point_to_segment, segments_intersect, fftsurr, movavg, \
     exp_safe, \
     amap, rms_flat, l1norm, l2norm, norm_flat, frange,  identity, \
     base_repr, binary_repr, log2, ispower2, \
     rec_append_fields, rec_drop_fields, rec_join, csv2rec, rec2csv, isvector

import matplotlib.mlab as mlab
import matplotlib.cbook as cbook

from numpy import *
from numpy.fft import *
from numpy.random import *
from numpy.linalg import *

from matplotlib.pyplot import *

# provide the recommended module abbrevs in the pylab namespace
import matplotlib.pyplot as plt
import numpy as np
import numpy.ma as ma

# don't let numpy's datetime hide stdlib
import datetime

# This is needed, or bytes will be numpy.random.bytes from
# "from numpy.random import *" above
bytes = __builtins__['bytes']
