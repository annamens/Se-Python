from abc import ABC, abstractmethod


class demo_absract(ABC):

    @abstractmethod
    def abstract_method(self):
        print('absract class')
        pass
