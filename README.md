# Ansible Collection - `chrisjsewell.conda`

[![Ansible Galaxy](https://img.shields.io/badge/galaxy-chrisjsewell.conda-blue.svg)](https://galaxy.ansible.com/chrisjsewell/conda)

## Install

```bash
$ ansible-galaxy collection install chrisjsewell.conda
```

## Roles

### `chrisjsewell.conda.user_install`

Install the `conda` package manager for a specific user.
You should call this role using the user that you want to install `conda` for.

```yaml
- hosts: servers
  roles:
  - role: chrisjsewell.conda.user_install
    become: true
    become_user: user_name
```

variables:

```yaml
- conda_folder
        The folder where conda will be installed
        (~ expands to the user's home directory)
        [Default: ~/.conda]
        type: str

- conda_executable
        the name of the conda executable to use for `[conda|mamba] init`
        [Default: mamba]
        type: str

- conda_installer_checksum
        the sha256 checksum of the installer
        [Default: sha256:d47b78b593e3cf5513bafbfa6a51eafcd9f0e164c41c79c790061bb583c82859]
        type: str

- conda_installer_url
        the url to the conda installer
        [Default: https://github.com/conda-forge/miniforge/releases/download/4.14.0-0/Mambaforge-4.14.0-0-Linux-x86_64.sh]
        type: str

- conda_download_timeout
        the timeout for the installer
        [Default: 300]
        type: int

- conda_activate_alias
        Create an alias command for `conda activate`
        type: str
```

## Modules

### `chrisjsewell.conda.install_pks`

Install conda packages, into an existing or new environment.

```yaml
- name: Install Conda packages
  become: true
  become_user: user_name
  chrisjsewell.conda.install_pks:
    env: myenv
    packages:
    - python=3.9
    - numpy
```

Options:

```yaml
- packages
        The name of the packages to install.

        elements: str
        type: list
- channels
        Extra channels to use when installing packages.
        [Default: (null)]
        elements: str
        type: list

- env
        Name of the environment (if it does not exist then it will be created).
        [Default: (null)]
        type: str

- executable
        Full path to the conda executable
        (~ expands to the user's home directory)
        [Default: ~/.conda/bin/mamba]
        type: path

- extra_args
        Extra arguments passed to the command.
        [Default: (null)]
        type: str
```

Return values:

```yaml
- output
        JSON output from Conda

        returned: changed == True
        type: dict

- stderr
        stderr content written by Conda

        returned: changed == True
        type: str
```

### `chrisjsewell.conda.list_pks`

List conda packages, from an existing environment.

```yaml
- name: list packages in Conda environment
  chrisjsewell.conda.list_pkgs:
    env: myenv
    regex: python.*
  register: myenv_pkgs

- debug:
    var: myenv_pkgs.list
```

Options:

```yaml
- env
        Name of the environment
        type: str

- executable
        Full path to the conda executable
        (~ expands to the user's home directory)
        [Default: ~/.conda/bin/mamba]
        type: path

- regex
        List only packages matching this regular expression.
        [Default: (null)]
        type: str
```

Return values:

```yaml
- list
        JSON output from Conda for each package (keys include 'name', 'version', 'channel')

        elements: dict
        returned: success == False
        type: list
```

## Development

See: <https://docs.ansible.com/ansible/latest/dev_guide/developing_collections.html>

### Testing

To run `ansible-conda` sanity tests:

```bash
ansible-test sanity --target-python=3.10 --skip-test metaclass-boilerplate --skip-test future-import-boilerplate
```

### Documentation

To create docs build of a role:

```bash
ansible-doc -t role -r roles -s install
```

To create docs build of a module:

```bash
ansible-doc -t module -M plugins/modules -s install_pkgs
```

### Distribution

To build the collection artifact:

```bash
ansible-galaxy collection build --force --output-path dist
```

To publish the collection artifact to [Ansible Galaxy](https://galaxy.ansible.com):

```bash
$ ansible-galaxy collection publish --token xxx dist/chrisjsewell-conda-yyy.tar.gz
```
