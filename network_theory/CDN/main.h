#include <iostream>
using namespace std;

#ifndef MAIN_H_INCLUDED
#define MAIN_H_INCLUDED

typedef struct edge{
int from;
int to;
int weight;
edge(int from,int to,int weight):from(from),to(to),weight(weight){};
}EDGE;
void bellman_ford(char **buff,int len);
int maxFlow(char **buff,int len);
#endif // MAIN_H_INCLUDED
