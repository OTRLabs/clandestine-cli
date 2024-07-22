# Offensive Security Kubernetes Framework

## Introduction

The Offensive Security Kubernetes Framework is a Kubernetes distribution designed specifically for offensive security operations. This framework focuses on operational security and operator anonymity, providing a robust and isolated environment for conducting various security tasks.

## Objective

The objective of this project is to create a highly configurable and isolated environment for offensive security operations, combining the capabilities of Kubernetes with the flexibility of virtual clusters and containers.

## Components

The framework leverages the following components:

- **Debian**: Base operating system for all machines.
- **Kubeadm**: Tool to set up the Kubernetes cluster.
- **SurrealDB**: Handles system wide information & knowledge management. 
- **VCluster**: Inspired by [loft-sh/vcluster](https://github.com/loft-sh/vcluster), used for creating virtual clusters.
- **Vagrant**: For managing virtual machines.
- **Docker, Podman, and Containerd**: Container runtimes based on requirements.
- **Nix**: Package manager for containers to ensure high levels of isolation and configurability.

## Architecture

The architecture is designed to provide a flexible and secure environment for offensive security operations. The design is based off of `Kubeadm` as it looks like the `K8s` distribution with the least amount of preset configs, & general bloat. Our goal is to provide a system that is as close to a clean slate as possible, allowing you to build your multiverse of environments as you see fit.

> Do you want to use a virtual machine for that service or will containers do? Which container runtime do you want to use? Up to you! 
>

### Multiverse Theory: Dividing the Cluster into Virtual Clusters

Think of each instance of Kali Linux as a planet. In this framework, we are creating a "multiverse" of environments, where the Kubernetes cluster acts as the multiverse.

### The "Multiverse" Architecture

#### Kubeadm Cluster: The "Multiverse"

The Kubernetes cluster is the foundation of the multiverse, providing the infrastructure to support multiple isolated environments.

#### Virtual Clusters

Virtual clusters are isolated environments within the main Kubernetes cluster, each serving specific purposes. They offer better multi-tenancy and isolation than regular namespaces.

**Templates for Virtual Clusters**:
- *Attack Cluster Template*


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
- Vagrant for managing virtual machines?
- Docker, Podman, or Containerd installed based on requirements.
- Nix package manager installed within containers.



### Example Use Cases

- **Launching a Phishing Campaign**:
  Set up the Phishing Cluster and deploy phishing infrastructure.

- **Conducting Network Reconnaissance**:
  Use the Network Recon Cluster to gather information on target networks.

## Conclusion

The Offensive Security Kubernetes Framework provides a versatile and secure environment for conducting offensive security operations. By leveraging Kubernetes, virtual clusters, and containers, this framework offers unparalleled flexibility and isolation. For more detailed instructions and advanced configurations, refer to the respective documentation links provided.



# framework
experimental port of msf from Ruby to Python lol


## Outline
My original goal was to do a complete rewrite of the [Metasploit Framework](https://metasploit.com), primarily [msfconsole] from `Ruby` to [Python](https://python.org). I wanted to do this because I wanted to learn more about exploit development & the typical structure of a framework like Metasploit. I also wanted to take advantage of the `Python` ecosystem.


Now, my goals have shifted & there are some additional features I would like to add to this project.


First and foremost, we want to write this in python using statically typed annotations. This will allow for better code completion & error checking. We will also use [Black](https://black.readthedocs.io/en/stable/) for code formatting. We are using `pdm` as our package manager. We are using `pytest` for testing. We are using `mypy` for static type checking. 

The base application is a [Rich](https://github.com/Textualize/rich) based `cli application`.

I would like to add a `REST API` to this project. This would allow for easier integration with other tools & services. For this we will use [Litestar](https://litestar.dev/), formerly known as `Starlite`.

Eventually I would also like to add a `Web UI` to this project. This would allow for easier use of the framework for those who are not comfortable with the command line, however this is a lower priority than the `REST API` & the `cli app`.

In addition, I would like to add an `AI` based `exploit development` system, which uses a wide variety of information to develop modules for the framework. This is a long term goal & will require a lot of research & development, but if you are interested it can be monitored... i will move that to the organization repo later.

