#
# This file is part of rhevsh. rhevsh is free software that is made
# available under the MIT license. Consult the file "LICENSE" that is
# distributed together with this file for the exact licensing terms.
#
# rhevsh is copyright (c) 2011 by the rhevsh authors. See the file
# "AUTHORS" for a complete overview.

from optparse import OptionParser, HelpFormatter


class RhevshHelpFormatter(HelpFormatter):
    """Help formatter that does not try to reformat multi-line strings."""

    def __init__(self):
        HelpFormatter.__init__(self, indent_increment=0,
                   max_help_position=24, width=None, short_first=0)

    def format_description(self, description):
        return description

    def format_usage(self, usage):
        return 'Usage: %s\n' % usage
 
    def format_heading(self, heading):
        return '%s\n' % heading


class RhevshOptionParser(OptionParser):

    usage='%prog [options]'
    description = 'foo'

    def __init__(self):
        formatter = RhevshHelpFormatter()
        OptionParser.__init__(self, formatter=formatter, usage=self.usage,
                              description=self.description)
        self.add_option('-d', '--debug', action='store_true',
                        help='enable debugging')
        self.add_option('-v', '--verbose', action='store_true',
                        help='be more verbose')
        self.add_option('-U', '--url',
                        help='specifies the API entry point URL')
        self.add_option('-u', '--username', help='connect as this user')
        self.add_option('-p', '--password', help='specify password')
        self.add_option('-r', '--read-input', action='store_true',
                        help='read pre-formatted input on stdin')
        self.add_option('-i', '--input-format', metavar='FORMAT',
                        help='input format for pre-formatted input')
        self.add_option('-o', '--output-format', metavar='FORMAT',
                         help='specfies the output format')
        self.add_option('-c', '--connect', action='store_true',
                        help='automatically connect')
        self.add_option('-f', '--filter', metavar='FILE',
                        help='read commands from FILE instead of stdin')
        self.add_option('-w', '--wide', action='store_true',
                        help='wide display')
        self.add_option('-n', '--no-header', action='store_false',
                        dest='header', help='suppress output header')
        self.add_option('-F', '--fields', help='fields to display')
        self.disable_interspersed_args()
