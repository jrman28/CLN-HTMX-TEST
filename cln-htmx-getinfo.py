#!/usr/bin/env python3

from flask import Flask, Response, render_template
from pyln.client import Plugin, RpcError

plugin = Plugin()

@plugin.init()  # this runs when the plugin starts.
def init(options, configuration, plugin, **kwargs):

    plugin.log("lnwidget.guide - cln-htmx-getinfo plugin initialized")


@plugin.method("htmx-getinfo")
def htmx_getinfo(plugin):
    '''Returns the getinfo output as HTMX.'''
    
    html_content = "<table><tr><th>Node ID</th><th>Alias</th><th>Color</th></tr><tr><td>node_id_xxx</td><td>Alice</td><td>Blue</td></tr></table>"

    # Return the HTML content with the correct Content-Type header
    return Response(html_content, mimetype='text/html')
    
plugin.run()  # Run our plugin