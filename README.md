# Kafka Mouse Tracker

A simple project for studying Apache Kafka, demonstrating real-time mouse position tracking. The producer captures mouse movements and sends coordinates to a Kafka topic, while the consumer reads these events and draws connecting lines on a canvas in real-time, creating a "digital paint" effect.

## Table of Contents

- [Kafka Mouse Tracker](#kafka-mouse-tracker)
  - [Table of Contents](#table-of-contents)
  - [How It Works](#how-it-works)
  - [Architecture](#architecture)
  - [Technologies](#technologies)
  - [Prerequisites](#prerequisites)
  - [Setup](#setup)
    - [1. Clone the Repository](#1-clone-the-repository)
    - [2. Install Python Dependencies](#2-install-python-dependencies)
    - [3. Create Environment File](#3-create-environment-file)
    - [4. Start Kafka with Docker](#4-start-kafka-with-docker)
  - [Running the Project](#running-the-project)
    - [Producer (Mouse Capture)](#producer-mouse-capture)
    - [Consumer (Real-Time Drawing)](#consumer-real-time-drawing)
  - [Result](#result)
  - [Optimizations](#optimizations)
  - [Important Notes](#important-notes)
  - [Learning Objectives](#learning-objectives)

## How It Works

1. The **producer** continuously captures the mouse position using `pynput`.
2. Sends the `(x, y)` coordinates as messages to a Kafka topic.
3. The **consumer** subscribes to the topic and reads incoming messages.
4. Parses the coordinates and draws lines connecting consecutive points on a Tkinter canvas.

## Architecture

```
Mouse → Producer → Kafka Broker → Consumer → Tkinter Canvas
```

- **Producer**: Captures mouse events and publishes to Kafka.
- **Kafka**: Acts as the message broker for event streaming.
- **Consumer**: Subscribes to the topic and updates the GUI.

## Technologies

- **Python 3.11+**: Core programming language.
- **Apache Kafka**: Distributed event streaming platform.
- **Docker & Docker Compose**: Containerization for Kafka setup.
- **Tkinter**: Built-in Python GUI library for drawing.
- **pynput**: Library for monitoring mouse and keyboard input.

## Prerequisites

- Python 3.11 or higher installed locally.
- Docker and Docker Compose installed.
- Basic knowledge of Kafka concepts (topics, producers, consumers).

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/ThiagoCanatoAzevedo/kafka-study.git
cd kafka-study
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 3. Create Environment File

Create a `.env` file in the project root with the following content:

```env
SERVER=localhost:9092
TOPIC=mouse_positions
```

### 4. Start Kafka with Docker

```bash
docker compose up --build
```

This will start Kafka and Zookeeper. The Kafka UI will be available at [http://localhost:8080](http://localhost:8080) for monitoring topics and messages.

## Running the Project

### Producer (Mouse Capture)

Run the producer to start capturing mouse positions:

```bash
python get_positions.py
```

This will begin sending mouse coordinates to the Kafka topic.

### Consumer (Real-Time Drawing)

In a separate terminal, run the consumer to visualize the drawing:

```bash
python draw_lines.py
```

The Tkinter window will open and start drawing lines based on the mouse movements captured by the producer.

## Result

- Move your mouse around while both producer and consumer are running.
- Lines will be drawn in real-time on the canvas, connecting the points as you move.
- Higher event frequency results in smoother, more continuous lines.

## Optimizations

- **Asynchronous Sending**: Uses non-blocking message production to avoid UI lag.
- **High Frequency Events**: Captures ~100 mouse events per second for smooth tracking.
- **Threaded Consumer**: Runs Kafka consumption in a separate thread to prevent GUI freezing.
- **Queue Buffering**: Uses a queue for efficient message processing.
- **Incremental Drawing**: Draws lines between consecutive points for better performance.

## Important Notes

- Tkinter requires a graphical environment and doesn't work well inside Docker containers.
- Both producer and consumer must run on the local machine (not in containers).
- Kafka runs in Docker as expected.
- Ensure the `.env` file is correctly configured before starting.
- If you encounter permission issues with Docker, you may need to run commands with `sudo`.

## Learning Objectives

This project helps practice key concepts in event-driven systems:

- Event-driven architecture
- Asynchronous communication patterns
- Real-time data streaming
- Kafka integration and message brokering
- GUI programming with threading
- Containerized service orchestration
