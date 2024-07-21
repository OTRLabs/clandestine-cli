# DMZ Cluster: Isolated Environment for Low Risk External-Facing Services

The `DMZ Cluster` is designed to be the dividing line between services that are exposed to the internet and the internal network. 

It is a highly isolated environment that allows low risk services such as:
- `web browsing` with [Crawlee]() that emulates a user browsing the internet. only use if the target network being alerted is of minimal risk to the internal network.
- [Canary Services & Servers]() that act as decoys to detect and alert on anyone scanning unused routes on an HTTP server or something.
- `web servers` that host static content or low-risk applications. Decoy sites perhaps.

& low external-facing services with low risk to the internal network.

## Features

- **Isolation**: The DMZ Cluster is isolated from the rest of the network to prevent unauthorized access to internal resources.
- **Security**: The DMZ Cluster is designed to be secure by default, with strict firewall rules and access controls.
- **Monitoring**: The DMZ Cluster is monitored for any suspicious activity or unauthorized access attempts.
- **Decoy Services**: The DMZ Cluster hosts decoy services to detect and alert on any unauthorized access attempts.
- **Web Browsing**: The DMZ Cluster includes a web browsing service to emulate user browsing behavior.
- **Web Servers**: The DMZ Cluster hosts web servers for hosting static content or low-risk applications.
- **Canary Services**: The DMZ Cluster includes canary services to detect and alert on unauthorized access attempts.
- **Low Risk**: The DMZ Cluster is designed for hosting low-risk external-facing services.
- **Alerting**: The DMZ Cluster is configured to alert on any suspicious activity or unauthorized access attempts.
- **Logging**: The DMZ Cluster logs all activity for auditing and analysis purposes.
- **Multiple Instances**: The DMZ Cluster can be deployed in multiple instances acting as gatekeepers to create a web of vclusters that do have access to each other. this make pivoting & network navigation more difficult for attackers.