'''
run me:

$ python3 create_server.py

and in another shell:

$ echo hi | nc 127.0.0.1 8888
'''
# ref: https://stackoverflow.com/questions/43124340/python-3-6-coroutine-was-never-awaited
import asyncio

class MyProtocol(asyncio.Protocol):
    def __getattribute__(self, name):
        """intercept and print all acceccess to this class's methods so we can see what callbacks we can support"""
        print('__getattribute__', name)
        return super().__getattribute__(name)

    def connection_made(self, transport):
        print('Connection made', transport)
        self.transport = transport

    def data_received(self, data):
        print(self.transport, 'data received', data)

loop = asyncio.new_event_loop()
# Each client connection will create a new protocol instance
coro = loop.create_server(MyProtocol, '127.0.0.1', 8888)
server = loop.run_until_complete(coro)
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

'''
Output:

__getattribute__ __class__
__getattribute__ connection_made
Connection made <_SelectorSocketTransport fd=7 read=idle write=<idle, bufsize=0>>
__getattribute__ data_received
__getattribute__ transport
<_SelectorSocketTransport fd=7 read=polling write=<idle, bufsize=0>> data received b'hi\n'
__getattribute__ eof_received
__getattribute__ connection_lost
'''
