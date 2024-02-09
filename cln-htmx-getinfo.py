#!/usr/bin/env python3
import json
import re
from pyln.client import Plugin, RpcError

plugin = Plugin()

@plugin.init()  # this runs when the plugin starts.
def init(options, configuration, plugin, **kwargs):

    plugin.log("lnwidget.guide - cln-htmx-getinfo plugin initialized")


@plugin.method("htmx-getinfo")
def htmx_getinfo(plugin):
    '''Returns the getinfo output as HTMX.'''
    try:
        return "<p>Get Info</p>"

    except RpcError as e:
        plugin.log(e)
        return e



plugin.run()  # Run our plugin