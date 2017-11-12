# ..................................................................
# : Carceral Contagion: An Agent-Based Model of Mass Incarceration :
# : Yuchen Jin, Adam Rahman | WHACK 2017                           :
# : carceral-contagion/server.py                                   :
# : -- Defines classes for browser model visualization via Mesa's  :
# : modular server, and instantiates a visualization server.       :
# :................................................................:

from model                                   import IncarModel
from description                             import *
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam            import UserSettableParameter
from mesa.visualization.modules              import CanvasGrid, ChartModule

# Adjusts how agents are portrayed in the simulation
# with distinct appearances depending on gender or 
# incarceration status
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

# Generating a 750 x 600 px grid
grid = CanvasGrid(agent_portrayal, 50, 40, 750, 600)

# Slider to adjust population count
n_slider = UserSettableParameter('slider', "Population Count", 1000, 100, 5000, 1)

# Static Text used for model description
static_text1 = UserSettableParameter('static_text', value=description1)
static_text2 = UserSettableParameter('static_text', value=description2)
static_text3 = UserSettableParameter('static_text', value=description3)

# Allows the user to modify the race of the simulated population
race_option = UserSettableParameter('choice', 'Race of Simulated Population', 
                                               value='Black',
                                               choices=['Black', 'White'])

# Independent sliders for black and white sentence lengths
# different ones are required due to distinct default values
bsl_slider = UserSettableParameter('slider', "Max Sentence Length", 17, 1, 100, 1)
wsl_slider = UserSettableParameter('slider', "Max Sentence Length", 14, 1, 100, 1)

# Displays a line chart showing incarceration rate over time
chart = ChartModule([{"Label": "Incarceration Rates",
                      "Color": "Black"}],
                    data_collector_name='datacollector')

# Dictionary of parameters for IncarModel
model_params = {"N": n_slider, "width": 50, "height": 40, 
                "sentence_l": bsl_slider, "race": race_option, 
               "text1": static_text1, "text2": static_text2, "text3": static_text3}

# Call to Mesa's server module which runs our incarceration model
server = ModularServer(IncarModel, [grid, chart], 
                       "Carceral Contagion", model_params)