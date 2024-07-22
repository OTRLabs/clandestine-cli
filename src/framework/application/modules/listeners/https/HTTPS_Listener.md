# Standard HTTPS Listener

---

purpose: |
    This document provides the necessary information to deploy a standard HTTPS Listener on the C2 Virtual Kubernetes Cluster.



---

## 1. HTTPS Listener Deployment Overview
Built using [Litestar ASGI Framework](https://litestar.dev), the `HTTPS Listener` is a standard listener that is deployed on the `C2 Virtual Kubernetes Cluster`. The `HTTPS Listener` is a secure listener that is used to receive incoming requests from the `C2 Agent` and forward them to the `C2 Command & Control Server`. The `HTTPS Listener` is deployed on the `C2 Virtual Kubernetes Cluster` and is used to receive incoming requests from the `C2 Agent` and forward them to the `C2 Command & Control Server`.
### 1.1. HTTPS Listener Deployment Process:

#### 1.1.1. Manual Listener Deployment Steps:
- 1. [ ] Access the `C2 Virtual Kubernetes Cluster` *admin panel*, and follow the instructions to deploy a new listener `HTTPS Listener`.
- 2. [ ] Launch the first layer of isolation, the base environment in this case is the `Debian 12` `KVM based virtual machine`, hardened with the `C2 Listener Security Baseline`. Authenticate with this machine & access it via `SSH`.
- 3. [ ] Once you have authorized & have access to the `Debian 12` `KVM Virtual machine` has been obtained, begin building the next layer of *virtualization* / *isolation* to the `HTTPS Listener` be container for the [Litestar ASGI Framework](https://litestar.dev) based `HTTPS Listener`.
- 4. [ ] Deploy the `HTTPS Listener` container on the `Debian 12` `KVM Virtual machine` using the `Docker` container runtime.