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
### 主要算法
轮盘赌算法伪代码：
```c
轮盘赌算法

/*
* 按设定的概率，随机选中一个个体
* P[i]表示第i个个体被选中的概率
*/
int RWS()
{
m =0;
r =Random(0,1); //r为0至1的随机数
for(i=1;i<=N; i++)
{
/* 产生的随机数在m~m+P[i]间则认为选中了i
* 因此i被选中的概率是P[i]
*/
m = m + P[i];
if(r<=m) return i;
}
}
```
主体代码：
```c
基本遗传算法伪代码

/*
* Pc：交叉发生的概率
* Pm：变异发生的概率
* M：种群规模
* G：终止进化的代数
* Tf：进化产生的任何一个个体的适应度函数超过Tf，则可以终止进化过程
*/
初始化Pm，Pc，M，G，Tf等参数。随机产生第一代种群Pop

do
{ 
　　计算种群Pop中每一个体的适应度F(i)。
　　初始化空种群newPop
　　do
　　{
　　　　根据适应度以比例选择算法从种群Pop中选出2个个体
　　　　if ( random ( 0 , 1 ) < Pc )
　　　　{
　　　　　　对2个个体按交叉概率Pc执行交叉操作
　　　　}
　　　　if ( random ( 0 , 1 ) < Pm )
　　　　{
　　　　　　对2个个体按变异概率Pm执行变异操作
　　　　}
将2个新个体加入种群newPop中
} until ( M个子代被创建 )
用newPop取代Pop
}until ( 任何染色体得分超过Tf， 或繁殖代数超过G )
```
### 算法结果TSP问题
5个城市数据时暴力求解（最优值）和启发结果对比
![](https://github.com/FuGuishan/modern-optimize-methods/blob/master/genetic_algorithm/raw/5points.png)
10个城市数据时暴力求解（最优值）和启发结果对比
![](https://github.com/FuGuishan/modern-optimize-methods/blob/master/genetic_algorithm/raw/10points.png)
50个城市数据时暴力求解（最优值）无法在短时间内给出解，给出启发结果
![](https://github.com/FuGuishan/modern-optimize-methods/blob/master/genetic_algorithm/raw/50points.png)
