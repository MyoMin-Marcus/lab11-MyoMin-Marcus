# Intermediate programming practice: async and sockets.
#
# For EACH problem, work out your problem-solving OUTLINE first, then implement it (you
# may use an AI assistant to help - see the README). The async parts must actually run
# their work CONCURRENTLY (that's the whole point), not one after another.
#
# Do not rename the functions - the tests use these names.

import asyncio
import socket


async def gather_doubled(numbers):
    # Outline (write your plan here first): async function that takes a list of numbers, creates an async task for each number to double it, 
    # and gathers the results concurrently.
    #   ...
    # TODO (Part 1, async): run one async task per number that returns n * 2, all
    #   CONCURRENTLY with asyncio.gather, and return the results as a list in the same
    #   order as `numbers`.
    async def double(n):
        return n * 2
    return await asyncio.gather(*[double(n) for n in numbers])


async def fastest(jobs):
    # Outline: each job is an async function that sleeps for the given delay and returns its label. Use asyncio.as_completed to get the first completed job.
    #   ...
    # TODO (Part 2, async): `jobs` is a list of (label, delay) pairs. Start them all
    #   concurrently - each one just does `await asyncio.sleep(delay)` - and return the
    #   label of the FIRST job to finish. (Hint: asyncio.as_completed.)
    async def job(label, delay):
        await asyncio.sleep(delay)
        return label

    tasks = [job(label, delay) for label, delay in jobs]
    for task in asyncio.as_completed(tasks):
        return await task


def echo_once(host, port, message):
    # Outline: open a TCP socket, connect to the given host and port, send the message, receive the reply, and return it as a string.
    #   ...
    # TODO (Part 3, sockets): open a TCP socket and connect to (host, port). Send
    #   `message` (encode it to bytes first), receive the server's reply, and return it
    #   as a string. (Hint: socket.socket, .connect, .sendall, .recv, .decode.)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(message.encode())
        reply = s.recv(1024)
    return reply.decode()

def main():
    # Optional scratch space - try the async parts here, e.g.:
    # print(asyncio.run(gather_doubled([1, 2, 3, 4])))   # [2, 4, 6, 8]
    pass


if __name__ == "__main__":
    main()
    asyncio.run(gather_doubled([1, 2, 3, 4]))   # returns [2, 4, 6, 8]
    asyncio.run(fastest([("A", 0.06), ("B", 0.02), ("C", 0.04)]))   # returns "B"
    echo_once("127.0.0.1", 50011, "hello")   # returns "hello"   (against an echo server)
