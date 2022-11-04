class Calculator(object):
    
    def __init__(self):
        self.current = 0;
        
    def add(self, amount):
        self.current += amount;
        
    def subtrack(self, amount):
        self.current -= amount;
        
    def getCurrent(self):
        return self.current;
    
firstCalculator = Calculator();
firstCalculator.add(2);
'''
firstCalculator.add(2);
firstCalculator.subtrack(2);
'''
print(firstCalculator.getCurrent());