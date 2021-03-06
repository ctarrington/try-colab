def plot_distributions(rvs, labels):
  ps = np.linspace(0, 1, 200)

  for (rv, label) in zip(rvs, labels):
    plot(ps, rv.pdf(ps), label=label)
    
  plt.legend()
  
def print_ci(rv, ci):
  left = (1-ci)/2
  right = 1-left

  percentiles = rv.ppf([left, 0.5, right])
  print(ci*100, ' of the distribution is between ', percentiles[0], ' and ',
        percentiles[2], ' with a median of ', percentiles[1])

import numpy as np

from matplotlib import pyplot as plt
from matplotlib.pyplot import plot, fill_between, vlines, hlines

leftEdge = 0.00001
rightEdge = 1-leftEdge

def plot_ci(rv, ci, variable):
  [left, right] = rv.ppf([leftEdge, rightEdge])
  leftCI = (1-ci)/2
  rightCI = 1 - leftCI

  ps = np.linspace(left, right, 200)
  [leftPercentile, rightPercentile] = rv.ppf([leftCI, rightCI])

  median = rv.median()
  print('mean: ', rv.mean(), ' median: ', median)
  print('leftCI', leftCI, 'rightCI', rightCI)
  print(ci*100, ' percent confidence interval', leftPercentile, ' to ', rightPercentile)

  fig, (pdf_ax, cdf_ax) = plt.subplots(2, 1, figsize=(12,12))
  pdf_ax.set_xlabel(variable)
  pdf_ax.set_ylabel('Density')

  cdf_ax.set_xlabel(variable)
  cdf_ax.set_ylabel('Cumulative Probability')

  pdf_ax.plot(ps, rv.pdf(ps))
  pdf_ax.vlines(leftPercentile, 0, rv.pdf(leftPercentile))
  pdf_ax.vlines(median, 0, rv.pdf(median), colors='red')
  pdf_ax.vlines(rightPercentile, 0, rv.pdf(rightPercentile))

  print('Probability ', leftPercentile, ' < ', variable, ' < ', rightPercentile, ' = ', rv.cdf(rightPercentile) - rv.cdf(leftPercentile))

  cdf_ax.plot(ps, rv.cdf(ps))
  cdf_ax.hlines(leftCI, left, leftPercentile)
  cdf_ax.vlines(leftPercentile, 0, leftCI)

  cdf_ax.hlines(0.5, left, median, colors='red')
  cdf_ax.vlines(median, 0, 0.5, colors='red')

  cdf_ax.hlines(rightCI, left, rightPercentile)
  cdf_ax.vlines(rightPercentile, 0, rightCI)
