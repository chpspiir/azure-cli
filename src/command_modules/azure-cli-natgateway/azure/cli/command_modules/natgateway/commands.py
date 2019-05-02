# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.commands import CliCommandType

from azure.cli.command_modules.natgateway._client_factory import cf_nat_gateways

def load_command_table(self, _):

    nat_gateway_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.network.operations#NatGatewaysOperations.{}',
        client_factory=cf_nat_gateways)

    with self.command_group('network nat-gateway', nat_gateway_sdk) as g:
        g.show_command('show', 'get')
        g.generic_update_command('update', supports_no_wait=True)
        g.custom_command('create', 'create_nat_gateway', supports_no_wait=True)
        g.custom_command('list', 'list_nat_gateway')
        g.command('delete', 'delete')
        g.wait_command('wait')
