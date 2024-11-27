class Math_Operations:

    def isitnum(self,a,b):
        if (
            not isinstance(a,(int,float)) or 
            not isinstance(a,(int,float)) or 
            isinstance(a,bool) or 
            isinstance(b,bool)
            ):
            raise ValueError("Both arguments must be int or float")
    
    def divbyzero(self,a,b):
        if b == 0:
            raise ZeroDivisionError("Divisor cannot be zero")

    def add(self,a,b):
        self.isitnum(a,b)
        return a+b
        
    def sub(self,a,b):
        self.isitnum(a,b)
        return a-b

    def mul(self,a,b):
        self.isitnum(a,b)
        return a*b

    def div(self, a, b):
        self.divbyzero(a, b)
        self.isitnum(a, b)
        return a/b