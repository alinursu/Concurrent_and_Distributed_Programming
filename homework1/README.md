# CDP - Homework 1

The project is split in two "components": the `client`, and the `server`. The goal of this application
is to send large amounts of data (~1.1GB of photos) from client to server through network.

The project implements two types of communication: TCP (the code can be viewed in the `TCPClient` and `TCPServer`),
and UDP (`UDPClient` and `UDPServer`). Also, you can use two types of mechanisms for sending message: `STREAMING`, which will
stream byte messages without awaiting acknowledge, and `STOP_AND_WAIT` which will require acknowledge
before sending the next package.

Once running `server/server.py`, you'll be asked which type of communication and the transmission mechanism. Same happens for
`client/client.py`. The client will then start sending each image in parts of pre-defined message size (which needs to be
a power of `2`).

Note: The image dataset used in the test can be found on [Kaggle](https://www.kaggle.com/datasets/pavansanagapati/images-dataset), and the pictures must be placed in
the `client/data` directory.

### Testing on local network

Both the client and the server ran on the same Linux Virtual Machine instance, as two different processes.

Sending the images through the `TCP` protocol, using the `STREAMING` mechanism:

| Message (package) size, in bytes | # of messages sent | # of messages received | % of loss on messages | Total bytes sent | Total bytes received | % of loss on bytes | Time     |
|----------------------------------|--------------------|------------------------|-----------------------|------------------|----------------------|--------------------|----------|
| 2048                             | 1127784            | 1127784                | 0                     | 1152349321       | 1152349321           | 0                  | 00:08:40 |
| 4096                             | 565738             | 565738                 | 0                     | 1151787275       | 1151787275           | 0                  | 00:02:53 |
| 8192                             | 283510             | 283510                 | 0                     | 1151505047       | 1151505047           | 0                  | 00:01:27 |
| 16384                            | 143544             | 143544                 | 0                     | 1151365081       | 1151365081           | 0                  | 00:00:42 |
| 32768                            | 73586              | 73586                  | 0                     | 1151295123       | 1151295123           | 0                  | 00:00:22 |

Sending the images through the `TCP` protocol, using the `STOP_AND_WAIT` mechanism:

| Message (package) size, in bytes | # of messages sent | # of messages received | % of loss on messages | Total bytes sent | Total bytes received | % of loss on bytes | Time     |
|----------------------------------|--------------------|------------------------|-----------------------|------------------|----------------------|--------------------|----------|
| 2048                             | 1127784            | 1127784                | 0                     | 1152349321       | 1152349321           | 0                  | 00:09:29 |
| 4096                             | 565738             | 565738                 | 0                     | 1151787275       | 1151787275           | 0                  | 00:03:26 |
| 8192                             | 283510             | 283510                 | 0                     | 1151505047       | 1151505047           | 0                  | 00:01:46 |
| 16384                            | 143544             | 143544                 | 0                     | 1151365081       | 1151365081           | 0                  | 00:00:52 |
| 32768                            | 73586              | 73586                  | 0                     | 1151295123       | 1151295123           | 0                  | 00:00:26 |

Sending the images through the `UDP` protocol, using the `STREAMING` mechanism:

| Message (package) size, in bytes | # of messages sent | # of messages received | % of loss on messages | Total bytes sent | Total bytes received | % of loss on bytes | Time     |
|----------------------------------|--------------------|------------------------|-----------------------|------------------|----------------------|--------------------|----------|
| 2048                             | 1127784            | 1127781                | 0.00002               | 1152349321       | 1152345223           | 0.00003            | 00:07:20 |
| 4096                             | 565738             | 565738                 | 0                     | 1151787275       | 1151787275           | 0                  | 00:02:53 |
| 8192                             | 283510             | 283488                 | 0.007                 | 1151505047       | 1151406723           | 0.008              | 00:01:26 |
| 16384                            | 143544             | 143537                 | 0.004                 | 1151365081       | 1151299539           | 0.005              | 00:00:40 |
| 32768                            | 73586              | 73586                  | 0                     | 1151295123       | 1151295123           | 0                  | 00:00:22 |

Sending the images through the `UDP` protocol, using the `STOP_AND_WAIT` mechanism:

| Message (package) size, in bytes | # of messages sent | # of messages received | % of loss on messages | Total bytes sent | Total bytes received | % of loss on bytes | Time     |
|----------------------------------|--------------------|------------------------|-----------------------|------------------|----------------------|--------------------|----------|
| 2048                             | 1127784            | 1127784                | 0                     | 1152349321       | 1152349321           | 0                  | 00:07:48 |
| 4096                             | 565738             | 565738                 | 0                     | 1151787275       | 1151787275           | 0                  | 00:03:29 |
| 8192                             | 283506             | 283506                 | 0                     | 1151505047       | 1151505047           | 0                  | 00:01:43 |
| 16384                            | 143544             | 143544                 | 0                     | 1151365081       | 1151365081           | 0                  | 00:00:51 |
| 32768                            | 73586              | 73586                  | 0                     | 1151295123       | 1151295123           | 0                  | 00:00:26 |

### Testing on Cloud

Each part of the application (client and server) was deployed to a different AWS EC2 instance, having the same configuration:
- Running on Amazon AMI Linux 2
- Having the `t2.micro` instance type
- Having 8GB of internal memory

#### Two instances on the same AWS Region

Both the client and the server's instances were run on the Frankfurt AWS region (`eu-central-1`). Even so, due to the fact
that AWS Regions consist of 2 to 6 Availability Zones (data centers) which have their own networking, we can say
that the client and the server didn't run on the same infrastructure.

Sending the images through the `TCP` protocol, using the `STREAMING` mechanism:

| Message (package) size, in bytes | # of messages sent | # of messages received | % of loss on messages | Total bytes sent | Total bytes received | % of loss on bytes | Time     |
|----------------------------------|--------------------|------------------------|-----------------------|------------------|----------------------|--------------------|----------|
| 2048                             | 1127784            | 1859420                | 0                     | 1152349321       | 1152349321           | 0                  | 00:02:41 |
| 4096                             | 565738             | 812697                 | 0                     | 1151787275       | 1151787275           | 0                  | 00:01:24 |
| 8192                             | 283510             | 431794                 | 0                     | 1151505047       | 1151505047           | 0                  | 00:00:45 |
| 16384                            | 143544             | 263061                 | 0                     | 1151365081       | 1151365081           | 0                  | 00:00:25 |
| 32768                            | 73586              | 165068                 | 0                     | 1151295123       | 1151295123           | 0                  | 00:00:18 |

Sending the images through the `TCP` protocol, using the `STOP_AND_WAIT` mechanism:

| Message (package) size, in bytes | # of messages sent | # of messages received | % of loss on messages | Total bytes sent | Total bytes received | % of loss on bytes | Time     |
|----------------------------------|--------------------|------------------------|-----------------------|------------------|----------------------|--------------------|----------|
| 2048                             | 1127784            | 1127794                | 0                     | 1152349321       | 1152349321           | 0                  | 00:03:06 |
| 4096                             | 565738             | 566695                 | 0                     | 1151787275       | 1151787275           | 0                  | 00:01:55 |
| 8192                             | 283510             | 284439                 | 0                     | 1151505047       | 1151505047           | 0                  | 00:00:56 |
| 16384                            | 143544             | 147315                 | 0                     | 1151365081       | 1151365081           | 0                  | 00:00:29 |
| 32768                            | 73586              | 97425                  | 0                     | 1151295123       | 1151295123           | 0                  | 00:00:18 |

Sending the images through the `UDP` protocol, using the `STREAMING` mechanism:

| Message (package) size, in bytes | # of messages sent | # of messages received | % of loss on messages | Total bytes sent | Total bytes received | % of loss on bytes | Time     |
|----------------------------------|--------------------|------------------------|-----------------------|------------------|----------------------|--------------------|----------|
| 2048                             | 1127784            | 1127581                | 0.018                 | 1152349321       | 1151352513           | 0.086              | 00:02:46 |
| 4096                             | 565738             | 565501                 | 0.042                 | 1151787275       | 1150063175           | 0.149              | 00:01:27 |
| 8192                             | 283510             | 283399                 | 0.039                 | 1151505047       | 1136852013           | 1.272              | 00:00:56 |
| 16384                            | 143544             | 143518                 | 0.018                 | 1151365081       | 1150340366           | 0.089              | 00:00:29 |
| 32768                            | 73586              | 73244                  | 0.464                 | 1151295123       | 1129858007           | 1.862              | 00:00:17 |

Sending the images through the `UDP` protocol, using the `STOP_AND_WAIT` mechanism:

| Message (package) size, in bytes | # of messages sent | # of messages received | % of loss on messages | Total bytes sent | Total bytes received | % of loss on bytes | Time     |
|----------------------------------|--------------------|------------------------|-----------------------|------------------|----------------------|--------------------|----------|
| 2048                             | 1127784            | 1127784                | 0                     | 1152349321       | 1152349321           | 0                  | 00:09:28 |
| 4096                             | 565738             | 565738                 | 0                     | 1151787275       | 1151787275           | 0                  | 00:04:18 |
| 8192                             | 283506             | 283506                 | 0                     | 1151505047       | 1151505047           | 0                  | 00:02:24 |
| 16384                            | 143544             | 143544                 | 0                     | 1151365081       | 1151365081           | 0                  | 00:01:36 |
| 32768                            | 73586              | 73586                  | 0                     | 1151295123       | 1151295123           | 0                  | 00:01:03 |

#### Two instances on different AWS Region

The client's instance ran on the Frankfurt AWS region (`eu-central-1`), while the server's instance ran on the 
Paris region (`eu-west-3`).

Sending the images through the `TCP` protocol, using the `STREAMING` mechanism:

| Message (package) size, in bytes | # of messages sent | # of messages received | % of loss on messages | Total bytes sent | Total bytes received | % of loss on bytes | Time     |
|----------------------------------|--------------------|------------------------|-----------------------|------------------|----------------------|--------------------|----------|
| 2048                             | 1127784            | 1167535                | 0                     | 1152349321       | 1152349321           | 0                  | 00:02:40 |
| 4096                             | 565738             | 612805                 | 0                     | 1151787275       | 1151787275           | 0                  | 00:01:23 |
| 8192                             | 283510             | 383171                 | 0                     | 1151505047       | 1151505047           | 0                  | 00:00:45 |
| 16384                            | 143544             | 205397                 | 0                     | 1151365081       | 1151365081           | 0                  | 00:00:27 |
| 32768                            | 73586              | 156167                 | 0                     | 1151295123       | 1151295123           | 0                  | 00:00:23 |

Sending the images through the `TCP` protocol, using the `STOP_AND_WAIT` mechanism:

| Message (package) size, in bytes | # of messages sent | # of messages received | % of loss on messages | Total bytes sent | Total bytes received | % of loss on bytes | Time     |
|----------------------------------|--------------------|------------------------|-----------------------|------------------|----------------------|--------------------|----------|
| 2048                             | 1127784            | 1186541                | 0                     | 1152349321       | 1152349321           | 0                  | 00:08:43 |
| 4096                             | 565738             | 663865                 | 0                     | 1151787275       | 1151787275           | 0                  | 00:05:12 |
| 8192                             | 283510             | 361021                 | 0                     | 1151505047       | 1151505047           | 0                  | 00:02:34 |
| 16384                            | 143544             | 156653                 | 0                     | 1151365081       | 1151365081           | 0                  | 00:01:12 |
| 32768                            | 73586              | 112870                 | 0                     | 1151295123       | 1151295123           | 0                  | 00:00:28 |

Sending the images through the `UDP` protocol, using the `STREAMING` mechanism:

| Message (package) size, in bytes | # of messages sent | # of messages received | % of loss on messages | Total bytes sent | Total bytes received | % of loss on bytes | Time     |
|----------------------------------|--------------------|------------------------|-----------------------|------------------|----------------------|--------------------|----------|
| 2048                             | 1127784            | 1127740                | 0.0003                | 1152349321       | 1147356989           | 0.433              | 00:02:46 |
| 4096                             | 565738             | 565688                 | 0.008                 | 1151787275       | 1146278561           | 0.478              | 00:01:26 |
| 8192                             | 283510             | 283450                 | 0.021                 | 1151505047       | 1146666881           | 0.420              | 00:00:45 |
| 16384                            | 143544             | 138441                 | 3.555                 | 1151365081       | 1067994735           | 7.241              | 00:00:24 |
| 32768                            | 73586              | 73472                  | 0.154                 | 1151295123       | 1143400727           | 0.685              | 00:00:26 |

Sending the images through the `UDP` protocol, using the `STOP_AND_WAIT` mechanism:

| Message (package) size, in bytes | # of messages sent | # of messages received | % of loss on messages | Total bytes sent | Total bytes received | % of loss on bytes | Time     |
|----------------------------------|--------------------|------------------------|-----------------------|------------------|----------------------|--------------------|----------|
| 2048                             | 1127784            | 1127784                | 0                     | 1152349321       | 1152349321           | 0                  | 00:11:19 |
| 4096                             | 565738             | 565738                 | 0                     | 1151787275       | 1151787275           | 0                  | 00:06:27 |
| 8192                             | 283506             | 283506                 | 0                     | 1151505047       | 1151505047           | 0                  | 00:04:09 |
| 16384                            | 143544             | 143544                 | 0                     | 1151365081       | 1151365081           | 0                  | 00:02:32 |
| 32768                            | 73586              | 73586                  | 0                     | 1151295123       | 1151295123           | 0                  | 00:01:48 |
