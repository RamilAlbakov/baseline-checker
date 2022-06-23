"""Get data from ENM by executing CLI commands."""

import os

import enmscripting


class Enm(object):
    """Provide API for connecting to ENM and get data."""

    def execute_enm_command(self, cli_command):
        """
        Execute ENM CLI commands.

        Args:
            cli_command: string

        Returns:
            enmscripting ElementGroup
        """
        session = enmscripting.open(os.getenv('ENM_SERVER')).with_credentials(
            enmscripting.UsernameAndPassword(
                os.getenv('ENM_LOGIN'),
                os.getenv('ENM_PASSWORD'),
            ),
        )
        enm_cmd = session.command()
        response = enm_cmd.execute(cli_command)
        enmscripting.close(session)
        return response.get_output()
