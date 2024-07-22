FROM nixos/nix:latest

# Set up SSH
RUN nix-env -iA nixos.openssh
RUN mkdir /run/sshd
RUN echo 'root:password' | chpasswd
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -i 's/#Port 22/Port 2222/' /etc/ssh/sshd_config

# Expose port 2222 for SSH
EXPOSE 2222

# Start SSH daemon
CMD ["/usr/sbin/sshd", "-D"]