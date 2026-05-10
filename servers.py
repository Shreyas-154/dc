# Load Balancing Algorithms Simulation

import random

# ============================================
# 1. ROUND ROBIN
# Concept: Distribute requests equally
# ============================================

print("==== ROUND ROBIN ====")
print("Distributes requests evenly across all servers in order\n")

# List of servers
servers = ["Server1", "Server2", "Server3"]

# Keep track of current server index
current_index = 0

# Simulate 6 requests
for request_number in range(1, 7):

    # Select current server
    selected_server = servers[current_index]

    # Print allocation
    print(f"Request {request_number} -> {selected_server}")

    # Move to next server
    current_index = current_index + 1

    # If index exceeds list size, reset to 0
    if current_index >= len(servers):
        current_index = 0


# ============================================
# 2. WEIGHTED ROUND ROBIN
# Concept: Powerful servers get more requests
# ============================================

print("\n==== WEIGHTED ROUND ROBIN ====")
print("Server1 is powerful: gets 5 requests")
print("Server2 and Server3 get 1 request each\n")

# Define server weights
server_weights = {
    "Server1": 5,
    "Server2": 1,
    "Server3": 1
}

# Create weighted server list
weighted_server_list = []

for server_name, weight in server_weights.items():

    for i in range(weight):

        weighted_server_list.append(server_name)

# Show weighted cycle
print("Server Cycle:", weighted_server_list)
print()

# Simulate 7 requests
for request_number in range(1, 8):

    # Get position in cycle
    position_in_cycle = (request_number - 1) % len(weighted_server_list)

    # Select server
    selected_server = weighted_server_list[position_in_cycle]

    # Print allocation
    print(f"Request {request_number} -> {selected_server}")


# ============================================
# 3. LEAST CONNECTIONS
# Concept: Choose server with minimum workload
# ============================================

print("\n==== LEAST CONNECTIONS ====")
print("Choose server with least active connections\n")

# Store active connections
active_connections = {
    "Server1": 0,
    "Server2": 0,
    "Server3": 0
}

# Simulate 6 requests
for request_number in range(1, 7):

    # Initialize minimum values
    server_with_least_connections = None
    minimum_connections = float('inf')

    # Find least loaded server
    for server_name, connection_count in active_connections.items():

        if connection_count < minimum_connections:

            minimum_connections = connection_count
            server_with_least_connections = server_name

    # Print selected server
    print(f"Request {request_number} -> {server_with_least_connections}")

    # Print connection counts before update
    print("Connection counts before:", active_connections)

    # Simulate new connections
    new_connections = random.randint(0, 2)

    # Increase connections
    active_connections[server_with_least_connections] += new_connections

    # Print updated connections
    print("Connection counts after: ", active_connections)
    print()


# ============================================
# 4. LEAST RESPONSE TIME
# Concept: Choose fastest server
# ============================================

print("\n==== LEAST RESPONSE TIME ====")
print("Choose the server with minimum response time\n")

# Simulate 6 requests
for request_number in range(1, 7):

    # Generate random response times
    current_response_times = {
        "Server1": round(random.uniform(0.1, 1.0), 2),
        "Server2": round(random.uniform(0.1, 1.0), 2),
        "Server3": round(random.uniform(0.1, 1.0), 2)
    }

    # Initialize minimum values
    fastest_server = None
    fastest_time = float('inf')

    # Find fastest server
    for server_name, response_time in current_response_times.items():

        if response_time < fastest_time:

            fastest_time = response_time
            fastest_server = server_name

    # Print selected server
    print(f"Request {request_number} -> {fastest_server}")

    # Print all response times
    print(
        f"Response Times: "
        f"Server1={current_response_times['Server1']}s, "
        f"Server2={current_response_times['Server2']}s, "
        f"Server3={current_response_times['Server3']}s"
    )

    # Print fastest server
    print(f"Fastest: {fastest_server} at {fastest_time}s")
    print()