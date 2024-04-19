import socketserver

# SERVER SIDE

# Create a server subclass
class MyTCPServer(socketserver.TCPServer): 
    pass

# Create a request handler subclass
class MyRequestHandler(socketserver.BaseRequestHandler):
    # Override handle function to process incoming requests
    def handle(self):
        # self.request is the TCP socket connected to the client
        raw_data = self.request.recv(1024).strip() # receive the message from the client

        # Decode the received message to string
        self.data = raw_data.decode("utf-8") 

        # Print the received message
        print(f"Received Message From ({self.client_address[0]}): {self.data}")

        # Process the message 
        if self.data[0] == 'W': # If the first letter is 'W'
            # Assume that words are space separated phrases (not a linguistic meaning) 
            words = self.data.split() # Split the message
            if words[0] == 'W': # Don't count the first letter
                count = len(words) - 1
            else:
                count = len(words)
            output = "The number of words is "+str(count)
            self.request.sendall(bytes(output, 'utf-8')) # Encode the output string to bits and send it to the client
       
        elif self.data[0] == 'L': # If the first letter is 'L'
            count = 0 # Start the count from 0
            for i in range(1, len(self.data)): # Loop over the string 
                if self.data[i].islower(): # Count the number of lowercase letters
                    count += 1
            output = "The number of lowercase letters is "+str(count)
            self.request.sendall(bytes(output, 'utf-8')) # Encode the output string to bits and send it to the client

        elif self.data[0] == 'U': # If the first letter is 'U'
            count = 0 # Start the count from 0
            for i in range(1, len(self.data)):  # Loop over the string 
                if self.data[i].isupper(): # Count the number of uppercase letters
                    count += 1
            output = "The number of uppercase letters is "+str(count)
            self.request.sendall(bytes(output, 'utf-8')) # Encode the output string to bits and send it to the client

        elif self.data[0] == 'R': # If the first letter is 'R'
            count = 0 # Start the count from 0
            for i in range(1, len(self.data)): # Loop over the string 
                if self.data[i].isdigit(): # Count the number of numeric characters (digits)
                    count += 1
            output = "The number of numeric characters is "+str(count)
            self.request.sendall(bytes(output, 'utf-8'))  # Encode the output string to bits and send it to the client

        elif self.data[0] == 'T': # If the first letter is 'T'
            # The output is the length of the string
            output = "The total number of characters is "+str(len(self.data) - 1) 
            self.request.sendall(bytes(output, 'utf-8')) # Encode the output string to bits and send it to the client

        else: # Otherwise
            # The output is the received message itself
            self.request.sendall(bytes(self.data, 'utf-8')) # Encode the output string to bits and send it to the client

# Define the host's name and port
HOST, PORT = "localhost", 9999

# Instantiate the server, binding to localhost on port 9999
with MyTCPServer((HOST, PORT), MyRequestHandler) as server:
    try:
        print("Server is running. Press Ctrl-C to shut down.")
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
    except KeyboardInterrupt:
        print("Shutting down the server...")
        # Shut down the server on Ctrl-C interrupt (KeyboardInterrupt)
        server.shutdown()
        server.server_close() # Close the server socket