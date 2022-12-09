#class
class Point:

    def __init__(self,x,y):
        #cod-> coordinate
        self.x_cod=x
        self.y_cod=y
    
    def __str__(self) -> str:
        return f"<{self.x_cod},{self.y_cod}>"
    
    def euclidean_distance(self,other):
        # Distance ((x2-x1)^2 +(y2-y1)^2)^1/5
        return ((self.x_cod-other.x_cod)**2 + (self.y_cod-other.y_cod)**2)**0.5
    
    def distance_from_origin(self):
        return self.euclidean_distance(Point(0,0))
        
class Line:
    def __init__(self,A,B,C) -> None:
        self.A=A
        self.B=B
        self.C=C
        
    def __str__(self) -> str:
        if self.A<0 and self.B<0 and self.C<0:
            return f"-{self.A}x-{self.B}y-{self.C}=0"
        elif self.A<0 and self.B<0:
            return f"{self.A}x{self.B}y+{self.C}=0"
        elif self.B<0 and self.C<0:
            return f"{self.A}x{self.B}y{self.C}=0"
        elif self.A<0 and self.C<0:
            return f"{self.A}x+{self.B}y{self.C}=0"
        elif self.B<0:
            return f"{self.A}x{self.B}y+{self.C}=0"
        elif self.C<0:
            return f"{self.A}x+{self.B}y{self.C}=0"
        else: 
            return f"{self.A}x+{self.B}y+{self.C}=0"
    
    def point_on_line(line,point):
        if line.A*point.x_cod+line.B*point.y_cod+line.C==0:
            return "lies on the line"
        else:
            return "does not lie on the line"
    
    def shortest_distance(line,point):
        return abs(line.A*point.x_cod+line.B*point.y_cod+line.C)/(line.A**2+line.B**2)**0.5



# p1=Point(0,0)
# p2=Point(1,1)
# print(p1)
# print(p2)
# print(p1.euclidean_distance(p2))

l1=Line(1,1,-2)
p1=Point(1,1)
print(l1)
print(p1)

print(l1.point_on_line(p1))
print(l1.shortest_distance(p1))