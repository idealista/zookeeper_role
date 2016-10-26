import pytest


@pytest.fixture()
def AnsibleDefaults(Ansible):
    return Ansible("include_vars", "defaults/main.yml")["ansible_facts"]


@pytest.fixture()
def AnsibleVars(Ansible):
    return Ansible("include_vars", "tests/group_vars/group01.yml")["ansible_facts"]


def test_zookeeper_version(File, AnsibleVars):
    version = AnsibleVars["zookeeper_version"]
    assert File("/opt/zookeeper-" + version).exists
    assert File("/opt/zookeeper").is_symlink
    assert File("/opt/zookeeper").linked_to == "/opt/zookeeper-" + version
