import socket

HOST, PORT = "127.0.0.1", 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
msg = "hello udp"
print("[UDP CLIENT] sending:", msg, flush=True)
sock.sendto(msg.encode(), (HOST, PORT))
data, _ = sock.recvfrom(4096)
print("[UDP CLIENT] reply:", data.decode(errors="replace"), flush=True)
sock.close()
