import socket
import time
import struct
import locale

def server_program():
    host = '0.0.0.0'
    port = 5656

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(1)
    conn, address = server_socket.accept()  # accept new connection
    conn.settimeout(60) # 60 second timeout
    print("Connection from: " + str(address))

    dump_data = bytearray()
    while True:
        try:
            data = conn.recv(0x10000)
            if not data:
                break
            dump_data.extend(data)
            print("Received " + str(len(dump_data)) + " bytes...")
        except socket.timeout:
            print("Timeout reached for receiving data (1 min)")
            break

    # write to file
    timestr = time.strftime("%Y%m%d-%H%M%S")
    print("[+] Writing dump to dump-" + timestr + ".bin...")
    f = open("dump-" + timestr + ".bin", "wb")
    f.write(dump_data)
    f.close()

    conn.close()

if __name__ == '__main__':
    server_program()