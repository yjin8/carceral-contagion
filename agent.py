# ..................................................................
# : Carceral Contagion: An Agent-Based Model of Mass Incarceration :
# : Yuchen Jin, Adam Rahman | WHACK 2017                           :
# : carceral-contagion/agent.py                                    :
# :................................................................:

from mesa                import Agent
from random              import random, randrange, randint

def decision(probability):
    ''' Given a probability p, P(True) = p, 
    P(False) = 1-p '''
    return random() < probability

class Person(Agent):
    """ An individual agent in the simulation
    sex -> "M" or "F"

    age_start -> The agent's age at the beginning of the 
        simulation, a value between 18 and 70

    current_age -> The agent's current age, depending on how 
        many months pass in the simulation

    month -> How many months have passed over the course
        of the simulation

    prev_incarcerated -> True or False depending on if
        the agent was formerly imprisoned

    incarcerated -> True or False depending on if the agent
        is imprisoned in the current iteration
    """
    def __init__(self, unique_id, model, incar_prob, sentence_length):
        #super().__init__(unique_id, model)
        self.incar_prob = incar_prob
        self.sentence_length = sentence_length
        self.unique_id = unique_id

        self.func_incar_prob = sentence_length * (incar_prob**2)

        self.prev_incarcerated = False

        self.incarcerated = random() < self.func_incar_prob

        if decision(0.5):
            self.sex = 'M'
        else:
            self.sex = 'F'

        self.year = 0
        self.age_start = randint(18, 70)
        self.current_age = self.age_start

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=False)
        new_position = random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    def isRelated():
        """ We assume that an individual has a 1-in-3 chance
        of being related to someone else in this community"""
        return decision(1/3)

    #Determines probability of incarceration being transmitted
    #from one agent to another
    def transmit(self):
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        #determies number of agents in the same cell

        if len(cellmates) > 1: #if there's more than 1 agent in cell
            other = random.choice(cellmates)

            if self.sex == 'M':
                if other.incarcerated == True and isRelated() and other.sex == 'M':
                    if (self.age - other.age > 10):
                        self.incarcerated = decision(0.006342)
                    if (self.age - other.age < 5):
                        self.incarcerated = decision(0.030173)
                    if (other.age - self.age > 10):
                        self.incarcerated = decision(0.011334)

                elif other.incarcerated == True and isRelated() and other.sex == 'F':
                    if (self.age - other.age > 10):
                        self.incarcerated = decision(0.006342)
                    if (self.age - other.age < 5):
                        self.incarcerated = decision(0.004367)
                    if (other.age - self.age > 10):
                        self.incarcerated = decision(0.003473)
                else:
                    self.incarcerated = decision(0.01)

            if self.sex == 'F':
                if other.incarcerated == True and isRelated() and other.sex == 'M':
                    if (self.age - other.age > 10):
                        self.incarcerated = decision(0.001696)
                    if (self.age - other.age < 5):
                        self.incarcerated = decision(0.033205)
                    if (other.age - self.age > 10):
                        self.incarcerated = decision(0.011288)

                elif other.incarcerated == True and isRelated() and other.sex == 'F':
                    if (self.age - other.age > 10):
                        self.incarcerated = decision(0.00085)
                    if (self.age - other.age < 5):
                        self.incarcerated = decision(0.008012)
                    if (other.age - self.age > 10):
                        self.incarcerated = decision(0.01696)
                else:
                    self.incarcerated = decision(0.01)

       
    def step(self):
        if (self.current_age - self.year) >= self.sentence_length and self.incarcerated == True:
            self.incarcerated = False
            self.prev_incarcerated = True
    
        self.current_age += (1/52)
        self.year += 1/52
        print(self.year)
            
        if self.incarcerated == False:
            self.incarcerated = decision(self.func_incar_prob)
        else:
            pass
