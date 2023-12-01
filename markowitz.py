import numpy as np
import matplotlib.pyplot as plt
import cvxopt as opt
from cvxopt import blas, solvers
import pandas as pd

np.random.seed(123)

# 关掉进度展示，进度展示是运行过程进度的一个打印输出，可以通过其查看代码运行进度
solvers.options['show_progress'] = False

# 加载数据
df = pd.read_excel('E:\\大四第一段\\數學建模比賽\\longterm average return.xlsx')

# 仅保留收益率数据
return_vec = df.iloc[:, 1:]

def optimal_portfolio(returns):
    n = len(returns)
    returns = np.asmatrix(returns)
    
    N = 19
    mus = [-0.12+0.01*i for i in range(N)]
    
    # 转化为cvxopt matrices
    P = opt.matrix(np.cov(returns))
    q = opt.matrix(np.zeros((n, 1)))
    pbar = opt.matrix(np.mean(returns, axis=1))

    # 约束条件
    G = opt.matrix(np.concatenate((-np.array(pbar).T,-np.eye(n)),0))   # opt默认是求最大值，因此要求最小化问题，还得乘以一个负号
    A = opt.matrix(1.0, (1, n))
    b = opt.matrix(1.0)
    
    # 使用凸优化计算有效前沿
    portfolios = [solvers.qp(P, q, G, opt.matrix(np.concatenate((-np.ones((1, 1)) * mu, np.zeros((n, 1))), 0)), A, b)['x']
                  for mu in mus]
    ## 计算有效前沿的收益率和风险
    returns = [blas.dot(pbar, x) for x in portfolios]
    risks = [np.sqrt(blas.dot(x, P*x)) for x in portfolios]
    #m1 = np.polyfit(returns, risks, 2)
    #x1 = np.sqrt(m1[2] / m1[0])
    #print(x1)
    x1=0.05
    # 计算最优组合
    opt_weights = solvers.qp(P, q, G, opt.matrix(np.concatenate((-np.ones((1, 1)) * x1, np.zeros((n, 1))), 0)), A, b)['x']
    opt_returns = blas.dot(pbar,opt_weights)
    opt_risks = np.sqrt(blas.dot(opt_weights,P*opt_weights))
    return opt_weights, opt_returns, opt_risks, returns, risks

opt_weights, opt_returns, opt_risks, returns, risks = optimal_portfolio(return_vec)

print(opt_weights)
print(opt_returns)
print(opt_risks)
#print(returns)
#print(risks)

plt.plot(risks, returns, 'y-o')
plt.title('Long-term')
plt.ylabel('returns')
plt.xlabel('risks')
plt.ticklabel_format(useOffset=False,style='plain')
plt.show()