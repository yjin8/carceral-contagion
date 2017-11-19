# ..................................................................
# : Carceral Contagion: An Agent-Based Model of Mass Incarceration :
# : Yuchen Jin, Adam Rahman | WHACK 2017                           :
# : carceral-contagion/model.py                                    :
# : -- Contains the agent class "Person, and the overall model     :
# : class "IncarModel", along with their respective methods        :
# :................................................................:

from mesa                import Model, Agent
from mesa.space          import MultiGrid
from mesa.time           import RandomActivation
from mesa.datacollection import DataCollector
from random              import random, randrange, randint


def compute_incar_rates(model):
    agents_incar = [agent.incarcerated for agent in model.schedule.agents]
    num_incarcerated = 0
    N = model.num_agents
    for incar in agents_incar:
        if incar == True: 
            num_incarcerated += 1
    return num_incarcerated/N


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
        self.incar_prob = incar_prob
        self.sentence_length = sentence_length
        self.unique_id = unique_id

        self.func_incar_prob = sentence_length * (incar_prob**2)

        self.prev_incarcerated = False

        self.incarcerated = decision(self.func_incar_prob)

        if decision(0.5):
            self.sex = 'M'
        else:
            self.sex = 'F'

        self.year = 0
        self.age_start = randint(18, 70)
        self.current_age = self.age_start

    def move(self):
        """Agent changes position in grid"""
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=False)
        new_position = random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    def isRelated():
        """We assume that an individual has a 1-in-3 chance
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
                    pass

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
                    pass

       
    def step(self):
        if (self.current_age - self.year) >= randint(5,self.sentence_length) and self.incarcerated == True:
            self.incarcerated = False
            self.prev_incarcerated = True
    
        self.current_age += (1/52)
        self.year += 1/52
            
        if self.incarcerated == False:
            self.incarcerated = random() < self.func_incar_prob
        else:
            pass


class IncarModel(Model):
    """ 
    An agent-based epidemiological model of mass incarceration and     
    its resultant racial disparities in the United States,             
    programmed in Python 3.6 using Mesa by Yuchen Jin and Adam Rahman. 

    We instantiate separate classes of agents and models and allow 
    the simulation to step through units of months, with agents moving
    in between cells in a grid and interacting with one another. People
    'transmit' the likeliness of being incarcerated through risk behaviors
    and psychological conditioning, hence spreading the risk of being imprisoned.
    """
    def __init__(self, N, width, height, sentence_l, race, text1="", text2="", text3=""):
        self.running = True
        self.num_agents = N
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)
        self.race = race
        self.num_incarcerated = 0

        # Create agents
        for i in range(self.num_agents):
            if self.race == 'Black':
                self.sentence_l = 17
                a = Person(i, self, 0.03023, self.sentence_l)
            else:
                self.sentence_l = 14
                a = Person(i, self, 0.00478, self.sentence_l)
            self.schedule.add(a)
            # Add the agent to a random grid cell
            x = randrange(self.grid.width)
            y = randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))

        self.datacollector = DataCollector(
           model_reporters = {"Incarceration Rates": compute_incar_rates},
           agent_reporters = {"Incarcerated:": lambda a : a.incarcerated})

    def step(self):
        self.schedule.step()
        self.datacollector.collect(self)

def decision(probability):
    ''' Given a probability p, P(True) = p, 
    P(False) = 1-p '''
    return random() < probability