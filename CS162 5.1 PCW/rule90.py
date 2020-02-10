import numpy as np
import random as rn

class AbstractSimulation:
    def __init__(self, number_steps):
        self.number_steps = number_steps
        self.show_intermediate_steps = True

    def initialize_sim(self):
        pass

    def run_one_step(self):
        raise NotImplementedError

    def print_sim_state(self):
        pass

    def run(self):
        self.initialize_sim()
        for a in range(self.number_steps):
            self.run_one_step()
            if self.show_intermediate_steps:
                self.print_sim_state()
        if not (self.show_intermediate_steps):
            self.print_sim_state()


class rule_90(AbstractSimulation):
    def __init__(self, number_steps):
        super().__init__(number_steps)
    
    def initialize_sim(self):
        self.state = [rn.choice([0,1]) for _ in range (20)]
        self.length = len(self.state)
        self.time = 0

    def run_one_step(self):
        self.time += 1
        new_state = [0]*self.length
        for i in range(self.length):
            if self.state[(i-1)%self.length] != self.state[(i+1)%self.length]:
                new_state[i] = 1
        self.state = new_state
        
    def print_sim_state(self):
        print("At time {} the state is {}".format(self.time, self.state))

sim = rule_90(9)
sim.run()