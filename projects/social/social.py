import random
import sys
sys.path.append('../graph')
from util import Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # Add users
        for i in range(0, num_users):
            self.add_user(f"User {i}")

        # Create Friendships
        # Generate all possible friendship combinations
        possible_friendships = []

        # Avoid duplicates by ensuring the first number is smaller than the
        # second
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))

        # Shuffle the possible friendships
        random.shuffle(possible_friendships)

        # Create friendships for the first X pairs of the list
        # X is determined by the formula: num_users * avg_friendships // 2
        # Need to divide by 2 since each add_friendship() creates 2 friendships
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set

        q = Queue()
        q.enqueue([user_id])

        # go through friends (neighbors) in breadth-first order
        while q.size() > 0:
            path = q.dequeue()
            user = path[-1]
            if user not in visited:
                visited[user] = path
            for friend in self.friendships[user]:
                if friend not in visited:
                    q.enqueue(path + [friend])
        return visited




if __name__ == '__main__':
    num_trials = 10
    # tot_perc_extended = 0
    tot_perc_avg_num = 0
    tot_avg_degree = 0

    for t in range(num_trials):
        sg = SocialGraph()
        num_users = 1000
        avg_friendships = 5
        sg.populate_graph(num_users, avg_friendships)
        # print(sg.friendships)
        # connections = sg.get_all_social_paths(1)
        # print(connections)

        all_connections = {}
        num_connections = {}
        total = 0
        total2 = 0
        for i in range(1,num_users+1):
            connections = sg.get_all_social_paths(i)
            all_connections[i] = connections
            num_connections[i] = len(connections)
            total += len(connections)
            degree = sum([len(x) for x in connections.values()])
            total2 += degree

        print('Trial',t+1)
        # print('All connections:', all_connections)
        # print('Number of connections:',num_connections)

        avg_num = (total / num_users) - 1
        perc_avg_num = 100 * (avg_num / (num_users - 1))
        print('Percentage of other users in extended network:', round(perc_avg_num, 2),'%')
        tot_perc_avg_num += perc_avg_num

        avg_degree = (total2 - total) / (total - num_users)
        print('Average degree of separation:', round(avg_degree,2))
        tot_avg_degree += avg_degree
        print()

        # print('Average number of connections:', round(avg_num,1))
        # print('Average number of 1st order connections:', avg_friendships)
        # print('Average number of 2+ order connections:', round(avg_num -
        # avg_friendships,1))
        # perc_extended = 100 * (1 - avg_friendships / avg_num)
        # print('Percentage of 2+ order connections:', round(perc_extended,
        # 2),'%')
        # tot_perc_extended += perc_extended

    print('Summary after',num_trials,'trials')
    print('Percentage of other users in extended network:', round(tot_perc_avg_num / num_trials, 2),'%')
    print('Average degree of separation:', round(tot_avg_degree / num_trials,2))

    # print('Percentage of 2+ order connections:', round(tot_perc_extended /
    # num_trials,2),'%')






