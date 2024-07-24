FROM nixos/nix:latest

# Install OpenSSH server
RUN nix-env -iA nixos.openssh

# Set SSH port to 2222
RUN echo "Port 2222" >> /etc/ssh/sshd_config

# Generate SSH host keys
RUN ssh-keygen -A

# Create a user for SSH access
RUN useradd -m -s /bin/bash sshuser
RUN echo "sshuser:password" | chpasswd

# Expose SSH port
EXPOSE 2222

# Start SSH server
CMD ["/usr/sbin/sshd", "-D"]