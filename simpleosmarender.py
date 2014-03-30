#!/bin/env python

from optparse import OptionParser, OptionValueError
from subprocess import check_call
import os

class SimpleOsmarender:
    def __init__(self):
        self.OptionParser = OptionParser(usage = '%prog [options] input.osm output.svg')
        self.OptionParser.add_option('-z', '--zoom', action = 'store',
            type = 'int', dest = 'zoom', default = 17,
            help = 'Zoom level [default: %default]' )
    
    def __path_to_default_input_xml_file(self, zoom):
        exec_dirpath = os.path.dirname(os.path.realpath(__file__))
        return os.path.join(exec_dirpath, 'osm-map-features-z%d.xml' % (zoom))
    
    def run(self):
        (options, args) = self.OptionParser.parse_args()
        
        if len(args) != 2:
            self.OptionParser.error('require osm file and svg file.')
        inputosm = os.path.abspath(args[0])
        outputsvg = os.path.abspath(args[1])
        xmlfile = os.path.abspath(self.__path_to_default_input_xml_file(options.zoom))
        
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        check_call(["xsltproc", "-o", outputsvg,
                                "--stringparam", "osmfile", inputosm,
                                "osmarender.xsl",
                                xmlfile])

if __name__ == '__main__':
    r = SimpleOsmarender()
    r.run()

# vim: expandtab shiftwidth=4 tabstop=8 softtabstop=4 fileencoding=UTF-8 textwidth=99:
