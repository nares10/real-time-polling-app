# Real-Time Polling App

The Real-Time Polling App is a simple application that allows users to participate in a real-time poll over WebSocket connections. This project demonstrates the implementation of WebSocket communication for real-time interactions between clients and a server.

## Features

- **WebSocket Communication**: Utilizes WebSocket protocol for two-way communication between clients and server.
- **Real-Time Updates**: Poll data is updated in real-time, enabling users to see immediate changes.
- **Simple CLI Interface**: Provides a command-line interface for clients to interact with the poll.

## Getting Started

### Prerequisites

- Python 3.x
- `websockets` library (install via `pip install websockets`)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/real-time-polling-app.git
    ```

2. Navigate to the project directory:

    ```bash
    cd real-time-polling-app
    ```

### Running the Application

1. Start the WebSocket server:

    ```bash
    cd server
    python app.py
    ```

2. Start the WebSocket client:

    ```bash
    cd ../client
    python client.py
    ```

3. Interact with the poll using the client's command-line interface.

## Usage

- Upon connecting to the server, the client will receive the initial poll data.
- Clients can vote for their preferred options by selecting the corresponding option number.
- The poll data is updated in real-time, and clients receive updated poll information automatically.

## File Structure

```
real-time-polling-app/
│
├── server/
│   └── app.py               # WebSocket server implementation
│
└── client/
    └── client.py            # WebSocket client implementation
```

## Contributing

Contributions are welcome! Feel free to open issues or pull requests for any improvements or features you'd like to see added to the project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [websockets](https://websockets.readthedocs.io/en/stable/) - Python library for WebSocket communication.
- [Python Documentation](https://docs.python.org/3/) - Official documentation for the Python programming language.

---

Feel free to customize this README file with additional information specific to your project, such as usage examples, troubleshooting tips, or deployment instructions.
