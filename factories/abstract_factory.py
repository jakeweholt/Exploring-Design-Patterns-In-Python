from abc import ABC, abstractmethod


class AbstractFactory(ABC):
 
    def __init__(self, name):
        self.name = name
        super().__init__()
    
    @abstractmethod
    def method_1(self):
        pass
    
    @abstractmethod
    def method_2(self):
        pass


class Factory_1(AbstractFactory):
    def method_1(self):
        return('factory_1_method_1')
    
    def method_2(self):
        return('factory_1_method_2')
    
    
class Factory_2(AbstractFactory):
    def method_1(self):
        return('factory_2_method_1')
    
    def method_2(self):
        return('factory_2_method_2')
    
    
class EntryPoint:
    def __init__(self, factory):
        self.name = factory.name
        self.method_1 = factory.method_1
        self.method_2 = factory.method_2