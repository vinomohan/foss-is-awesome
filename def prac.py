def solve(a,b,c,d,e,f):
    x=((d*e-b*f)/(a*d-b*c))
    y=((a*f-c*e)/(a*d-b*c))
    return[x,y]
xsol,ysol=solve(2,3,1,4,2,5)
print('the solution is x=',xsol,'and',ysol)
