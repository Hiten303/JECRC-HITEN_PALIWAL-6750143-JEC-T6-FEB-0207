

class MyDt:
    def __init__(self,val):
        self.val=val
    
    def __str__(self):
        return str(self.val)

    def __add__(self,*ano_obj):
        sum=self.val
        for i in ano_obj:
            sum+=i.val
        return MyDt(sum)

    
    
    def __sub__(self,*ano_obj):
        sum=self.val
        for i in ano_obj:
            sum-=i.val
        return MyDt(sum)
        
    
    def __mul__(self,*ano_obj):
        sum=self.val
        for i in ano_obj:
            sum*=i.val
        return MyDt(sum)
    
    def __floordiv__(self,*ano_obj):
        sum=self.val
        for i in ano_obj:
            sum//=i.val
        return MyDt(sum)
    
    def __truediv__(self,*ano_obj):
        sum=self.val
        for i in ano_obj:
            sum/=i.val
        return MyDt(sum)
    
    def __mod__(self,*ano_obj):
        sum=self.val
        for i in ano_obj:
            sum%=i.val
        return MyDt(sum)
    
print(MyDt(10.10)+MyDt(20))
print(MyDt(100)-MyDt(34))
print(MyDt(4)*MyDt(20))
print(MyDt(100)+MyDt(200)+MyDt(300)+MyDt(400))