# Carceral Contagion - Agent-Based Incarceration Model

## Summary
Mass incarceration refers to the substantial increase in incarcerated individuals in the United States over the past four decades, reflective of not only the United States' excessively punitive criminal justice system, but also its perpetuation of oppression along racial lines. Using data collected from the Bureau of Justice Statisitics and survey data, we construct a model of mass incarceration that attempts to reproduce the racial disparities found in the system. 

We initalize individual agents interacting inside of a model, where contact between agents leads to higher transmission of the likelihood of being sent to prison, depending on the relationship between individuals. For example, when an incarcerated father and non-incarcerated son interact, the latter is more likely to be incarcerated - the presence of a father in prison can result in real psychological harm and lead to the proliferation of risk behaviors. 

The model is simplified, e.g. segregation of black and white simulations, this is done to highlight (a) the extensive racial disparity, which aligns with real world observation and (b) the infectious spread of incarceration, which is exceedingly pronounced in the black simulation. 

## Interaction

The simulation is interactive! You can adjust the sliders to modify the speed of the simulation (i.e. increase the rate of months per second in a range of 2 to 20, cinsluve), population size (range of 100 to 5000, inclusive), sentencing length i.e. how long an individual stays in prison until they are released (a range of 1 to 100, inclusive), and toggling between a simulation of a black population and a white population. When you select a new value, be sure to hit 'reset' to reinitialize the simulation. 

## Background
We have been interested in exploring the nature of the prison industrial complex for some time, and as beginning programmers, we thought it would be a good idea to test our skills by creating simulations of real world phenomena, even with medium or limited knowledge of advanced statistical concepts. We were particularly inspired by books such as _The New Jim Crow_ by Michelle Alexander, which go in-depth into the oppressive nature of the prison-industrial complex and how it reinforces racism and economic destitution. 

We craft this model with the full intention of expanding on it in the future - intersectionality is always key, as well as more precise and larger-in-scope simulations. But we know that even a simple model is sufficient to illustrate the metaphor of the epidemic, and that criminalization of demographics is sustained by biased policy. 

## Installation

To install the dependencies use pip and the requirements.txt in this directory. e.g.

```
    $ pip install -r requirements.txt
```

## How to Run

To run the model interactively, run ``run.py`` in this directory. e.g.

```
    $ python run.py
```

Then open your browser to [http://127.0.0.1:8521/](http://127.0.0.1:8521/) and press Reset, then Run.

## Files

* ``run.py``: Launches a model visualization server.
* ``model.py``: Contains the agent class, and the overall model class.
* ``server.py``: Defines classes for visualizing the model in the browser via Mesa's modular server, and instantiates a visualization server.

## Further Reading

An engrossing book describing the nature of the criminal justice system!:

[The New Jim Crow by Michelle Alexander](http://newjimcrow.com/)
