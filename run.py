# ..................................................................
# : Carceral Contagion: An Agent-Based Model of Mass Incarceration :
# : Yuchen Jin, Adam Rahman | WHACK 2017                           :
# : carceral-contagion/run.py                                      :
# : -- Launches a model visualization server.                      :
# :................................................................:

import os
from server import server
server.port(int.os.environ.get("PORT",5000))
server.Launch()