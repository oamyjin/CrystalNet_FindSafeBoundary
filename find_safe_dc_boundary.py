from optparse import OptionParser

# One node in the topology has its own node number and directly linked nodes
# node_no: the number of the node (start from 1)
# parents: the connected upper layer nodes list (may be empty)
class Node:
    def __init__(self, node_no):
        self.node_no = node_no
        self.parents = []

    def add_parent(self, new_parent):
        self.parents.append(new_parent)

    def get_parents(self):
        return self.parents

    def get_no(self):
        return self.node_no


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-g", "--input_topology", dest="topology_file", help="the file of the datacenter network topology",
                      default="topology.txt")
    parser.add_option("-d", "--input_devices", dest="devices_file", help="the file of the input devices by operators to be emulated",
                      default="devices.txt")
    parser.add_option("-o", "--output_devices", dest="emu_devices_file", help="the output file of the all devices to be emulated",
                      default="emu_devices.txt")
    options, args = parser.parse_args()

    total_nodes_num = 0
    nodes = []

    # read the input topology file to create topology
    lines = open(options.topology_file, "r").readlines()

    # create nodes
    total_nodes_num = int(lines[0])
    lines.pop(0)
    for n in range(total_nodes_num):
        nodes.append(Node(n + 1))

    # add links to nodes
    for line in lines:
        p, c = map(float, line.strip().split(' '))
        # only modify the child node by adding the parent node
        nodes[int(c) - 1].add_parent(nodes[int(p) - 1])

    # read the input devices file
    lines = open(options.devices_file, "r").readlines()
    devices = []
    for line in lines:
        for d in line.strip().split(' '):
            devices.append(nodes[int(d) - 1])

    emu_devices = [] # all the devices to be emulated
    # find all devices to be emulated
    while len(devices) != 0:
        device = devices.pop()
        emu_devices.append(device)
        # if the node has no parents, it is the highest layer device
        if len(device.get_parents()) == 0:
            continue
        # otherwise, add all parent nodes into the emu_devices
        for parent in device.get_parents():
            if (parent in devices) or (parent in emu_devices):
                continue
            devices.append(parent)

    # record the devices to the output file
    ofile = open(options.emu_devices_file, "w")

    # number of total emulated devices, and the percentage among all devices
    ofile.write("%d %.1f%%\n" % (len(emu_devices), len(emu_devices) / total_nodes_num * 100))
    for emu_device in emu_devices:
        ofile.write("%d " % emu_device.get_no())
    ofile.close()

    # speaker devices

# to run the .py file, use the following command:
# python find_safe_dc_boundary.py -g topology.txt -d devices.txt -o emu_devices.txt