

# Refactoring + reassessment of our approach

this system is going to shift it’s focus from being a metasploit ripoff, to being a Kubernetes distribution designed specifically for offensive security with a focus on operational security and operator anonymity 

The system is based on kubeadm & designed to use virtual clusters in addition to virtual machines & containers

We will be using Nix as our package manager within the containers. 

This allows us to achieve  an almost absurd level of isolation & configuration as well as create disposable environments that can be easily recreated.

This allows us to obscure more persistent infrastructure like databases and other services that are not directly related to individual attacks.


For example, a C2 listener & a document storage system have different levels of Operational security considerations that need to be taken.


- Debian for the bare metal OS for all machines.
- Kubeadm for the base of the k8s distribution. Bare metal as it gets for k8s.
- VCluster at least will inspire the configurations of our machines if not be the outright choice we go with
- Vagrant for virtual machines
- Docker & podman, containerd runtimes available depending on the situation, and runtime requirementsm
- Nix for the container package manager

Basically the goal is to build something between Kali Linux and microk8s. 

Rather than providing you with a single OS environment with common configs Fock offensive security 

We are aiming to provide a rapidly evolving series of highly configurable environments for configuring and deploying common offensive infrastructure, centralizing the data and destroying unnecessary infrastructure when its job is done 

## 2 "Multiverse" Theory: Dividing the cluster into virtual clusters 

If you think of an instance of Kali as a planet we are aiming to create a “multiverse” of environments 

actually I like that analogy so we are running with it 

### 2.1 Kubeadm Cluster: The "Multiverse"
the multiverse in this case is the Kubernetes cluster. 


### 2.2 Virtual Clusters
credit for concept inspiration: [loft-sh/vcluster](https://github.com/loft-sh/vcluster)

The Kubernetes cluster contains X number of *universes* which are in this case `virtual Kubernetes clusters`.
`Virtual Kubernetes Clusters` like `virtual machines` are fully functional `Kubernetes clusters` - Each vcluster runs inside a namespace of the underlying k8s cluster. It's cheaper than creating separate full-blown clusters and it offers better multi-tenancy and isolation than regular namespaces.
These `virtual Kubernetes clusters` are isolated from each other and can be destroyed and recreated at will. They exist within the same cluster but are isolated from each other. 
`Virtual clusters` tend to serve a more specific purpose within the main cluster, taking the operations of the system at large into consideration, rather than just running a bunch of instances or something.
The next section will break down some information on the types of `virtual clusters` you can deploy within the `multiverse cluster`. 
#### 2.2.1 Defining Virtual Cluster Types


**Persistent Clusters**
Clusters designed to be protected, isolated & maintained for long periods of time. think of it as [dom0 in qubes OS](https://www.qubes-os.org/doc/glossary/#dom0).
- [Admin Cluster](docs/vclusters/Admin-Cluster.md)
- [AI Cluster](docs/vclusters/AI-Cluster.md)
- [Data Cluster](docs/vclusters/Data-Cluster.md)

**Temporary / Rotated Periodically Clusters**
length of time is irrelevant, these services (unless extremely necessary) should be destroyed and recreated periodically at set intervals. You should know ahead of time when you are going to destroy and recreate these clusters, to update your infrastructure and configurations to the latest versions & to match what your latest operation looks like. No wasted resources.
- [Barrier Cluster](docs/vclusters/Barrier-Cluster.md)
- [DMZ Cluster](docs/vclusters/DMZ-Cluster.md)
- [Jump Cluster](docs/vclusters/Jump-Cluster.md)
- [UI Cluster](docs/vclusters/UI-Cluster.md)


**Rapidly Disposable Clusters**
- [Phishing Cluster](docs/vclusters/Phishing-Cluster.md)
- [Attack Cluster](docs/vclusters/Attack-Cluster.md)
- [C2 Cluster](docs/vclusters/C2-Cluster.md)
- [Network Recon Cluster](docs/vclusters/Recon-Cluster.md)
- [Exploit Cluster](docs/vclusters/Exploit-Cluster.md)


