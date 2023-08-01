class Calculator:
    # 여기에 코드를 작성해보세요!
    
    def __init__(self, name, age):
        self.name = name
        self.result=0
        self.age = age
        
    def add(self, num):
        self.result += num
        return self.result
    def sub(self, num):
        self.result -= num
        return self.result
    
    def div(self, num):
        self.result /= num
        return self.result
    def mul(self, num):
        self.result *= num
        

calculator1 = Calculator("Ditto", 10)
calculator2 = Calculator("Sixtail", 32)

print(calculator1.name)
print(calculator2.name)

calculator1.add(3)
calculator1.div(3)
calculator1.add(2)
calculator1.sub(2)
calculator1.mul(10)
    