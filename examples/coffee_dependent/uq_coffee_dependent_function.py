import uncertainpy as un
import chaospy as cp
import numpy as np
from scipy.integrate import odeint


def coffee_cup_dependent(kappa_hat, T_env, alpha):
    # Initial temperature and time
    time = np.linspace(0, 200, 150)
    T_0 = 95

    # The equation describing the model
    def f(T, time, alpha, kappa_hat, T_env):
        return -alpha*kappa_hat*(T - T_env)

    # Solving the equation by integration.
    values = odeint(f, T_0, time, args=(alpha, kappa_hat, T_env))[:, 0]

    # Return time and model results
    return time, values


# Create the distributions
T_env_dist = cp.Uniform(15, 25)
alpha_dist = cp.Uniform(0.5, 1.5)
kappa_hat_dist = cp.Uniform(0.025, 0.075)/alpha_dist

# Define a parameter list and use it to create the parameters
parameter_list = [["alpha", alpha_dist],
                  ["kappa_hat", kappa_hat_dist],
                  ["T_env", T_env_dist]]
parameters = un.Parameters(parameter_list)

# Create a model from coffee_cup function and add labels
model = un.Model(coffee_cup_dependent,
                 labels=["Time (s)", "Temperature (C)"])


# Perform the uncertainty quantification using the Rosenblatt transformation
UQ = un.UncertaintyQuantification(model=model,
                                  parameters=parameters)

UQ.quantify(rosenblatt=True,
            figure_folder="figures_coffee_dependent",
            filename="coffee_cup_dependent")
