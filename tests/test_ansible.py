import pytest


@pytest.fixture()
def AnsibleDefaults(Ansible):
    return Ansible("include_vars", "defaults/main.yml")["ansible_facts"]


@pytest.fixture()
def AnsibleVars(Ansible):
    return Ansible("include_vars", "tests/group_vars/group01.yml")["ansible_facts"]


def test_zookeeper_service(File, Service, Socket, AnsibleDefaults):
    assert File("/lib/systemd/system/zookeeper.service").exists
    assert Service("zookeeper").is_enabled
    assert Service("zookeeper").is_running
    port = AnsibleDefaults["client_port"]
    assert Socket("tcp://0.0.0.0:" + str(port)).is_listening
    jmx_port = AnsibleDefaults["zookeeper_jmx_port"]
    assert Socket("tcp://0.0.0.0:" + str(jmx_port)).is_listening
