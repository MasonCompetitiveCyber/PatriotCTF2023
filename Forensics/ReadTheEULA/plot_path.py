import json
import matplotlib.pyplot as plt
import numpy as np


def plot_path(coords):
    # Unzip the coordinates
    x, y = zip(*coords)
    
    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, '-o', label='Path', color='blue')
    plt.scatter(x[0], y[0], color='green', label='Start')
    plt.scatter(x[-1], y[-1], color='red', label='End')
    
    # Annotations & Display
    plt.title('Path of the Particle')
    plt.xlabel('X-coordinate')
    plt.ylabel('Y-coordinate')
    plt.legend()
    plt.grid(True)
    plt.show()

with open("minetestpcap.json", "rb") as f:
    packets = json.load(f)

positions = []
 
for packet in packets:
    minetest_packet = packet["_source"]["layers"]["minetest.client"]
    x = minetest_packet["minetest.client.playerpos_x"]
    z = minetest_packet["minetest.client.playerpos_z"]
    positions.append((int(x), int(z)))

x_avg = 0
y_avg = 0

for coord in positions:
    x_avg += coord[0]
    y_avg += coord[1]

x_avg /= len(positions)
y_avg /= len(positions)

path = [(x_avg - coord[0], y_avg - coord[1]) for coord in positions]
plot_path(positions)