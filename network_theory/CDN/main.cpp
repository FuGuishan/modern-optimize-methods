#include <iostream>
#include <vector>
#include "file.h"
#include "main.h"
#include<stdlib.h>
#include<stdio.h>
#include <string.h>
#define MAX_NODE 200
using namespace std;

int main()
{
    char *buff[100];
    int lineNum=0;
    const char* filename="test.txt";
    lineNum=read_file(buff,filename);
    int flow=maxFlow(buff,lineNum);
    cout<<flow<<endl;
  //  bellman_ford(buff,lineNum);
}

char * charToNum(char * str, int& target)
{
	int sum = 0;
	bool minus=false;
	while(((*str) != 32) && ((*str) != 13) && ((*str) !=0)&& ((*str) !='\n'))
	{
	    if(*str=='-')
            {
                str++;
                 minus=true;
                continue;

            }


		sum = sum * 10 + ((*str) - '0');
		str++;
	}
	target = minus?-sum:sum;
	return ++str;
}
/*
带负路径的单元最短路算法
*/
void bellman_ford(char **buff,int len)
{
 char *index=NULL;
 vector<EDGE> edges;
 int nodeNums   ;
 int from;
 int to;
 int weight;
 index=charToNum(buff[0],nodeNums);
 for (int i=1;i<len;i++)
 {
     index=charToNum(buff[i],from);
     index=charToNum(index,to);
     index=charToNum(index,weight);
     edges.push_back(EDGE(from,to,weight));
 }
 int dis[nodeNums];
  for(vector<EDGE>::iterator it=edges.begin();it!=edges.end();it++)
     cout<<(*it).from<<" "<<(*it).to<<" "<<(*it).weight<<endl;

 //int pre[nodeNums];
 for (int i=0;i<nodeNums;i++)
 {
     if(i==0)
        dis[i]=0;
    else
        dis[i]=0x7ffffff;
 }
 for (int i=0;i<nodeNums;i++)
 {
     for(int j=0;j<len-1;j++)
     {

         if(dis[edges[j].to]>dis[edges[j].from]+edges[j].weight)
         {
             dis[edges[j].to]=dis[edges[j].from]+edges[j].weight;
          //   pre[edges[j].to]=edges[j].from;
         }
     }


 }
          for(int j=0;j<len-1;j++)
     {

         if(dis[edges[j].to]>dis[edges[j].from]+edges[j].weight)
         {
             printf("error!");
             return;
         }
     }
 for(int i=0;i<nodeNums;i++)
    cout<<dis[i]<<endl;

 cout<<nodeNums<<endl;

}
int dfs(bool *used,int from,int des,vector<EDGE> &edges,vector<int> *nodes,int flow){
    if(from==des)

        return flow;
    used[from]=true;
    for(unsigned int i=0;i<nodes[from].size();i++)
    {
        //int nodeId=nodes[from][i];
        EDGE ed=edges[nodes[from][i]];
        int id=ed.to;
        if(used[id]==false && ed.weight>0)
        {
            int d=dfs(used,id,des,edges,nodes,min(flow,ed.weight));
            edges[nodes[from][i]].weight-=d;
            edges[nodes[from][i]^1].weight+=d;
            return d;
        }

    }
    return -1;
}
int maxFlow(char **buff,int len)
{
 char *index=NULL;
 vector<EDGE> edges;
 vector<int> nodes[MAX_NODE];

 int nodeNums;
 int from;
// int j=0;
 int to;
 int weight;
 index=charToNum(buff[0],nodeNums);

 for (int i=1;i<len;i++)
 {
     index=charToNum(buff[i],from);
     index=charToNum(index,to);
     index=charToNum(index,weight);
     edges.push_back(EDGE(from,to,weight));
     edges.push_back(EDGE(to,from,0));
     int m=edges.size();
     nodes[to].push_back(m-1);
     nodes[from].push_back(m-2);
 }
 int flow=0;
 while(true)
 {
   bool used[nodeNums];
   memset(used,false,sizeof(used));
  // used[0]=true;
   int f=dfs(used,0,nodeNums-1,edges,nodes,0x7fffffff);
   if(f<=0)
    return flow;
   flow+=f;
 }
 return flow;

}

