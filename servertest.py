# ..................................................................
# : Carceral Contagion: An Agent-Based Model of Mass Incarceration :
# : Yuchen Jin, Adam Rahman | WHACK 2017                           :
# : carceral-contagion/server.py                                   :
# :................................................................:

from model                                   import IncarModel
from description                             import *
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules              import CanvasGrid
from mesa.visualization.modules              import ChartModule
from mesa.visualization.UserParam            import UserSettableParameter

def agent_portrayal(agent):
    portrayal = {"Shape": "circle", "r": 1, "Filled": "false","Color": "grey",
                 "Layer": 0, "text": 'A', "text_color":"white"}

    if agent.sex == 'M':
      portrayal["text"] = 'M'
      # portrayal["heading_x"] = agent.pos[0]
      # portrayal["heading_y"] = agent.pos[1]
    else:
      portrayal["text"] = 'F'
      # portrayal["heading_x"] = agent.pos[0]
      # portrayal["heading_y"] = agent.pos[1]

    if agent.incarcerated == True:
        portrayal["Color"] = "blue"
        portrayal["Layer"] = 0
        #portrayal["r"] = 0.3
    else:
        if agent.prev_incarcerated == True:
          portrayal["Layer"] = 0
          #portrayal["r"] = 0.2
          portrayal["Color"] = "red"

    return portrayal

grid = CanvasGrid(agent_portrayal, 50, 40, 750, 600)

n_slider = UserSettableParameter('slider', "Population Cout", 1000, 100, 5000, 1)

static_text1 = UserSettableParameter('static_text', value=description1)
static_text2 = UserSettableParameter('static_text', value=description2)
static_text3 = UserSettableParameter('static_text', value=description3)

race_option = UserSettableParameter('choice', 'Race of Simulated Population', 
                                               value='Black',
                                               choices=['Black', 'White'])
bsl_slider = UserSettableParameter('slider', "Sentence Length (Months)", 17, 1, 100, 1)
wsl_slider = UserSettableParameter('slider', "Sentence Length (Months)", 14, 1, 100, 1)

chart = ChartModule([{"Label": "Incidence",
                      "Color": "Black"}],
                    data_collector_name='datacollector')

server = ModularServer(IncarModel, [grid, chart], "Carceral Contagion",
                       {"N": n_slider, "width": 50, "height": 40, 
                       "sentence_l": bsl_slider, "race": race_option, 
                       "text1": static_text1, "text2": static_text2, "text3": static_text3})