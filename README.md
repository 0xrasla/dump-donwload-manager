# dump-download-manager

A simple and clean download manager built around aria2c for efficient file downloads.

## Features

- Utilizes aria2c for high-speed, multi-protocol downloads.
- Supports RPC for remote control.

## Installation

1. Install aria2c on your system.
2. Clone this repository: `git clone https://github.com/yourusername/dump-download-manager.git`
3. Run the manager script.

## Usage

Start aria2c with RPC enabled:

```
aria2c --enable-rpc --rpc-listen-all=true --rpc-allow-origin-all
```

Then, use the manager to handle downloads.

## License

MIT
