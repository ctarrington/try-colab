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
