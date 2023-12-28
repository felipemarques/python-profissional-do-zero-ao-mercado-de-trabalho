import os
print(os.getcwd())
os.chdir('..')
print(os.getcwd())

os.chdir('secao7')
print(os.getcwd())

os.chdir('/home/felipe/.ssh')

print(os.getcwd())

print(os.name)