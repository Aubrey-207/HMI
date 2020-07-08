import socket
import os
import threading

from PyQt5.Qt import *

class TcpServer(QWidget):
    client_connect_signal = pyqtSignal()
    recv_signal = pyqtSignal(str, )

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.tcp_server_scoket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("init")


    def start_tcp_server(self, ip, port):
        try:
            self.tcp_server_scoket.bind((ip, port))
        except Exception as e:
            print("ip or port error!")
        else:
            self.tcp_server_scoket.listen(128)
            self.tcp_server_scoket.setblocking(False)
            server_th = threading.Thread(target=self.tcp_connect_concurrency)
            server_th.start()
            print("listening!")

    def service_client(self, new_socket, client_addr, recv_data):
        print(str(client_addr[0]) + ":" + str(client_addr[1]) + ":" +recv_data)
        data = str(client_addr[0]) + ":" + str(client_addr[1]) + ":" +recv_data
        self.recv_signal.emit(data)

    def tcp_connect_concurrency(self):
        self.client_sockte_dict = dict()
        while True:
            try:
                new_socket, client_addr = self.tcp_server_scoket.accept()
            except Exception as e:
                pass
            else:
                new_socket.setblocking(False)
                self.client_sockte_dict[str(client_addr)] = new_socket
                self.client_connect_signal.emit()

            for ip in list(self.client_sockte_dict.keys()):
                try:
                    recv_data = self.client_sockte_dict[ip].recv(1024).decode("utf-8")
                except Exception as e:
                    pass
                else:
                    if recv_data:
                        self.service_client(self.client_sockte_dict[ip], client_addr, recv_data)
                    else:
                        self.client_sockte_dict[ip].close()
                        del self.client_sockte_dict[ip]
                        self.client_connect_signal.emit()
                        #self.client_sockte_list.remove(self.client_sockte_dict[ip])

    def tcp_server_send(self, ip, data):
        self.client_sockte_dict[ip].send(data.encode("utf-8"))

    def tcp_close_server(self):
        for client_socket in self.client_sockte_list:
            client_socket.close()
        self.tcp_server_scoket.close()

if __name__ == '__main__':
    tcpserver = TcpServer()
    tcpserver.start_tcp_server("192.168.2.128", 7890)