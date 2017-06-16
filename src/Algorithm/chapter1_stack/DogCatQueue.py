# coding:_utf8
from collections import deque
class Pet(object):
    def __init__(self,type):
        self.type = type

    def getPetType(self):
        return self.type

class Dog(Pet):
    def __init__(self):
        super(Dog,self).__init__('dog')

class Cat(Pet):
    def __init__(self):
        super(Cat, self).__init__('cat')

##########################
class PetEnterQueue(object):
    def __init__(self,pet,count):
        self.pet = pet
        self.count = count
    def getPet(self):
        return self.pet
    def getCount(self):
        return self.count
    def getEnterPetType(self):
        return self.pet.getPetType()

############################
class DogCatQueue():
    def __init__(self):
        self.dogQ = deque()
        self.catQ = deque()
        self.count = 0
    def add(self,pet):
        if pet.getPetType() is 'dog':
            self.dogQ.append(PetEnterQueue(pet,self.count))
            self.count += 1
        elif pet.getPetType() is 'cat':
            self.catQ.append(PetEnterQueue(pet,self.count))
            self.count += 1
        else:
            raise "err, not dog or cat"

    def pollAll(self):
        if len(self.dogQ)>0 and len(self.catQ)>0:
            if self.dogQ[0].getCount() < self.catQ[0].getCount():
                return self.dogQ.popleft().getPet()
            else:
                return self.catQ.popleft().getPet()
        elif len(self.dogQ) > 0:
            return self.dogQ.popleft().getPet()
        elif len(self.catQ) > 0:
            return self.catQ.popleft().getPet()
        else:
            raise "err, queue is empty"

    def pollDog(self):
        if len(self.dogQ) > 0:
            return self.dogQ.popleft().getPet()
        else:
            raise "Dog queue is empty!"

    def pollCat(self):
        if len(self.catQ) > 0:
            return self.catQ.popleft().getPet()
        else:
            raise "Cat queue is empty!"

    def isEmpty(self):
        return len(self.dogQ) == 0 and len(self.catQ) == 0

    def isDogQueueEmpty(self):
        if len(self.dogQ) == 0:
            return True
        else:
            return False

    def isCatQueueEmpty(self):
        if len(self.dogQ) == 0:
            return True
        else:
            return False














