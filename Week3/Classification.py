import numpy as np
import random
import scipy.stats as ss

def distance(p1, p2):
    """Finds the distance between points p1 and p2"""
    print(np.sqrt(np.sum(np.power(p2 - p1, 2))))
    return np.sqrt(np.sum(np.power(p2 - p1, 2)))

p1 = np.array([1,1])
p2 = np.array([4,4])
distance(p1, p2)

def majority_vote_short(votes):
    """Return the most common element in votes"""
    mode, count = ss.mstats.mode(votes)

    print(mode)
    return mode



def majority_vote(votes):
    vote_counts = {}
    for vote in votes:
        if vote in vote_counts:
            vote_counts[vote] += 1
        else:
            vote_counts[vote] = 1

    winners = []
    max_counts = max(vote_counts.values())
    for vote, count in vote_counts.items():
        if count == max_counts:
            winners.append(vote)
    print(winners)
    print(random.choice(winners))
    return random.choice(winners)


votes = [1,2,3,1,2,3,1,2,3,2,2,2]
vote_counts = majority_vote_short(votes)
# max_counts_key = max(vote_counts.keys())
# print(max_counts)



# print(winners)
import matplotlib.pyplot as plt

points = np.array([[1,1], [1,2], [1,3], [2,1], [2,2], [2,3], [3,1], [3,2], [3,3]])
p = np.array([2.5, 2])
distances = np.zeros(points.shape[0])
for i in range(len(distances)):
    distances[i] = distance(p, points[i])

plt.plot(points[:,0], points[:,1], "ro")
plt.plot(p[0], p[1], "bo")
plt.axis([0.5, 3.5, 0.5, 3.5])
