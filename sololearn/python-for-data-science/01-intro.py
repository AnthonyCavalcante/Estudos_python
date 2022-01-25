import numpy as np
from numpy.core.fromnumeric import mean
class statistic:
    def __init__(self):
        self
    
    def mean(self, value):
        self.value = value
        return  sum(self.value)/len(self.value)

def extra_intro1():
    #find median
    median = [24, 28, 22, 27, 29, 26, 25, 21, 23,30,15]
    median.sort()
    print(median)
    calculate_median =int(len(median))
    if (calculate_median%2) == 0:
        x = int((calculate_median/2))
        print((median[x-1]+median[x])/2)
    else:
        x = int((calculate_median/2)-0.5)
        print(median[x])

def extra_intro2():
    #calculate variance and standard Deviation
    #question = verificar quais idades estão dentro de um desvio padrão
    cal = statistic()
    popul= [14, 18, 19, 24, 26, 33, 42, 55, 67]
    print(popul)
    print('mean= {:.1f}'.format(cal.mean(popul)))
    
    variance_popul = [(x-cal.mean(popul))**2 for x in popul]
    print ('variance= {:.1f}'.format(cal.mean(variance_popul)))
   
    std_deviation = cal.mean(variance_popul)**0.5
    print ('std_deviation= {:.1f}'.format(std_deviation))

    age_std = [age for age in popul 
                if age > (cal.mean(popul)-std_deviation) and age < (cal.mean(popul)+std_deviation)]
    print (age_std)
    print('=============')

def extra_intronp():
    popul= [14, 18, 19, 24, 26, 33, 42, 55, 67]
    new_popul = np.array(popul)
    print(new_popul)
    print('mean = {:.1f}'.format(np.mean(new_popul)))
    print('variance = {:.1f}'.format(np.var(new_popul)))
    print ('std = {:.1f}'.format(np.std(new_popul)))
    mean = np.mean(new_popul)
    std = np.std(new_popul)
    age_std = [age for age in new_popul if age > (mean-std) and age < (mean+std)] 
    print(new_popul[new_popul>(mean-std) & new_popul<(mean+std)])

def exercise1():
    vac_nums = [0,0,0,0,0,
            1,1,1,1,1,1,1,1,
            2,2,2,2,
            3,3,3
            ]
    vac_mean = sum(vac_nums)/len(vac_nums)
    print(vac_mean)

def exercise2():
    vac_nums = [0,0,0,0,0,
            1,1,1,1,1,1,1,1,
            2,2,2,2,
            3,3,3
            ]
    vac_mean = sum(vac_nums)/len(vac_nums)
    var_num = [(x - vac_mean)**2 for x in vac_nums]
    variance = sum(var_num) / len(var_num)
    print(var_num)
    print(vac_nums)
    print(sum(var_num), len(var_num))
    
def basket_players():
    players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]
    players.sort()
    p = statistic()

    var_p = [(i - p.mean(players))**2 for i in players]
    std = (p.mean(var_p))**0.5
    std_p = [i for i in players if i > (p.mean(players)- std) and i < (p.mean(players)+ std)]
    print(len(std_p))
   
    

def main():
  extra_intro2()
  extra_intronp()
if __name__ == '__main__':
    main()
    