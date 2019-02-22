# Change Log
All notable changes to this project will be documented in this file.

## [Unreleased](https://github.com/idealista/zookeeper_role/tree/develop)

## [1.5.0](https://github.com/idealista/zookeeper_role/tree/1.5.0) (2019-02-22)
[Full Changelog](https://github.com/idealista/zookeeper_role/compare/1.4.1...1.5.0)
### Changed
- *[#40](https://github.com/idealista/zookeeper_role/issues/40) Changing role name* @dortegau
### Added
- *[#26](https://github.com/idealista/zookeeper_role/issues/26) Adding deployment to Docker Hub via ansible playbook* @dortegau

## [1.4.1](https://github.com/idealista/zookeeper_role/tree/1.4.1) (2019-01-30)
[Full Changelog](https://github.com/idealista/zookeeper_role/compare/1.4.0...1.4.1)
### Fixed
- *[#36](https://github.com/idealista/zookeeper_role/issues/36) Check if `zookeeper_config_map` is defined*  @eskabetxe

## [1.4.0](https://github.com/idealista/zookeeper_role/tree/1.4.0) (2019-01-03)
[Full Changelog](https://github.com/idealista/zookeeper_role/compare/1.3.0...1.4.0)
### Added
- *[#23](https://github.com/idealista/zookeeper_role/issues/23) Support advanced configuration values* @jperera
### Fixed
- *[#32](https://github.com/idealista/zookeeper_role/issues/32) Fix [CVE-2018-10855](https://access.redhat.com/security/cve/cve-2018-10855) (using Ansible > 2.5.5.0)*  @dortegau

## [1.3.0](https://github.com/idealista/zookeeper_role/tree/1.3.0) (2018-12-05)
[Full Changelog](https://github.com/idealista/zookeeper_role/compare/1.2.0...1.3.0)
### Changed
- *[#23](https://github.com/idealista/zookeeper_role/issues/23) Using ZooKeeper 3.4.13 as default version*  @dortegau
- *[#22](https://github.com/idealista/zookeeper_role/issues/22) Upgrading molecule version to 2.19.0 and Ansible to 2.5.3.0*  @dortegau

## [1.2.0](https://github.com/idealista/zookeeper_role/tree/1.2.0) (2018-06-04)
[Full Changelog](https://github.com/idealista/zookeeper_role/compare/1.1.1...1.2.0)
### Changed
- *[#19](https://github.com/idealista/zookeeper_role/issues/19) Upgrade ZooKeeper version to 3.4.12*  @eskabetxe
- *Upgrade idealista.java-role to 3.0.0* @eskabetxe

## [1.1.1](https://github.com/idealista/zookeeper_role/tree/1.1.1) (2018-03-05)
[Full Changelog](https://github.com/idealista/zookeeper_role/compare/1.1.0...1.1.1)
### Fixed
- *[#12](https://github.com/idealista/zookeeper_role/issues/12) Expose service using tcp4 by default and ensuring that remote JMX access is enabled*  @dortegau
- *Remove upstart script to easy enable systemd service* @jmonterrubio

## [1.1.0](https://github.com/idealista/zookeeper_role/tree/1.1.0) (2017-05-04)
[Full Changelog](https://github.com/idealista/zookeeper_role/compare/1.0.3...1.1.0)
### Added
- *[#6](https://github.com/idealista/zookeeper_role/issues/6) Added JMX*  @jmonterrubio
### Changed
- *Some variable redefinition* @jmonterrubio
### Fixed
- *Remove upstart script to easy enable systemd service* @jmonterrubio

## [1.0.3](https://github.com/idealista/zookeeper_role/tree/1.0.3) (2016-12-23)
[Full Changelog](https://github.com/idealista/zookeeper_role/compare/1.0.2...1.0.3)
### Fixed
- *[#1](https://github.com/idealista/zookeeper_role/issues/1) Enable service by default*  @jmonterrubio

## [1.0.2](https://github.com/idealista/zookeeper_role/tree/1.0.2) (2016-12-21)
[Full Changelog](https://github.com/idealista/zookeeper_role/compare/1.0.1...1.0.2)
### Fixed
- *Update docs and refactor tasks*  @jmonterrubio

## [1.0.1](https://github.com/idealista/zookeeper_role/tree/1.0.1) (2016-11-18)
[Full Changelog](https://github.com/idealista/zookeeper_role/compare/1.0.0...1.0.1)
### Fixed
- *Fix problem with ansible unarchive*  @jmonterrubio

## [1.0.0](https://github.com/idealista/zookeeper_role/tree/1.0.0) (2016-10-26)
### Added
- *First commit* @jmonterrubio
