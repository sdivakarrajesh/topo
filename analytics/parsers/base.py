from abc import ABC, abstractmethod

class FileParser(ABC):
    def __init__(self, file_path):
        self.file_path = file_path
        self.parsed_data = []
        
    @abstractmethod
    def parse(self):
        pass
    
    @abstractmethod
    def load_db(self):
        pass
    
    @abstractmethod
    def run(self):
        self.parse()
        self.load_db()
    
    