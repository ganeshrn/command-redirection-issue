#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2017, Ansible by Red Hat, inc
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = """
module: my_command
"""

EXAMPLES = """
"""

RETURN = """
"""
from ansible.module_utils.basic import AnsibleModule


def main():
    """ main entry point for module execution
    """
    argument_spec = dict(
        test_cmd=dict(),
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
    )
    result = {'cmd': module.params['test_cmd']}
    module.exit_json(**result)


if __name__ == "__main__":
    main()
