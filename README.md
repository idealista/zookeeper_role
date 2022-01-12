![Logo](https://raw.githubusercontent.com/idealista/zookeeper_role/master/logo.gif)

# Apache ZooKeeper Ansible role 

[![Build Status](https://travis-ci.org/idealista/zookeeper_role.png)](https://travis-ci.org/idealista/zookeeper_role)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-idealista.zookeeper__role-B62682.svg)](https://galaxy.ansible.com/idealista/zookeeper_role)
[![Docker Hub pulls](https://img.shields.io/docker/pulls/idealista/zookeeper.svg)](https://hub.docker.com/r/idealista/zookeeper/)

This Ansible role installs an Apache ZooKeeper service in a Debian environment.

- [Getting Started](#getting-started)
	- [Prerequisites](#prerequisites)
	- [Installing](#installing)
- [Usage](#usage)
- [Testing](#testing)
- [Built With](#built-with)
- [Versioning](#versioning)
- [Authors](#authors)
- [License](#license)
- [Contributing](#contributing)

## Getting Started

These instructions will get you a copy of the role for your Ansible Playbook. Once launched, it will install an Apache ZooKeeper server.

### Prerequisites

Ansible 2.8.8 version installed.

Molecule 3.x.x version installed.

For testing purposes, [Molecule](https://molecule.readthedocs.io/) with [Docker](https://www.docker.com/) as driver and [Goss](https://github.com/aelsabbahy/goss) as verifier.

### Installing

Create or add to your roles dependency file (e.g requirements.yml):

```
- src: idealista.zookeeper_role
  version: 1.11.0
  name: zookeeper
```

Install the role with ansible-galaxy command:

```
ansible-galaxy install -p roles -r requirements.yml -f
```

Use in a playbook:

```
---

- hosts: someserver
  roles:
    - zookeeper
```

## Usage

To set multiple versions

```
zookeeper_hosts:
  - host: zookeeper1
    id: 1
  - host: zookeeper2
    id: 2
  - host: zookeeper3
    id: 3
```

## Testing

### Install dependencies

```sh
$ pipenv sync
```

For more information read the [pipenv docs](ipenv-fork.readthedocs.io/en/latest/).

### Testing

```sh
$ pipenv run molecule test 
```

## Built With

![Ansible](https://img.shields.io/badge/ansible-2.8.8-green.svg)

## Versioning

For the versions available, see the [tags on this repository](https://github.com/idealista/zookeeper_role/tags).

Additionaly you can see what change in each version in the [CHANGELOG.md](CHANGELOG.md) file.

## Authors

* **Idealista** - *Work with* - [idealista](https://github.com/idealista)

See also the list of [contributors](https://github.com/idealista/zookeeper_role/contributors) who participated in this project.

## License

![Apache 2.0 License](https://img.shields.io/hexpm/l/plug.svg)

This project is licensed under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license - see the [LICENSE](LICENSE) file for details.

## Contributing

Please read [CONTRIBUTING.md](.github/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.
