from time import time
from typing import Any, NoReturn

class Randoms():
    '''класс рандома написан статично для выявления багов,
       пускай останется в проде'''
    def __init__(self,seed:float=None) -> NoReturn:
        if not seed:
            self.seed=int(time()%32768)
        else:
            self.seed=int(seed%32768)
        self.count=0
        self.rseed=self.seed
#    def __del__(self) -> NoReturn:
#        print(f"{self.__class__.__name__} уничтожен")
    def setSeed(self,seed:float=0) -> str:
        self.seed=int(seed%32768)
        self.count=0
        self.rseed=self.seed
        return f"Seed Was Set To {self.seed}"
    def getSeed(self) -> str:
        return f"[{self.rseed}] Seed Is {self.seed}, Count: {self.count}"
    def getRandom(self,min:int=0,max:int=1) -> int:
        self.rseed=((8253729*self.rseed+2396403 )%32768)
        self.count+=1
        return int(self.rseed%(max-min+1)+min)
    def getChoice(self,list) -> Any:
        return list[self.getRandom(max=len(list)-1)]