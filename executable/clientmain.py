import socket
from webdriver import WebDriver

if __name__ == "__main__":
    IP = "60.227.19.217"
    PORT = 6000

    driver = WebDriver()
    login = False
    while not login:
        try:
            email = input("Please enter your school email here: ")
            password = input("Please enter your school password here: ")
            driver.login(email, password)
            login = True
        except:
            driver.reset()

    # This part is for the proof that no emails or passwords are stored or sent anywhere
    email = ""
    password = ""

    loop = True
    while loop:
        try:
            driver.reset()
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((IP, PORT))
            
            msgLen = int(sock.recv(10).decode())
            sock.send(b'RCVD')
            combinedMessage = sock.recv(msgLen).decode()
            sock.send(b'RCVD')

            # This is going to process the message and join the meet correctly and establishes the timings between the two
            splitMessage = combinedMessage.split("kDsJ^*&322@@")
            if splitMessage[0] == "code":
                driver.hasCode(splitMessage[1])
            else:
                driver.getFromURL(splitMessage[1])
            driver.joinMeet()
            sock.recv(3)
            sock.send(b'RDY')

            while True:
                msgLen = int(sock.recv(10).decode())
                sock.send(b'RCVD')
                msg = sock.recv(msgLen).decode()
                sock.send(b'RCVD')

                print(f"Logged Message: '{msg}'")
                if msg == "/reset":
                    sock.close()
                    break
                elif ((msg == "/disconnect") or (msg == "/exit")):
                    sock.close()
                    driver.quit()
                    loop = False
                    break
                else:
                    driver.sendMessage(msg)

        except Exception as e:
            try:
                sock.send(b'*')
                sock.close()
            except:
                pass
            print(f"Error Encountered: '{e}'.")
            continue
