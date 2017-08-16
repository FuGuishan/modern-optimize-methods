#
#取口袋游戏
#A从B的n个口袋里面选择一个口袋。B从选择的口袋里选择一个物品给A
#博弈的利害关系为A想获得最大的利润，B想拥有最小的损失
#博弈论的最大最小剪枝算法同样应用在棋局博弈的双方
def function AlphaBeta(node,depth,alpha,beta,player):
	if node is a terminal node or depth=0:
		return the heuristic value of node
	if player=RED:
		for each child of node:

			alpha:=max(alpha,AlphaBeta(child,depth-1,alpha,beta,not player))
			if alpha>=beta:
				break;
		return alpha
	else:
		for each child of node:
			beta=min(beta,AlphaBeta(child,depth-1,alpha,beta,not player))
			if beta<=alpha:
				break;
		return beta
AlphaBeta(root,MaxDepth,-infinity,+infinity,RED)