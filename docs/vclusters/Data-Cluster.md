# Data Cluster: Storage and Access Control for Knowledge & Information Management

The Data Cluster is designed using [SurrealDB](https://surrealdb.com) ito provide a secure and scalable environment for storing and managing knowledge and information. It is a persistent cluster that is protected, isolated, and maintained for long periods to ensure data integrity and availability.


## 1. Overview

## 2. Purpose

## 3. Design
Uses `SurrealDB` for data storage and management.

### 3.1. Single Node Clusters are optimized to use RocksDB 
**Built on RocksDB**:

>Reference: [SurrealDB Docs](https://surrealdb.com/docs/surrealdb/introduction/architecture#rocksdb)
> "In embedded mode, SurrealDB uses RocksDB to store data on disk. `RocksDB` is a high performance embedded database for key-value data. It is originally a fork of Google's LevelDB optimized to exploit many CPU cores, and make efficient use of fast storage, such as solid-state drives and high-speed disk drives. It is based on a log-structured merge-tree data structure."

### 3.2. Multi-Node Clusters are optimized to use [TiKV](https://tikv.org/)
References: [SurrealDB Docs](https://surrealdb.com/docs/surrealdb/introduction/architecture#rocksdb)

## Purpose

The Data Cluster serves the following purposes:

- **Data Storage**: Provides a centralized repository for storing data, documents, and knowledge assets.
- **Access Control**: Enforces strict access control policies to protect sensitive information.
- **Document Management**: Supports the creation, organization, and retrieval of documents and files. Primarily Markdown, PDF, and other common file types. These documents locations are indexed in the database, allowing for combined knowledge to be shared.
- **Dataset Management**: Supports the organization and management of datasets for machine learning and data analysis primarily related to offensive security operations.
- **Knowledge Management**: Facilitates the organization, retrieval, and sharing of knowledge assets within the cluster.
- **Data Management**: Facilitates the organization, retrieval, and sharing of data within the cluster.
- **Log Analysis**: Supports log analysis and monitoring to track system activities and performance.
- **Data Processing**: [SurrealML](https://surrealdb.com/docs/surrealml) enables `advanced data processing` and analytics to derive insights from `operations` and make more informed decisions in the future based on your total comprehensive knowledge + Advanced `ML insights` using [PyTorch]() & [Tensorflow]().

## Components
**SurrealDB**: The primary database system for storing system-wide information and knowledge assets. The database is designed to be highly available, scalable, and secure. It supports various data types, including structured, semi-structured, and unstructured data.

**Goal**: Use `SurrealDB` as the single source of truth for storing and managing knowledge assets within the multiverse. All virtual clusters use the same database, allowing for users to reap the organizational benefits of all of `SurrealDB's` features.

> One thing I am most excited for, is the ability to use [SurrealML](https://surrealdb.com/docs/surrealml) to create and manage machine learning models. This will allow for the creation of AI models using Tensorflow & PyTorch to enhance the data in your database. 

the idea is that you can index all:


These analytics will be used across the `multiverse of environments`, providing a consistent and reliable source of truth for the state of our operations, allowing hyper optimizedd `AI`/`ML` models to interact with all the data we log..


