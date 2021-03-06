from uncertainpy.core import UncertaintyCalculations
from uncertainpy.core import UncertaintyCalculations
from uncertainpy.data import Data

class TestingUncertaintyCalculations(UncertaintyCalculations):
    def polynomial_chaos(self,
                         uncertain_parameters=None,
                         method="collocation",
                         rosenblatt=False,
                         polynomial_order=3,
                         nr_collocation_nodes=None,
                         quadrature_order=4,
                         nr_pc_mc_samples=10**4,
                         allow_incomplete=False,
                         seed=None):

        arguments = {}

        arguments["function"] = "PC"
        arguments["uncertain_parameters"] = uncertain_parameters
        arguments["method"] = method
        arguments["rosenblatt"] = rosenblatt
        arguments["polynomial_order"] = polynomial_order
        arguments["nr_collocation_nodes"] = nr_collocation_nodes
        arguments["quadrature_order"] = quadrature_order
        arguments["nr_pc_mc_samples"] = nr_pc_mc_samples
        arguments["seed"] = seed
        arguments["allow_incomplete"] = allow_incomplete


        data = Data()
        data.arguments = arguments

        return data


    def monte_carlo(self,
                    uncertain_parameters=None,
                    nr_samples=10**3,
                    seed=None):
        arguments = {}

        arguments["function"] = "MC"
        arguments["uncertain_parameters"] = uncertain_parameters
        arguments["seed"] = seed
        arguments["nr_samples"] = nr_samples

        data = Data()
        data.arguments = arguments

        return data



    def custom_uncertainty_quantification(self, custom_keyword="custom_value"):
        arguments = {}

        arguments["function"] = "custom_uncertainty_quantification"
        arguments["custom_keyword"] = custom_keyword

        data = Data()
        data.arguments = arguments

        return data