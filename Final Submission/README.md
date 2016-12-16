# Capstone Files for Final Presentation, December 16th, 2016

### Kadar Anwar, Devon Richards

* This folder contains the files necessary to establish a websocket connection between a client web browser and the web socket server.

* The web socket server is initiated by use of the *websocketd* daemon, which is a UNIX-style daemon for initiating a websocket server.

	* *websocketd* is able to serve the contents of a file, such as a Python script, using the Websocket protocol.

* Extract the contents of the *websocketd-0.2.11-linux_amd64.zip* file.
* Make the Python file executable with *chmod +X filename.py*
* Navigate to the newly unzipped directory and issue *./websocketd --port=### ./path/to/file.py*
* Access the *index.html* file, either hosted locally or remotely.
* **Please note**: You may need to change IP addresses to reflect your network topology.
