# Data Cluster: Storage and Access Control for Knowledge & Information Management

The Data Cluster is designed to provide a secure and scalable environment for storing and managing knowledge and information. It is a persistent cluster that is protected, isolated, and maintained for long periods to ensure data integrity and availability.

## Purpose

The Data Cluster serves the following purposes:

- **Data Storage**: Provides a centralized repository for storing data, documents, and knowledge assets.
- **Access Control**: Enforces strict access control policies to protect sensitive information.
- **Data Management**: Facilitates the organization, retrieval, and sharing of data within the cluster.


## Components
**Relational Database**:
- [Postgres Database](https://www.postgresql.org/): A powerful, open-source object-relational database system. Reliable and robust, it is widely used for data storage and management.

**S3 Document Storage Options**:
- [SeaWeedFS S3 Document Storage](https://github.com/seaweedfs/seaweedfs)
- [MinIO S3 Document Storage](https://min.io/)

**Vector Storage/Database**:
- DuckDB
- SurrealDB
## Access Control
Access to the `Data Cluster` is restricted to authorized users and applications.

This is done via [Litestar ASGI Server](https://litestar.dev) (formerly known as Starlite) which provides us with the [Guards](https://docs.litestar.dev/2/usage/security/guards.html#guards) mechanism for access control.