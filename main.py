import threading
from socket import *
import json


nickname = []
clients = []
pole = [-1, -1, -1, -1, -1, -1, -1, -1, -1]
xod = [1, 0]
WIN = [False]

class Server:





    def __init__(self, ip, port):
        print(f"SERVER IP: {ip}\n SERVER PORT: {port}")
        self.ser = socket(AF_INET, SOCK_STREAM)
        self.ser.bind((ip, 2000))
        self.ser.listen(2)
        self.start_server()








    def obrabotka(self, user, otvet):
        if(len(clients) == 2):
            if(pole[otvet] == -1):
                if(xod[clients.index(user)] == 1):
                    xod[0] = 1
                    xod[1] = 1
                    xod[clients.index(user)] = 0
                    pole[otvet] = clients.index(user)
                    stroka = str(otvet)
                    viner = self.Vinners(user)
                    msg = json.dumps(
                        {'Element': stroka,
                         'KrestikAndNolik': clients.index(user),
                         "VIN": viner,
                         "restart": 0,
                         "playerOne": nickname[0],
                         "playerTwo": nickname[1] }
                    )
                    self.sender(user, msg)
                    print(str(pole[0]) + " " + str(pole[1]) + " " + str(pole[2]))
                    print(str(pole[3]) + " " + str(pole[4]) + " " + str(pole[5]))
                    print(str(pole[6]) + " " + str(pole[7]) + " " + str(pole[8]))
                    print("-------------------")
        else:
            self.VinnersUser()







    def Vinners(self, user):
        if (pole[0] == clients.index(user) and pole[3] == clients.index(user) and pole[6] == clients.index(user)):
            self.VinnersUser()
            return str(nickname[clients.index(user)])

        if (pole[1] == clients.index(user) and pole[4] == clients.index(user) and pole[7] == clients.index(user)):
            self.VinnersUser()
            return str(nickname[clients.index(user)])

        if (pole[2] == clients.index(user) and pole[5] == clients.index(user) and pole[8] == clients.index(user)):
            self.VinnersUser()
            return str(nickname[clients.index(user)])

        if (pole[0] == clients.index(user) and pole[1] == clients.index(user) and pole[2] == clients.index(user)):
            self.VinnersUser()
            return str(nickname[clients.index(user)])

        if (pole[3] == clients.index(user) and pole[4] == clients.index(user) and pole[5] == clients.index(user)):
            self.VinnersUser()
            return str(nickname[clients.index(user)])

        if (pole[6] == clients.index(user) and pole[7] == clients.index(user) and pole[8] == clients.index(user)):
            self.VinnersUser()
            return str(nickname[clients.index(user)])

        if (pole[0] == clients.index(user) and pole[4] == clients.index(user) and pole[8] == clients.index(user)):
            self.VinnersUser()
            return str(nickname[clients.index(user)])

        if (pole[2] == clients.index(user) and pole[4] == 1 and pole[6] == 1):
            self.VinnersUser()
            return str(nickname[clients.index(user)])

        if(self.indexOf(-1) == -1):
            self.VinnersUser()
            return "null"
        return "GAME"


    def VinnersUser(self):
        pole[0] = -1
        pole[1] = -1
        pole[2] = -1
        pole[3] = -1
        pole[4] = -1
        pole[5] = -1
        pole[6] = -1
        pole[7] = -1
        pole[8] = -1


    def indexOf(self, num):
        numi = 0
        while numi != 8:
            if(num == pole[numi]):
                return numi
            numi += 1
        return -1



    def sender(self, user, text):
        for user in clients:
            user.send(text.encode('utf-8'))














    def start_server(self):
        while True:
            user, addr = self.ser.accept()
            print(f"CONNECT. IP: {addr[0]}\n\tPORT: {addr[1]}")
            names = user.recv(1024)
            nickname.append(format(str(names.decode('utf-8'))))
            clients.append(user)  # Добавление в списки клиентов
            thread = threading.Thread(target=self.listen, args=(user, ))  # Запуск многопоточности
            thread.start()  # Старт многопоточности




    def listen(self, user):
        is_work = True
        while is_work:
            try:
                data = user.recv(1024)
                self.Raspozn(data, user)


            except Exception as e:
                print(str(e))
                nickname.pop()
                clients.remove(user)
                self.VinnersUser()
                msg = json.dumps(
                    {
                        'Element': "null",
                        'KrestikAndNolik': "null",
                        "VIN": "restart",
                        "restart": 1,
                        "playerOne": nickname[0],
                        "playerTwo": nickname[1]
                     })
                self.sender(user, msg)
                is_work = False














    def Raspozn(self, otv, user):
        if (otv != ""):
            if (str(otv) == "b'1'"):
                self.obrabotka(user, 1)

            if (str(otv) == "b'2'"):
                self.obrabotka(user, 2)

            if (str(otv) == "b'3'"):
                self.obrabotka(user, 3)

            if (str(otv) == "b'4'"):
                self.obrabotka(user, 4)

            if (str(otv) == "b'5'"):
                self.obrabotka(user, 5)

            if (str(otv) == "b'6'"):
                self.obrabotka(user, 6)

            if (str(otv) == "b'7'"):
                self.obrabotka(user, 7)

            if (str(otv) == "b'8'"):
                self.obrabotka(user, 8)

            if (str(otv) == "b'0'"):
                self.obrabotka(user, 0)




Server('212.76.128.141', 2000)
