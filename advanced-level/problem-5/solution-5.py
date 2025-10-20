from scipy.stats import pearsonr

X = [10, 20, 30, 40, 50]
Y = [10, 27, 35, 45, 55]

corr,p_value= pearsonr(X, Y)
print("Pearson correlation coefficient:", corr,p_value)
