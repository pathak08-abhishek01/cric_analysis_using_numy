# importing required libraries
import numpy as np
import csv

# Reading the Data set
data_path = r'/home/abhishek/Data Analysis/Datasets/numpycric.csv'
with open(data_path, 'r') as f:
    reader = csv.reader(f, delimiter=',')
    # get header from first row
    headers = next(reader)
    # get all the rows as a list
    data = list(reader)
    # transform data into numpy array
    data = np.array(data).astype(str)

# Calculate the unique no. of matches in the provided dataset ?
dat_t = data.T
no_of_unique_matches = len(set(dat_t[0]))
print('{} unique matches were played'.format(no_of_unique_matches))

# Find the set of all unique teams that played in the matches in the data set.
total_teams = list(np.union1d(dat_t[3], dat_t[4]))
print('List of participating teams is {}'.format(total_teams))

# Find sum of all extras in all deliveries in all matches in the dataset
extras = dat_t[17].astype(np.int)
total_extra_runs = np.sum(extras)
print('Extra Runs given in total is {}'.format(total_extra_runs))

# Get the array of all delivery numbers when a given player got out. Also mention the wicket type.
condition= dat_t[20] != ''
got_out_players = list(np.extract(condition, dat_t[11]))
wicket_type = list(np.extract(condition, dat_t[21]))
wicket_taken = dict(zip(got_out_players,wicket_type))
print("Fall Of Wicket {}".format(wicket_taken))

# How many matches the team Mumbai Indians has won the toss?
condition2 = dat_t[5] == 'Mumbai Indians'
no_of_toss = len(set(np.extract(condition2, dat_t[0])))
print('Mumbai Indians won {} tosses'.format(no_of_toss))


# Create a filter that filters only those records where the batsman scored 6 runs. Also who has scored the maximum
# no. of sixes overall ?
condition3 = dat_t[16] == '6'
batsman_list = list(np.extract(condition3, dat_t[13]))
six = {}
for x in batsman_list:
    six[x] = six.get(x,0)+1

max_no_six = max(six.values())
batsman_list_most_six = []
for k in six.keys():
    if six[k] == max_no_six:
        batsman_list_most_six.append(k)

print('Batsman with most sixes are {} and {}'.format(batsman_list_most_six[0], batsman_list_most_six[1]))