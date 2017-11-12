# ..................................................................
# : Carceral Contagion: An Agent-Based Model of Mass Incarceration :
# : Yuchen Jin, Adam Rahman | WHACK 2017                           :
# : carceral-contagion/run.py                                      :
# : -- Launches a model visualization server.                      :
# :................................................................:

from servertest import server
server.port = 8521
server.launch()