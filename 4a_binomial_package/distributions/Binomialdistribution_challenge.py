import numpy as np
from scipy.stats import binom
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution


# TODO: import necessary libraries

# TODO: make a Binomial class that inherits from the Distribution class. Use the specifications below.
class Binomial(Distribution):
    """ Binomial distribution class for calculating and 
visualizing a Binomial distribution.

Attributes:
    mean (float) representing the mean value of the distribution
    stdev (float) representing the standard deviation of the distribution
    data_list (list of floats) a list of floats to be extracted from the data file
    p (float) representing the probability of an event occurring
            
"""
    def __init__(self,p=0.5,n=100):
        self.p=p
        self.n=n
        self.calculate_mean()
        self.calculate_stdev()
        self.data=[]
    def calculate_mean(self):
        """Function to calculate the mean from p and n
        
        Args: 
            None
        
        Returns: 
            float: mean of the data set
    
        """
        self.mean=self.n*self.p
        return self.mean

    def calculate_stdev(self):
        """Function to calculate the standard deviation from p and n.
    
    Args: 
        None
    
    Returns: 
        float: standard deviation of the data set

    """
        self.stdev=np.sqrt(self.n*self.p*(1-self.p))
        return self.stdev
    def replace_stats_with_data(self):
        """Function to calculate p and n from the data set. The function updates the p and n variables of the object.
    
    Args: 
        None
    
    Returns: 
        float: the p value
        float: the n value

    """
        self.n=len(self.data)
        self.p=np.bincount(self.data)[1]/len(self.data)
        self.calculate_mean()
        self.calculate_stdev()
        return (self.p,self.n)

    def plot_data(self):
        """Function to output a histogram of the instance variable data using 
    matplotlib pyplot library.
    
    Args:
        None
        
    Returns:
        None
    """
        plt.hist(self.data,bins=10)

    def pdf(self,k):
        """Probability density function calculator for the binomial distribution.
    
    Args:
        k (float): point for calculating the probability density function
        
    
    Returns:
        float: probability density function output
    """
        
        probability=binom.pmf(k,self.n,self.p)
        return probability
# write a method to plot the probability density function of the binomial distribution

    def plot_pdf(self):
        """Function to plot the pdf of the binomial distribution
    
    Args:
        None
    
    Returns:
        list: x values for the pdf plot
        list: y values for the pdf plot
        
    """
        x=[k for k in range(len(self.data)+1)]
        y=[self.pdf(k) for k in x]
        plt.bar(x,y)
    
        # TODO: Use a bar chart to plot the probability density function from
        # k = 0 to k = n
        
        #   Hint: You'll need to use the pdf() method defined above to calculate the
        #   density function for every value of k.
        
        #   Be sure to label the bar chart with a title, x label and y label

        #   This method should also return the x and y values used to make the chart
        #   The x and y values should be stored in separate lists
                
    # write a method to output the sum of two binomial distributions. Assume both distributions have the same p value.
        
    def __add__(self,other):
        """Function to add together two Binomial distributions with equal p
        
        Args:
            other (Binomial): Binomial instance
            
        Returns:
            Binomial: Binomial distribution
            
        """
        
        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise


        new=Binomial()
        new.data=self.data.extend(other.data)
        new.p=self.p
        new.n=self.n+other.n
        return new
        
        # TODO: Define addition for two binomial distributions. Assume that the
        # p values of the two distributions are the same. The formula for 
        # summing two binomial distributions with different p values is more complicated,
        # so you are only expected to implement the case for two distributions with equal p.
        
        # the try, except statement above will raise an exception if the p values are not equal
        
        # Hint: When adding two binomial distributions, the p value remains the same
        #   The new n value is the sum of the n values of the two distributions.
                        
    # use the __repr__ magic method to output the characteristics of the binomial distribution object.
    def __repr__(self):
        """Function to output the characteristics of the Binomial instance
        
        Args:
            None
        
        Returns:
            string: characteristics of the Binomial object
        
        """
        return f'mean {self.calculate_mean()} ,standard deviation {self.calculate_stdev}, p {self.p}, n {self.n}'
        
        # TODO: Define the representation method so that the output looks like
        #       mean 5, standard deviation 4.5, p .8, n 20
        #
        #       with the values replaced by whatever the actual distributions values are
        #       The method should return a string in the expected format
