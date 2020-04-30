import socket

def raiseException(recv):
    if recv == "*":
        raise Exception("Socket closed")

if __name__ == "__main__":
    serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversock.bind(("192.168.0.53", 6000))
    serversock.listen()

    mainLoop = True
    while mainLoop:
        try:
            client, address = serversock.accept()
            
            correctSend = False
            while not correctSend:
                codeOrURL = input("Do you have a code or a url: ")
                if codeOrURL == "code":
                    param = input("Please enter the code: ")
                    correctSend = True
                elif codeOrURL == "url":
                    param = input("Please enter the url: ")
                    correctSend = True
                else:
                    print("Not a valid join type please try again.")
            
            combinedMsg = codeOrURL+"kDsJ^*&322@@"+param
            lenCombined = str(len(combinedMsg))
            client.send(lenCombined.encode())
            raiseException(client.recv(4).decode())
            client.send(combinedMsg.encode())
            raiseException(client.recv(4).decode())

            client.send(b'RDY')
            raiseException(client.recv(3).decode())

            contMsg = True
            while contMsg:
                msg = input(">> ")
                msgLen = str(len(msg))
                client.send(msgLen.encode())
                raiseException(client.recv(4).decode())
                client.send(msg.encode())
                raiseException(client.recv(4).decode())
            
                if ((msg == "/reset") or (msg == "/disconnect")):
                    contMsg = False
                    client.close()
                elif msg == "/exit":
                    contMsg = False
                    mainLoop = False
                    client.close()
                    serversock.close()

        except Exception as e:
            try:
                client.close()
            except:
                pass
            print(f"Error Encountered: '{e}'.'")
            continue
