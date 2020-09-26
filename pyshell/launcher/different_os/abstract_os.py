from abc import ABC, abstractmethod


class AbstractOS(ABC):
    @abstractmethod
    def note(self):
        pass

    @abstractmethod
    def calc(self):
        pass