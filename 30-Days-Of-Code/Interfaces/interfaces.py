'''
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''
class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        summer = 0
        for i in range(1,n+1):
            if n%i==0:
                summer += i
        return summer
