# ..................................................................
# : Carceral Contagion: An Agent-Based Model of Mass Incarceration :
# : Yuchen Jin, Adam Rahman | WHACK 2017                           :
# : carceral-contagion/model.py                                    :
# :................................................................:

from mesa                import Model
from agent               import Person
from mesa.space          import MultiGrid
from mesa.time           import RandomActivation
from mesa.datacollection import DataCollector
from random              import random, randrange, randint

def compute_incar_rates(model):
    agent_incarcerated = [agent.incarcerated for agent in model.schedule.agents]
    num_incarcerated = 0
    N = model.num_agents
    for incar in agent_incarcerated:
        if incar == True: 
            num_incarcerated += 1
    return num_incarcerated/N


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
           model_reporters = {"Incidence": compute_incar_rates},
           agent_reporters = {"Incarcerated:": lambda a : a.incarcerated})
    
    def step(self):
        self.schedule.step()
        self.datacollector.collect(self)