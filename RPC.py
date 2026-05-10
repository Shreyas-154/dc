from xmlrpc.server import SimpleXMLRPCServer

# function to calculate factorial
def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact

# create server
server = SimpleXMLRPCServer(("localhost", 8000))

print("Server is running...")

# register function
server.register_function(factorial, "factorial")

# keep server running
server.serve_forever()

#--------------------------
import xmlrpc.client

# connect to server
client = xmlrpc.client.ServerProxy("http://localhost:8000/")

# take input
num = int(input("Enter a number: "))

# call remote function
result = client.factorial(num)

# display result
print("Factorial is:", result)