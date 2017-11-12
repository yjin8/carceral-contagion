# Carceral Contagion - Agent-Based Incarceration Model

## What's Up?
People just don't get how extensive and entrenched racism truly is - and the fact that we're sending so many people to prison for the _smallest_ of crimes is a huge contributor. Lives and communities are devastated due to bias and excessive punishment, and with public support of tough-on-crime laws, it's hard to convince people how racist the criminal justice system is. 

Through our model, we hope to disrupt people's understanding of how the criminal justice system operates. Imprisonment doesn't just contain people - it makes them contagious. Former convicts are impacted by the stresses of incarceration, making them more likely to go back to prison or ruin their family lives and less likely to earn a living income. With so many people interacting in a community, this makes the chance of incarceration exponentially higher.

We want to expand upon this model to inform not just people, but public policy. We want to translate data to design, and demonstrate decades of oppression in a single screen so that the average person can digest it and be motivated to resist. Even with our simplified model, we have accurate recreations of incarceration disparities in the U.S., which should be sufficient to convince people that this is a public health crisis, one worth fighting for. 

## Summary
Mass incarceration refers to the substantial increase in incarcerated individuals in the United States over the past four decades, reflective of not only the United States' excessively punitive criminal justice system, but also its perpetuation of oppression along racial lines. Using data collected from the Bureau of Justice Statisitics and survey data, we construct a model of mass incarceration that attempts to reproduce the racial disparities found in the system. 

We initalize individual agents interacting inside of a model, where contact between agents leads to higher transmission of the likelihood of being sent to prison, depending on the relationship between individuals. For example, when an incarcerated father and non-incarcerated son interact, the latter is more likely to be incarcerated - the presence of a father in prison can result in real psychological harm and lead to the proliferation of risk behaviors. 

The model is simplified, e.g. segregation of black and white simulations, this is done to highlight (a) the extensive racial disparity, which aligns with real world observation and (b) the infectious spread of incarceration, which is exceedingly pronounced in the black simulation. 

We implemented this simulation using the Mesa library for agent-based modelling in Python, and extended it to construct an epidemiological model.

## Interaction

The simulation is interactive! You can adjust the sliders to modify the speed of the simulation (i.e. increase the rate of months per second in a range of 2 to 20, incsluve), population size (range of 100 to 5000, inclusive), sentencing length i.e. how long an individual stays in prison until they are released (a range of 1 to 100, inclusive), and toggling between a simulation of a black population and a white population. When you select a new value, be sure to hit 'reset' to reinitialize the simulation. 

'Grey' nodes represent individuals who have not yet interacted with incarcerated individuals and have not been incarcerated, 'blue' nodes represent people who are in prison (and cannot move around the grid), 'red' nodes represent people who are out of prison - thus previously incarcerated - or have previously interacted with incarcerated individuals and/or have engaged in criminal behavior, and are thus contagious. Each agent has a gender ("M" or "F" indicated on the node), an age, a likelihood of being incarcerated, and a random position on the grid. An agent has a likelihood of being related to someone else, and the probability calculations are performed when agents overlap on a cell. 

## Background
We have been interested in exploring the nature of the prison industrial complex for some time, with both of us having Theater backgrounds, we have engaged in ways of combating mass incarceration through communicating the stories of people and communities impacted by it. As beginning programmers, we thought it would be a good idea to test our skills by creating simulations of real world phenomena, even with medium or limited knowledge of advanced statistical concepts. We were particularly inspired by books such as _The New Jim Crow_ by Michelle Alexander, which go in-depth into the oppressive nature of the prison-industrial complex and how it reinforces racism and economic destitution. 

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

## Sources
[Mitchell, Ojmarrh. "A meta-analysis of race and sentencing research: Explaining the
inconsistencies." Journal of Quantitative Criminology 21.4 (2005): 439-466] (https://www.jstor.org/stable/23367476)

[Dallaire, Danielle H. "Incarcerated mothers and fathers: A comparison of risks for children
and families." Family relations 56.5 (2007): 440-453.](http://onlinelibrary.wiley.com/doi/10.1111/j.1741-3729.2007.00472.x/abstract)

## Further Reading

For a holistic perspective on the nature of the prison industrial complex:

[Alexander, Michelle. The New Jim Crow: Mass Incarceration in the Age of Colorblindness. The
New Press, 2012.](http://newjimcrow.com/)
