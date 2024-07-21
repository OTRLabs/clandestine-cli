
# DMZ Cluster: Isolated Environment for Low-Risk External-Facing Services

The `DMZ Cluster` is designed to act as a boundary between internet-exposed services and the internal network. It provides a highly isolated environment for low-risk services, ensuring they do not compromise the internal network.

## Purpose

The `DMZ Cluster` hosts services that are exposed to the internet but pose minimal risk to the internal network. These services include:

- `Web Browsing` with [Crawlee](#) to emulate user browsing behavior. This should only be used if alerting the target network is of minimal risk.
- [Canary Services & Servers](#) to detect and alert on any scanning of unused routes on an HTTP server.
- `Web Servers` that host static content or low-risk applications, such as decoy sites.

## Features

### Isolation

- **Network Isolation**: The `DMZ Cluster` is isolated from the rest of the network to prevent unauthorized access to internal resources.
- **Service Isolation**: Each service within the `DMZ Cluster` operates in its own isolated environment.

### Security

- **Firewall Rules**: Strict firewall rules are in place to control access to and from the `DMZ Cluster`.
- **Access Controls**: Access to the `DMZ Cluster` is tightly controlled and monitored.

### Monitoring & Alerting

- **Activity Monitoring**: Continuous monitoring of the `DMZ Cluster` for suspicious activity or unauthorized access attempts.
- **Alerting**: Configured to send alerts on any suspicious activity or unauthorized access attempts.

### Decoy Services

- **Canary Services**: Includes canary services to detect and alert on any unauthorized access attempts.
- **Decoy Web Servers**: Hosts decoy web servers to detect and alert on unauthorized scanning activities.

### Logging

- **Activity Logging**: Logs all activities within the `DMZ Cluster` for auditing and analysis purposes.

### Web Browsing

- **User Emulation**: Includes a web browsing service with [Crawlee](#) to emulate user browsing behavior.

### Web Servers

- **Static Content Hosting**: Hosts web servers for static content or low-risk applications.

### Deployment

- **Multiple Instances**: The `DMZ Cluster` can be deployed in multiple instances, each acting as gatekeepers to the internal network. This creates a web of interconnected virtual clusters, making network navigation more difficult for attackers.

## Conclusion

The `DMZ Cluster` is a critical component in the Offensive Security Kubernetes Framework, providing a secure and isolated environment for low-risk, internet-facing services. By implementing strict security measures, continuous monitoring, and decoy services, it ensures that the internal network remains protected from external threats.

