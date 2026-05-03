from abc import ABC, abstractmethod

class Tab(ABC):
    @abstractmethod
    def render(self):pass