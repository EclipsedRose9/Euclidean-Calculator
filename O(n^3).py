GraphPoints = [[5,4],[6,10],[2,2],[1,1]]

def PointDistence(GraphPoints):
    GridSize = max(max(GraphPoints, key=max))*2
    for b in range(GridSize):
        for i in range(len(GraphPoints)):
            for l in range(len(GraphPoints)):
                x = GraphPoints[i][0] - GraphPoints[l][0]
                y = GraphPoints[i][1] - GraphPoints[l][1]
                Distence = (abs(x)+abs(y))
                if GridSize == Distence:
                    print(GraphPoints[i][0], GraphPoints[i][1])
                    print(GraphPoints[l][0], GraphPoints[l][1])
                    input()
        GridSize = GridSize - 1
         
PointDistence(GraphPoints)
