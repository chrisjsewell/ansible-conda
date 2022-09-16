#!/usr/bin/python
# -*- coding: utf-8 -*-
DOCUMENTATION = """
---
module: expandpath
short_description: Expands `~` and environmental variables for a path
description:
- Expands `~` and environmental variables for a path
- Unlike the jinja filters, this expands based on the remote user/environment
author:
  - Chris Sewell (@chrisjsewell)
options:
  path:
    description: The path to expand
    type: path
    required: true
"""

EXAMPLES = """
- name: install packages via Conda
  chrisjsewell.conda.expand_path:
    path: ~/test
  register: result

- name: print the expanded path
  debug:
    var: result.path
"""

RETURN = """
path:
    description: The expanded path
    returned: successful == True
    type: str
"""
from ansible.module_utils.basic import AnsibleModule


def _main():
    """Module entrypoint."""
    module = AnsibleModule(
        argument_spec={
            "path": {
                "type": "path",
                "required": True,
            },
        },
        supports_check_mode=True,
    )

    module.exit_json(changed=False, path=module.params["path"])


if __name__ == "__main__":
    _main()
