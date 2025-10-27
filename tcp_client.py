import socket

HOST, PORT = "127.0.0.1", 6006

with socket.create_connection((HOST, PORT), timeout=5) as s:
    msg = "hello tcp"
    print("[CLIENT] sending:", msg, flush=True)
    s.sendall(msg.encode())
    reply = s.recv(4096).decode(errors="replace")
    print("[CLIENT] reply:", reply, flush=True)
