# Carceral Contagion - Agent-Based Incarceration Model

## Summary

Mass incarceration refers to the substantial increase in incarcerated individuals in the United States over the past four decades, reflective of not only the United States' excessively punitive criminal justice system, but also its perpetuation of oppression along racial lines. Using data collected from the Bureau of Justice Statisitics and survey data, we construct a version of

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

An engrossing book describing the nature of the criminal justice system. 

[The New Jim Crow by Michelle Alexander](http://newjimcrow.com/)