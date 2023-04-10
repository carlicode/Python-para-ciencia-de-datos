import pandas as pd

df = pd.read_csv('temperaturas.csv', delimiter=';')

print('Min:', df['temperatura'].min())
print('Ma:', df['temperatura'].max())
print('Mean:',df['temperatura'].mean())
print('Std:', df['temperatura'].std())
print('Var:', df['temperatura'].var())

