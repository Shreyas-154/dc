from xmlrpc.server import SimpleXMLRPCServer

# Function to concatenate strings

def concatenate(a, b):
    return a + b

# Create server
server = SimpleXMLRPCServer(("localhost", 8000))

print("Server is running...")

# Register function
server.register_function(concatenate, "concatenate")

# Keep server running
server.serve_forever()
#-----------------------------

import xmlrpc.client

# Connect to server
client = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Take input
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Remote method call
result = client.concatenate(str1, str2)

# Display result
print("Concatenated String:", result)

#---------------------------
"""
    ConcatInterface.java
import java.rmi.Remote;
import java.rmi.RemoteException;

public interface ConcatInterface extends Remote
{
    String concatenate(String a, String b) throws RemoteException;
}
"""
"""
    Server.java
    import java.rmi.Naming;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class Server extends UnicastRemoteObject implements ConcatInterface
{
    // Constructor
    public Server() throws RemoteException
    {
        super();
    }

    // Method implementation
    public String concatenate(String a, String b)
    {
        return a + b;
    }

    public static void main(String args[])
    {
        try
        {
            // Create server object
            Server obj = new Server();

            // Register object with name
            Naming.rebind("rmi://localhost/concat", obj);

            System.out.println("Server is running...");
        }
        catch(Exception e)
        {
            System.out.println(e);
        }
    }
}
    """
    
"""
    Client.java
    import java.rmi.Naming;
import java.util.Scanner;

public class Client
{
    public static void main(String args[])
    {
        try
        {
            // Lookup remote object
            ConcatInterface obj =
            (ConcatInterface) Naming.lookup("rmi://localhost/concat");

            Scanner sc = new Scanner(System.in);

            // Input strings
            System.out.print("Enter first string: ");
            String str1 = sc.nextLine();

            System.out.print("Enter second string: ");
            String str2 = sc.nextLine();

            // Remote method call
            String result = obj.concatenate(str1, str2);

            // Display result
            System.out.println("Concatenated String: " + result);
        }
        catch(Exception e)
        {
            System.out.println(e);
        }
    }
}
    """
    