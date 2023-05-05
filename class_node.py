import random
import math
import collections
import utils

maxSimulationTime = 10


class Node:
    def __init__(self, location, trans_packets_num):
        self.queue = collections.deque(self.generate_queue(trans_packets_num))
        self.location = location
        self.collisions = 0
        self.wait_collisions = 0
        self.MAX_COLLISIONS = 10

    def collision_occured(self, trans_speed):
        self.collisions += 1
        if self.collisions > self.MAX_COLLISIONS:
            return self.pop_packet()

        backoff_time = self.queue[0] + self.exponential_backoff_time(trans_speed, self.collisions)

        for i in range(len(self.queue)):
            if backoff_time >= self.queue[i]:
                self.queue[i] = backoff_time
            else:
                break

    def successful_transmission(self):
        self.collisions = 0
        self.wait_collisions = 0

    def generate_queue(self, trans_packets_num):
        packets = []
        arrival_time_sum = 0

        while arrival_time_sum <= maxSimulationTime:
            arrival_time_sum += utils.get_exponential_random_variable(trans_packets_num)
            packets.append(arrival_time_sum)
        return sorted(packets)

    def exponential_backoff_time(self, trans_speed, general_collisions):
        rand_num = random.random() * (pow(2, general_collisions) - 1)
        return rand_num * 64/float(trans_speed)

    def pop_packet(self):
        self.queue.popleft()
        self.collisions = 0
        self.wait_collisions = 0

    def non_persistent_bus_busy(self, trans_speed):
        self.wait_collisions += 1
        if self.wait_collisions > self.MAX_COLLISIONS:
            return self.pop_packet()

        backoff_time = self.queue[0] + self.exponential_backoff_time(trans_speed, self.wait_collisions)

        for i in range(len(self.queue)):
            if backoff_time >= self.queue[i]:
                self.queue[i] = backoff_time
            else:
                break

