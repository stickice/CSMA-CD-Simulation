# nodes_num = The number of nodes connected to the LAN
# trans_packets_num = packets need to transmit per second
# trans_speed = transmission speed (B/s)
# packet_len = Packet length (B)
# nodes_dist = Distance between adjacent nodes (m)
# prop_speed = Propagation speed (m/s)

import random

run1 = {'nodes_num': random.randint(20, 30),
        'fix_nodes_num': 30,
        'trans_packets_num': [random.randint(5, 16) for _ in range(30)],
        'nodes_dist': random.sample(range(1, 186), 30)}

run2 = {'nodes_num': random.randint(20, 30),
        'fix_nodes_num': 20,
        'trans_packets_num': [random.randint(5, 16) for _ in range(20)],
        'nodes_dist': random.sample(range(1, 186), 20)}

run3 = {'nodes_num': random.randint(20, 30),
        'fix_nodes_num': 10,
        'trans_packets_num': [random.randint(5, 16) for _ in range(10)],
        'nodes_dist': random.sample(range(1, 186), 10)}

run5_1 = {'nodes_num': random.randint(20, 30),
          'fix_nodes_num': 10}
run5_2 = {'trans_packets_num': [random.randint(5, 16) for _ in range(run5_1['nodes_num'])],
          'nodes_dist': random.sample(range(1, 186), run5_1['nodes_num'])}


c = 3e8
prop_speed = 0.65 * c
trans_speed = 1.25e6
packet_len = 1500
