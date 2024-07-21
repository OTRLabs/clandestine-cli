# Offensive Security Kubernetes Framework

## Introduction

The Offensive Security Kubernetes Framework is a Kubernetes distribution designed specifically for offensive security operations. This framework focuses on operational security and operator anonymity, providing a robust and isolated environment for conducting various security tasks.

## Objective

The objective of this project is to create a highly configurable and isolated environment for offensive security operations, combining the capabilities of Kubernetes with the flexibility of virtual clusters and containers.

## Components

The framework leverages the following components:

- **Debian**: Base operating system for all machines.
- **Kubeadm**: Tool to set up the Kubernetes cluster.
- **VCluster**: Inspired by [loft-sh/vcluster](https://github.com/loft-sh/vcluster), used for creating virtual clusters.
- **Vagrant**: For managing virtual machines.
- **Docker, Podman, and Containerd**: Container runtimes based on requirements.
- **Nix**: Package manager for containers to ensure high levels of isolation and configurability.

## Architecture

The architecture is designed to provide a flexible and secure environment for offensive security operations.

### Multiverse Theory: Dividing the Cluster into Virtual Clusters

Think of each instance of Kali Linux as a planet. In this framework, we are creating a "multiverse" of environments, where the Kubernetes cluster acts as the multiverse.

#### Kubeadm Cluster: The "Multiverse"

The Kubernetes cluster is the foundation of the multiverse, providing the infrastructure to support multiple isolated environments.

#### Virtual Clusters

Virtual clusters are isolated environments within the main Kubernetes cluster, each serving specific purposes. They offer better multi-tenancy and isolation than regular namespaces.

**Persistent Clusters**: Designed to be protected, isolated, and maintained for long periods.
- [Admin Cluster](docs/vclusters/Admin-Cluster.md)
- [AI Cluster](docs/vclusters/AI-Cluster.md)
- [Data Cluster](docs/vclusters/Data-Cluster.md)

**Temporary / Rotated Periodically Clusters**: These clusters are destroyed and recreated at set intervals to ensure up-to-date infrastructure and configurations.
- [Barrier Cluster](docs/vclusters/Barrier-Cluster.md)
- [DMZ Cluster](docs/vclusters/DMZ-Cluster.md)
- [Jump Cluster](docs/vclusters/Jump-Cluster.md)
- [UI Cluster](docs/vclusters/UI-Cluster.md)

**Rapidly Disposable Clusters**: These clusters are created and destroyed as needed for specific tasks.
- [Phishing Cluster](docs/vclusters/Phishing-Cluster.md)
- [Attack Cluster](docs/vclusters/Attack-Cluster.md)
- [C2 Cluster](docs/vclusters/C2-Cluster.md)
- [Network Recon Cluster](docs/vclusters/Recon-Cluster.md)
- [Exploit Cluster](docs/vclusters/Exploit-Cluster.md)
- [Monitoring Cluster](docs/vclusters/Monitoring-Cluster.md)

## Installation & Setup

### Prerequisites

- Debian OS installed on all machines.
- Kubeadm installed for setting up the Kubernetes cluster.
- Vagrant for managing virtual machines.
- Docker, Podman, or Containerd installed based on requirements.
- Nix package manager installed within containers.



### Example Use Cases

- **Launching a Phishing Campaign**:
  Set up the Phishing Cluster and deploy phishing infrastructure.

- **Conducting Network Reconnaissance**:
  Use the Network Recon Cluster to gather information on target networks.

## Conclusion

The Offensive Security Kubernetes Framework provides a versatile and secure environment for conducting offensive security operations. By leveraging Kubernetes, virtual clusters, and containers, this framework offers unparalleled flexibility and isolation. For more detailed instructions and advanced configurations, refer to the respective documentation links provided.