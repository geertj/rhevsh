#
# This file is part of rhevsh. rhevsh is free software that is made
# available under the MIT license. Consult the file "LICENSE" that is
# distributed together with this file for the exact licensing terms.
#
# rhevsh is copyright (c) 2011 by the rhevsh authors. See the file
# "AUTHORS" for a complete overview.

from xml.etree import ElementTree as etree
from rhevsh.format.format import Formatter

# This module is called xml_ to prevent a naming conflict with the standard
# libary.

class XmlFormatter(Formatter):
    """XML formatter."""

    name = 'xml'

    def _make_pretty(self, node, level=0, last=False):
        """INTERNAL: pretty up the XML."""
        def spacing(level):
            return '\n' + '  ' * level
        node.tail = spacing(level-last)
        if len(node) == 0:
            return
        node.text = spacing(level+1)
        for ix in range(len(node)):
            self._make_pretty(node[ix], level+1, ix == len(node)-1)
        verbose = self.context.settings['verbose']
        if verbose:
            return
        remove = []
        for child in node:
            if child.tag in ('actions', 'link'):
                remove.append(child)
        for child in remove:
            node.remove(child)

    def format(self, context, result):
        if not hasattr(result, 'toxml'):
            raise TypeError, 'Expecting a binding instance.'
        self.context = context
        stdout = context.terminal.stdout
        buf = result.toxml()
        xml = etree.fromstring(buf)
        self._make_pretty(xml)
        buf = etree.tostring(xml)
        stdout.write(buf)
