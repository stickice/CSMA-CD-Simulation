import random
import math
import collections
from class_node import Node
import utils
import parameters
import numpy as np
from main import main


def build_nodes(nodes_num, trans_packets_num, nodes_dist):
    nodes = []
    # print(len(nodes_dist), len(trans_packets_num))
    for i in range(nodes_num):
        nodes.append(Node(nodes_dist[i], trans_packets_num[i]))
        # print(i+1)
    return nodes


def imp(nodes_num, trans_packets_num, trans_speed, packet_len, nodes_dist, prop_speed, is_persistent=True):
    sim_time = 10
    curr_time = 0
    transmitted_packets = 0
    suc_trans_packets = 0
    nodes = build_nodes(nodes_num, trans_packets_num, nodes_dist)
    lost_packets = []
    x_time = []
    collision_cnt = 0
    collision_num = []
    trans_num = []
    suc_trans_num = []
    cnt = 1

    while True:

        min_node = Node(None, trans_packets_num[0])
        min_node.queue = [float("infinity")]
        for node in nodes:
            if len(node.queue) > 0:
                min_node = min_node if min_node.queue[0] < node.queue[0] else node

        if min_node.location is None:
            print('All packets transferred!')
            break

        curr_time = min_node.queue[0]
        transmitted_packets += 1

        collision_occurred_once = False
        # i = 0
        for node in nodes:
            # print(i)
            # i+=1
            if node.location != min_node.location and len(node.queue) > 0:
                delta_location = abs(min_node.location - node.location)
                t_prop = delta_location / prop_speed
                t_trans = packet_len / trans_speed

                # Check collision
                will_collide = True if node.queue[0] <= (curr_time + t_prop) else False

                if (curr_time + t_prop) < node.queue[0] < (curr_time + t_prop + t_trans):
                    if is_persistent is True:
                        for i in range(len(node.queue)):
                            if (curr_time + t_prop) < node.queue[i] < (curr_time + t_prop + t_trans):
                                node.wait_collisions += 1
                                if node.wait_collisions > node.MAX_COLLISIONS:
                                    node.pop_packet()
                                backoff_time = node.exponential_backoff_time(trans_speed, node.wait_collisions)
                                node.queue[i] = (curr_time + t_prop + t_trans + backoff_time)
                            else:
                                break
                    else:
                        node.non_persistent_bus_busy(trans_speed)

                if will_collide:
                    collision_occurred_once = True
                    transmitted_packets += 1
                    node.collision_occured(trans_speed)

        if collision_occurred_once is not True:  # If no collision happened
            suc_trans_packets += 1
            min_node.pop_packet()
        else:  # If a collision occurred
            min_node.collision_occured(trans_speed)
            collision_cnt += 1
            # print(successfully_transmitted_packets)

        running_time = transmitted_packets * packet_len / trans_speed
        # if running_time*10 >= 0.1*cnt:
        x_time.append(running_time)
        lost_packets.append(transmitted_packets - suc_trans_packets)
        collision_num.append(collision_cnt)
        trans_num.append(transmitted_packets)
        suc_trans_num.append(suc_trans_packets)
        # cnt += 1
        if running_time >= sim_time:
            print(running_time)
            print(suc_trans_packets)
            print(transmitted_packets)
            print('end!')
            break

    return {'nodes_num': nodes_num, 'x_time': x_time, 'lost_packets': lost_packets,
            'collision_num': collision_num, 'trans_num': trans_num, 'suc_trans_num': suc_trans_num}


if __name__ == "__main__":
    # 'nodes_num'
    # 'fix_nodes_num'
    # 'trans_packets_num'
    # 'nodes_dist'

    run6 = main(parameters.run2['fix_nodes_num'], parameters.run2['trans_packets_num'], parameters.trans_speed,
                parameters.packet_len, parameters.run2['nodes_dist'], parameters.prop_speed)
    #
    # run7 = main(parameters.run2['fix_nodes_num'], parameters.run2['trans_packets_num'], 6.25e6,
    #             parameters.packet_len, parameters.run2['nodes_dist'], parameters.prop_speed)
    #
    # run8 = main(parameters.run2['fix_nodes_num'], parameters.run2['trans_packets_num'], 1.25e7,
    #             parameters.packet_len, parameters.run2['nodes_dist'], parameters.prop_speed)

    run9 = imp(parameters.run2['fix_nodes_num'], parameters.run2['trans_packets_num'], parameters.trans_speed,
                parameters.packet_len, parameters.run2['nodes_dist'], parameters.prop_speed)

    # utils.draw_imp_trans([run6, run7, run8])
    # utils.draw_single_lost(run9)
    utils.draw_imp_listen_time([run6, run9])