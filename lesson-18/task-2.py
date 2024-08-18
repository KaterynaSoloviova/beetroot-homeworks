# Task 2
# Implement 2 classes, the first one is the Boss and the second one is the Worker.
# Worker has a property boss, and its value must be an instance of Boss.
# You can reassign this value, but you should check whether the new value is Boss. Each Boss has a list of his own
# workers. You should implement a method that allows you to add workers to a Boss. You're not allowed to add instances
# of Boss class to workers list directly via access to attribute, use getters and setters instead!
# You can refactor the existing code.
# id_ - is just a random unique integer

class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.__workers = []

    def __repr__(self):
        return f'Boss({self.id}, {self.name}, {self.company})'

    def add_worker(self, worker: 'Worker'):
        if not isinstance(worker, Worker):
            raise TypeError('Worker must be of type Worker')
        if worker.company != self.company:
            raise ValueError('Company must be equal to worker')
        self.__workers.append(worker)

    @property
    def workers(self):
        return self.__workers

    @workers.setter
    def workers(self, value: list['Worker']):
        if not isinstance(value, list):
            raise TypeError('Worker must be of type list')
        self.__workers = value

class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = boss
        self._boss.add_worker(self)

    @property
    def boss(self) -> Boss:
        return self._boss

    @boss.setter
    def boss(self, value: Boss) -> None:
        if not isinstance(value, Boss):
            raise TypeError('Boss must be of type Boss')
        self._boss = value
        value.add_worker(self)


a = Boss(1, "Iron Man", "StarkIndustry")
b = Worker(2, "Hulk", "StarkIndustry", a)
c = Boss(3, "Capitan America", "US")
print(b.boss)
b.boss = c
print(b.boss)
a.add_worker(b)
a.workers.append(b)
c.workers.append(b)