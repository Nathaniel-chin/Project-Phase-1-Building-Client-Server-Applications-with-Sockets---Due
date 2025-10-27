import socket

HOST = "127.0.0.1"  # loopback
PORT = 6006
print("[SERVER] starting...", HOST, PORT, flush=True)

srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
srv.bind((HOST, PORT))
srv.listen(1)
print("[SERVER] listening", flush=True)

conn, addr = srv.accept()
print("[SERVER] connected by", addr, flush=True)
with conn:
    while True:
        data = conn.recv(4096)
        if not data:
            print("[SERVER] client closed", flush=True)
            break
        print("[SERVER] received:", data.decode(errors="replace"), flush=True)
        conn.sendall(data)
