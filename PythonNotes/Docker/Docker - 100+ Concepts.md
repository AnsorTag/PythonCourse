#docker

**Video Link**: [Watch on YouTube](https://www.youtube.com/watch/rIrNIzy6U_g)

---
## 🔍 Introduction

**Goal**: Ship software in the real world? One powerful tool to understand is **Containerization**! 🛠️

- **Local Development**: Solves the problem of “It works on my machine! 🖥️”
- **Cloud Deployment**: Solves scalability issues with architecture. ☁️

Let’s dive into 101 concepts about **Docker**, **Computer Science**, and **the Cloud**.

---

## 🖥️ Computer Basics

- **A computer**: 
  - CPU 💻: For calculations.
  - RAM 🧠: For currently running applications.
  - Disk 💽: To store things for later use.

- **Bare metal** 🧱: The hardware itself. But to use it, you need an **Operating System (OS)**, which includes a **Kernel**.

---

## 🌍 Networking

- When you watch a YouTube video 🎥, your computer is a **Client**, and the server providing the video is a **Remote Computer**.
- Issues when scaling for millions of users:
  - **CPU Overload** 🧑‍💻
  - **Disk I/O Slowdowns** 🐌
  - **Network Bandwidth Maxed Out** 🌐
  - **Database Query Inefficiency** 📊

---

## 📈 Scaling Infrastructure

### Two types of scaling:
1. **Vertical Scaling** 🏗️: Increase CPU and RAM of a single server.
2. **Horizontal Scaling** 🏢: Use multiple servers (often **Microservices**) to scale independently.

- Problems with scaling on **bare metal**:
  - Resource allocation varies, and it’s not practical.

---

## 🖥️ Virtual Machines (VMs) vs. Docker 🐋

- **VMs**: Allow running multiple OS on one machine using tools like **Hypervisors**.
- **Docker**: Efficiently uses resources dynamically, unlike VMs, where resource allocation is fixed.

---

## 🔑 Key Docker Concepts

- **Docker Engine**: Manages **OS-level virtualization** and allows multiple apps to share the same host OS.
- **Docker Desktop**: Easy setup for developers without needing big changes to your local system.

---

## 🛠️ How Docker Works

1. **Dockerfile** 📄: The blueprint for configuring your environment.
2. **Image** 🖼️: Built from the Dockerfile and contains OS, dependencies, and your code.
3. **Container** 📦: The isolated package running your application, which can scale infinitely in the cloud.

---

## 🔐 Dockerfile Breakdown

- **FROM**: Specifies the base image, e.g., Linux distro.
- **WORKDIR**: Sets up a working directory for your source code.
- **RUN**: Executes commands like installing dependencies using a Linux package manager.
- **COPY**: Copies code from your local machine into the image.
- **ENV**: Sets environment variables like API keys.
- **EXPOSE**: Opens a port for external traffic (e.g., for a web server).
- **CMD**: The main command that runs when the container starts. ⚡

---

## 🧑‍💻 Building and Running Docker Images

- **Docker Build** 🏗️: Turns your Dockerfile into an image. 
  - Use the `-t` flag to tag the image with a recognizable name.
  - Images are built in **layers** (identified by a **SHA-256 hash**), and Docker caches layers to only rebuild what’s changed. 🧩
  
- **Docker Ignore File** 📝: Specifies files that should be excluded from the image build.

---

## 🔍 Running a Container

- **Docker Run** 🚀: Spins up a container from the image.
- **Docker Desktop**: 
  - Shows running containers.
  - Logs and file systems can be inspected.
  - Commands can be executed directly inside the running container. 🛠️

### Stopping Containers:
- **Docker Stop**: Gracefully stops a container. 🛑
- **Docker Kill**: Force stops a container. 💥
- **Docker Remove**: Deletes the container when you're done.

---

## ☁️ Pushing to the Cloud

- **Docker Push** 📤: Uploads your image to a remote registry (e.g., Docker Hub) to run in the cloud (e.g., AWS).
  
---

## 🔒 Security with Docker Scout

- **Docker Scout**: Scans images for **security vulnerabilities** based on the Software Bill of Materials (SBOM) and compares it to security databases.
  - Prioritize vulnerabilities based on their **severity**. 🚨

---

## ✅ Final Tips

1. **Build** and **Run** containers often to practice and optimize.
2. Remember to monitor for security vulnerabilities.
3. Use **Docker Desktop** to visually manage your images and containers!