def getGrid(x,y,n,m):
    ret=[];
    for s in range(3):
        for e in range(3):
            curX,curY=x-s,y-e;
            if(curX>=1 and curX<=n and curY>=1 and curY<=m):
                ret.append((curX,curY));
    return ret;
def clearMush(gridAndMushes,mushAndGrids,times):
    if(times==0):
        return 0;
     
    gridAndMushes_sorted=sorted(gridAndMushes.items(),key=lambda x:len(set(x[1])));
    mostGrid=gridAndMushes_sorted[-1][0];
    clearedMushes=list(set(gridAndMushes[mostGrid]));
    for mush in clearedMushes:
        for grid in mushAndGrids[mush]:
            #if(mush in gridAndMushes[grid]):
            gridAndMushes[grid].remove(mush);
    return len(clearedMushes)+clearMush(gridAndMushes,mushAndGrids,times-1);
def main():
    while(True):
        try:
            n,m,k=map(int,raw_input().strip().split());
            gridAndMushes={};
            mushAndGrids={};
            for i in range(k):
                mush_i=tuple(map(int,raw_input().strip().split()));
                    #mushes[(mush_i)]=mushes.get(mush_i,[])+getGrid(mush_i[0],mush_i[1],n,m);
                if(mush_i in mushAndGrids):
                    grids_i=mushAndGrids[mush_i];
                else:
                    grids_i=getGrid(mush_i[0],mush_i[1],n,m);
                    mushAndGrids[mush_i]=grids_i;
                for grid in grids_i:
                    gridAndMushes[grid]=gridAndMushes.get(grid,[])+[mush_i];
            ret=clearMush(gridAndMushes,mushAndGrids,2);
            print ret;
        except:
            break;
 
main();