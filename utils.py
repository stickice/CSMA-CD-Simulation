import random
import math
import collections
import matplotlib.pyplot as plt

def get_exponential_random_variable(num):
    uniform_random_value = 1 - random.uniform(0, 1)
    exponential_random_value = (-math.log(1 - uniform_random_value) / float(num))
    return exponential_random_value


def draw_lost_packets(data):
    plt.plot(data[0]['x_time'], data[0]['lost_packets'])
    plt.plot(data[1]['x_time'], data[1]['lost_packets'])
    plt.plot(data[2]['x_time'], data[2]['lost_packets'])
    plt.legend(('30 nodes', '20 nodes', '10 nodes'))
    plt.xlabel('Time (s)')
    plt.ylabel('Packets')
    plt.show()
    # plt.savefig('./imgs/lost_packets.png')
    plt.close()


def draw_collision_num(data):
    plt.plot(data[0]['x_time'], data[0]['collision_num'])
    plt.plot(data[1]['x_time'], data[1]['collision_num'])
    plt.plot(data[2]['x_time'], data[2]['collision_num'])
    plt.legend(('30 nodes', '20 nodes', '10 nodes'))
    plt.xlabel('Time (s)')
    plt.ylabel('Collisions')
    plt.show()
    # plt.savefig('./imgs/collision_num.png')
    plt.close()


def draw_cmp_persistent(data):
    plt.plot(data[0]['x_time'], data[0]['lost_packets'])
    plt.plot(data[1]['x_time'], data[1]['lost_packets'])
    plt.legend(('p-persistent', 'non-persistent'))
    plt.xlabel('Time (s)')
    plt.ylabel('Packets')
    plt.show()
    # plt.savefig('./imgs/lost_packets.png')
    plt.close()


def draw_normal_run(data):
    plt.plot(data['x_time'], data['trans_num'])
    plt.plot(data['x_time'], data['suc_trans_num'])
    plt.plot(data['x_time'], data['lost_packets'])
    plt.legend(('transmitted packets', 'successfully transmitted packets', 'lost packets'))
    plt.xlabel('Time (s)')
    plt.ylabel('Packets')
    # plt.savefig('./imgs/normal_run.png')
    plt.show()
    plt.close()


def draw_single_lost(data):
    plt.plot(data['x_time'], data['lost_packets'])
    plt.legend(('lost packets',))
    plt.xlabel('Time (s)')
    plt.ylabel('Packets')
    # plt.savefig('./imgs/single_lost.png')
    plt.show()
    plt.close()


def draw_imp_trans(data):
    plt.plot(data[0]['x_time'], data[0]['lost_packets'])
    plt.plot(data[1]['x_time'], data[1]['lost_packets'])
    plt.plot(data[2]['x_time'], data[2]['lost_packets'])
    plt.legend(('transmission_speed=1.25MB/s', 'transmission_speed=6.25MB/s', 'transmission_speed=12.5MB/s'))
    plt.xlabel('Time (s)')
    plt.ylabel('Lost Packets')
    # plt.savefig('./imgs/improve_trans.png')
    plt.show()
    plt.close()


def draw_imp_listen_time(data):
    plt.plot(data[0]['x_time'], data[0]['lost_packets'])
    plt.plot(data[1]['x_time'], data[1]['lost_packets'])
    plt.legend(('w/o additional listening time', 'w/ additional listening time'))
    plt.xlabel('Time (s)')
    plt.ylabel('Lost Packets')
    # plt.savefig('./imgs/improve_listen_time.png')
    plt.show()
    plt.close()

    plt.plot(data[1]['x_time'], data[1]['lost_packets'])
    plt.legend(('w/ additional listening time',))
    plt.xlabel('Time (s)')
    plt.ylabel('Lost Packets')
    # plt.savefig('./imgs/single_listen_time.png')
    plt.show()
    plt.close()
