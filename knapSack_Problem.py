# KnapSack Problem  (Maximum Profit with less Weight)

def knapSack(m, weight, profit, n):
   K = [[0 for x in range(m + 1)] for x in range(n + 1)]
   for i in range(n + 1):
      for j in range(m + 1):
         if i == 0 or j == 0:
            K[i][j] = 0
         elif weight[i-1] <= j:
            K[i][j] = max(profit[i-1] + K[i-1][j-weight[i-1]], K[i-1][j])
         else:
            K[i][j] = K[i-1][j]
   return K[n][m]
profit = [50,100,150,200]
weight = [8,16,32,40]
m = 64
n = len(profit)
print(knapSack(m, weight, profit, n))
