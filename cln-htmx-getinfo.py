#!/usr/bin/env python3

from pyln.client import Plugin, RpcError

plugin = Plugin()

@plugin.init()  # this runs when the plugin starts.
def init(options, configuration, plugin, **kwargs):
    plugin.log("cln-htmx-getinfo boilerplate.")

@plugin.method("htmx-getinfo")
def htmx_getinfo(plugin):
    '''
    Returns the getinfo output as HTMX.
    '''

    get_info_response = plugin.rpc.getinfo()
    node_id = get_info_response["id"]
    node_color = get_info_response["color"]
    node_alias = get_info_response["alias"]
    block_height = get_info_response["blockheight"]

    html_content = f"""
    <table>
        <tr>
            <th>Node ID</th>
            <th>Alias</th>
            <th>Color</th>
            <th>Block Height</th>
        </tr>
        <tr>
            <td>{node_id}</td>
            <td>{node_alias}</td>
            <td>{color}</td>
            <td>{block_height}</td>
        </tr>
    </table>
    """

    return html_content

plugin.run()  # Run our plugin
