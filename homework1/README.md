# CDP - Homework 1

The project is split in two "components": the `client`, and the `server`. The goal of this application
is to send large amounts of data (~1GB of photos) from client to server through network.

The project implements two types of communication: TCP (the code can be viewed in the `TCPClient` and `TCPServer`),
and UDP (`UDPClient` and `UDPServer`). Also, you can use two types of mechanisms for sending message: `STREAMING`, which will
stream byte messages without awaiting acknowledge, and `STOP_AND_WAIT` which will require acknowledge
before sending the next package.

Once running `server/server.py`, you'll be asked which type of communication and the transmission mechanism. Same happens for
`client/client.py`.

You can view the outcome of runs in the [tests.txt](./tests.txt) file.

Note: The image dataset used in the test can be found on [Kaggle](https://www.kaggle.com/datasets/pavansanagapati/images-dataset), and the pictures must be placed in
the `client/data` directory.