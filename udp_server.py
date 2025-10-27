import socket

HOST = "127.0.0.1"
PORT = 5005
BUFFER = 4096

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))
print(f"[UDP SERVER] listening on {HOST}:{PORT}", flush=True)

while True:
    data, addr = sock.recvfrom(BUFFER)
    msg = data.decode(errors="replace")
    print(f"[UDP SERVER] from {addr}: {msg!r}", flush=True)
    sock.sendto(data, addr)
