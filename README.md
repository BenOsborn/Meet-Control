# Meet-Control
By Ben Osborn

A python program which lets users remote control someone else's Google Meet without the need for their email or password.

This app was built for a friend to help her avoid getting in trouble for the times when she was unable to join Google Meet online classes. It features a peer to peer connection where the controlled user logs into their Google account on their end which means the need to send a username and password to another machine is not needed. From there the controlling machine can join Google Meet sessions and type in the chat on behalf of the controlled user. The controlled user gets a log in the console of all of the things that the controller sent on behalf of them. 

It is built using Python and Selenium using Python sockets for the networking component, and was compiled using the Python pyinstaller module.

# Instructions
1. Download or clone the repository to your computer.
2. Delete the "source" folder so you are just left with the "executable" folder.
3. Open the "executable" folder and find "clientmain.exe".
4. For best results run this "clientmain.exe" in a command prompt window, otherwise it can just be run as a normal exe, however you will lose the logged messages on disconnect.
5. Follow the apps instructions.
