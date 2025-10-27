Client-Server Socket Application (UDP & TCP)

This project demonstrates a simple client-server application using UDP and TCP sockets in Python.

✅ 1. Requirements

Python 3 installed

Files in the same folder:

udp_server.py

udp_client.py

tcp_server.py

tcp_client.py

✅ 2. Running the UDP Application
Step 1: Start the UDP Server

Open a terminal and run:

python udp_server.py


You should see:

[UDP SERVER] listening on 127.0.0.1:5005

Step 2: Run the UDP Client

Open another terminal in the same folder and run:

python udp_client.py


Expected output:

[UDP CLIENT] sending: hello udp
[UDP CLIENT] reply: hello udp

✅ 3. Running the TCP Application
Step 1: Start the TCP Server

In a terminal, run:

python tcp_server.py


You should see:

[SERVER] starting... 127.0.0.1 6006
[SERVER] listening

Step 2: Run the TCP Client

Open another terminal and run:

python tcp_client.py


Expected output:

[CLIENT] sending: hello tcp
[CLIENT] reply: hello tcp
