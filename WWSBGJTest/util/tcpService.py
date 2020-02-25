import socket
import select

def start_server():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind("127.0.0.1", 8000)
    server_sock.listen(2)
    read_inputs = [s_handler, ]

    while True:
        print "waiting for connection..."
        rs, _, _ = select.select(read_inputs, [], [], 10)
        print 'receive new: %r %r' % (rs, read_inputs)
        for r_handler in rs:
            if r_handler is s_handler:
                c_socket, c_address = r_handler.accept()
                read_inputs.append(c_socket)
            else:
                data = r_handler.recv(1024)
                if not data:
                    read_inputs.remove(r_handler)
                else:
                    r_handler.send('demo')
                    print data

if __name__ == "__main__":
    start_server()
