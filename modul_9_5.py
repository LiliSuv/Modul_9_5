class StepValueError(ValueError):
    def __init__(self, message):
        self.message = message
        print (self.message)

class Iterator:
    def __init__(self,start,stop,step=1):
        self.start=start
        self.stop= stop
        self.step=step
        if step ==0:
            StepValueError (f'ValueError:"Шаг  не может быть равен 0"')
        if start>=stop and step>0 or start<=stop and step<0:
            StepValueError (f'ValueError:"Ошибка ввода данных"')
    def __iter__ (self):
        self.pointer=self.start
        return  self
    def __next__(self):
        if self.step <= 0 and self.pointer > self.stop or self.step > 0 and self.pointer < self.stop:
            self.pointer += self.step
        else:
            raise StopIteration()
        return self.pointer-self.step

iter1 = Iterator(4, 6, 0)
iter2 = Iterator(5, 1)
iter3 = Iterator(-5,3,-2)
iter4 = Iterator(-5, 1,)
iter5 = Iterator(6, 15, 2)
iter6 = Iterator(10, 1, -1)
iter7 = Iterator(1, -14, -3)

for i in iter1:
    print(i, end=' ')
print()
for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()
for i in iter6:
    print(i, end=' ')
print()
for i in iter7:
    print(i, end=' ')






