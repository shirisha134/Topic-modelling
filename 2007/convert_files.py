import os
from pyth.plugins.rtf15.reader import Rtf15Reader
from pyth.plugins.xhtml.writer import XHTMLWriter


list_files = os.listdir('./')
rtf_files = [each for each in list_files if each[-4:]==".rtf"]

for each in rtf_files:
	doc = Rtf15Reader.read(open(each,'r'))
	print "Completed reading from %s" % (each)
	r=XHTMLWriter.write(doc, pretty=True).read()
	f_obj_w = open(each[:-4],'w')
	f_obj_w.write(r)
	