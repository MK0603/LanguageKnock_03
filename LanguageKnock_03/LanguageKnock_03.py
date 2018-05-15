'''
Created on 2018/05/15

'''
target="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
targetRepl_1=target.replace(',', '')
targetRepl_2=targetRepl_1.replace('.', '')
targetArray=targetRepl_2.split(" ")


for i in range(len(targetArray)):
    print(len(targetArray[i]),end='')