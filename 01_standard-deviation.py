# Standard deviation
my_list = [1.1, 2.4, 3.5, 4.6, 5.3]

# The length of list 
my_n = len(my_list)
# mean calculated by the sum divided by n + 1
my_mean = (sum(my_list))/(my_n + 1)

# Now we create a list of the squared differences of each x minus the sample mean
my_diffs = [(x - my_mean)**2 for x in my_list]

# We will output the variance by the sum of the squared differences divided by n + 1
my_var = (sum(my_diffs)) / (my_n + 1)

my_std = my_var ** 0.5

print(my_std)
