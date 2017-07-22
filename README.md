现代优化算法-遗传算法
====
### 仿生学起源
    遗传算法借鉴了生物进化论方法，通过对解的编码形成染色体，仿生染色体的交叉，配对，基因变异，通过模拟自
    然选择的评价选择，通过不断地迭代，选出最优的后代，遗传算法属于启发式寻优算法，最优解并不稳定
### 生物遗传概念对应关系
    -------------------------------------------------------------------------------------------
    生物遗传概念                                               遗传算法中的作用
    -------------------------------------------------------------------------------------------
    适者生存                                     算法停止时，最优解被最大几率
    个体                                         解
    染色体                                       解的编码
    基因                                         解的每一个分量特征
    适应性                                       适应函数值
    群体                                         选定的一组解
    种群                                         根据适应函数值选定的一组解
    交配                                         通过交配原则产生一组新解的过程
    变异                                         编码的某一分量发生变化的过程
    ---------------------------------------------------------------------------------------------
### 算法结果
5个城市数据时暴力求解（最优值）和启发结果对比
![](https://github.com/FuGuishan/modern-optimize-methods/blob/master/genetic_algorithm/raw/5points.png)
10个城市数据时暴力求解（最优值）和启发结果对比
![](https://github.com/FuGuishan/modern-optimize-methods/blob/master/genetic_algorithm/raw/10points.png)
50个城市数据时暴力求解（最优值）无法在短时间内给出解，给出启发结果
![](https://github.com/FuGuishan/modern-optimize-methods/blob/master/genetic_algorithm/raw/50points.png)
