FROM debian:bullseye-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    make \
    xxd \
    libc6-dev \
    sudo \
    build-essential \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Create a new user and set password
RUN useradd -m -s /bin/bash user && echo "user:ad&*din3rtUF3wsft732" | chpasswd

# Ensure /home/user exists, then set permissions (read/execute only, no write)
RUN mkdir -p /home/user && chmod 555 /home/user && chown user:user /home/user

# Add files for root user
RUN echo -n "RkxBR3tiMW5hcjEzNV80bmRfc3R1ZmZ9Cg==" | base64 -d > /root/flag.txt
COPY message.txt /root/message.txt

# Add files for user
COPY vuln /home/user/vuln
RUN chmod +x /home/user/vuln

# Set SUID on the vulnerable program (if required)
RUN chown root:root /home/user/vuln && chmod +s /home/user/vuln

WORKDIR /home/user
USER user

CMD ["/bin/bash"]


