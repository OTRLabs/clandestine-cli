FROM nixos/nix:latest

# Set up the necessary environment variables
ENV LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    NIX_PATH=nixpkgs=/nix/var/nix/profiles/per-user/root/channels/nixos:nixos-config=/etc/nixos/configuration.nix

# Copy the NixOS configuration file into the container
COPY configuration.nix /etc/nixos/configuration.nix

# Install the necessary packages
RUN nix-env -iA nixos.nixUnstable

# Generate the NixOS system configuration
RUN nixos-rebuild switch

# Expose any necessary ports

# Set the entrypoint command
CMD ["/usr/bin/env", "bash"]