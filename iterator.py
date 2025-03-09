'''tuple1=("car","bike","van","bus","road","truck","plane")
iter1=iter(tuple1)
for i in tuple1:
    print(next(iter1))
    '''

class MyNumber:

    def __iter__(self):
        self.a=1
        return self
    
    def __next__(self):
        x=self.a
        self.a +=1
        return x
    
myclass=MyNumber()
myiter=iter(myclass)
print(next(myiter))