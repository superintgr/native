import os
import time

class Agent:
    def __init__(self, file_path):
        self.file_path = file_path
        self.alias = self.file_path + ".agent"
        self.bytes_processed = 0
        
        self.register()

    def read(self, n):
        with open(self.file_path, 'r') as f:
            chunk = f.read(n)
        self.bytes_processed += n
        return chunk
    
    def register(self):
        with open(self.alias, 'w') as f:
            f.write("Registered on {}".format(time.time()))
            f.write("\n")
            
    def __repr__(self):
        return self.alias

def create_agents(directory):
    agents = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            agents.append(Agent(file_path))
    return agents
    