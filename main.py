import sys
import json
from PyQt5.QtWidgets import QApplication

from TcpServer import TcpServer
from MainForm import MainForm
from TcpServer_Panel import TcpServer_Panel
from LoginForm import LoginForm
from User import *

def on_clicked_btn_Send():
    print("clicked")

#user_dict = {}

if __name__ == '__main__':
    app = QApplication(sys.argv)



    mainForm = MainForm()
    loginForm = LoginForm()
    tcpServerPanel = TcpServer_Panel()
    tcpServer = TcpServer()

    def load_users(file_path):
        with open(file_path, "r") as f:
            global user_dict
            user_dict = json.load(f)

        for key in user_dict["users"]:
            loginForm.comboBox_Account.addItem(key)

    def slot_check_login(account, pwd):
        if user_dict["users"][account]["password"] == pwd:
            print("登录成功")

            mainForm.show()
            loginForm.hide()
        else:
            loginForm.show_error_animation()
            print("登录失败")

    def slot_show_server():
        tcpServerPanel.show()

    def slot_listen(ip, port):
        print("listen")
        tcpServer.start_tcp_server(ip, int(port))

    def slot_client_connect():
        tcpServerPanel.cmb_Client.clear()
        tcpServerPanel.cmb_Client.addItems(tcpServer.client_sockte_dict.keys())

    def slot_server_recv(data):
        tcpServerPanel.textEdit_Recv.append(data)

    def slot_send(data):
        print("send")
        tmp = tcpServerPanel.cmb_Client.currentText()
        print(tmp)
        tcpServer.tcp_server_send(tcpServerPanel.cmb_Client.currentText(), data)

    #
    mainForm.openserver_signal.connect(slot_show_server)
    #
    tcpServerPanel.listen_signal.connect(slot_listen)
    tcpServerPanel.send_signal.connect(slot_send)
    #
    tcpServer.client_connect_signal.connect(slot_client_connect)
    tcpServer.recv_signal.connect(slot_server_recv)
    #
    loginForm.check_login_signal.connect(slot_check_login)
    #mainForm.show()
    load_users("User.json")
    loginForm.comboBox_Account.setCurrentIndex(2)
    #loginForm.read_jason("User.json")
    loginForm.show()

    sys.exit(app.exec())