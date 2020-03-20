from select import *
import select, socket, sys

ADDRESS_A = '192.168.1.30'
ADDRESS_B = '192.168.1.10'
PORT_A = 50000
PORT_B = 50001

socketA = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socketB = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#server.setblocking(0)
socketA.bind(('', PORT_A))
socketB.bind(('', PORT_B))
#server.listen(5)
inputs = [socketA, socketB]
outputs = []
#message_queues = {}

while inputs:
#    readable, writable, exceptional = select.select(inputs, outputs, inputs)
    readable, writable, exceptional = select.select(inputs, [], [])
    for s in readable:
        #data = s.recv(1024)
        msg, address = s.recvfrom(8192)
        print(f"message: {msg}\nfrom: {address}")
        if (s == socketA):
            socketB.sendto(msg, (ADDRESS_B, 8080))
        else:
            socketA.sendto(msg, (ADDRESS_A, 8080))

        #send_socket.sendto(msg.encode(), (ADDRESS, PORT))

        #if s is server:
        #    connection, client_address = s.accept()
        #    connection.setblocking(0)
        #    inputs.append(connection)
        #    message_queues[connection] = Queue.Queue()
        #else:
        #    data = s.recv(1024)
        #    if data:
        #        message_queues[s].put(data)
        #        if s not in outputs:
        #            outputs.append(s)
        #    else:
        #        if s in outputs:
        #            outputs.remove(s)
        #        inputs.remove(s)
        #        s.close()
        #        del message_queues[s]

    #for s in writable:
    #    try:
    #        next_msg = message_queues[s].get_nowait()
    #    except Queue.Empty:
    #        outputs.remove(s)
    #    else:
    #        s.send(next_msg)

    #for s in exceptional:
    #    inputs.remove(s)
    #    if s in outputs:
    #        outputs.remove(s)
    #    s.close()
    #    del message_queues[s]
