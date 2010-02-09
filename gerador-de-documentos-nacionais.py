#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Copyright (c) 2005-2010, Jayson Santos dos Reis
All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

    * Redistributions of source code must retain the above copyright notice,
      this list of conditions and the following disclaimer.

    * Redistributions in binary form must reproduce the above copyright notice,
      this list of conditions and the following disclaimer in the documentation
      and/or other materials provided with the distribution.

    * Neither the name of Alexandre Gomes Gaigalas nor the names of its
      contributors may be used to endorse or promote products derived from this
      software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

import math
from random import random        
import pygtk
pygtk.require('2.0')
import gtk

import sys

if len(sys.argv) > 1 and sys.argv[1] == '-s':
    standalone = True
else:
    standalone = False
    import gnomeapplet

class CpfApplet:
    def __init__(self, applet):
        self.cpf = True
        
        self.clipboard = gtk.clipboard_get()
        
        self.hbox = gtk.HBox()
        applet.add(self.hbox)
        
        self.documentoEventBox = gtk.EventBox()
        self.hbox.pack_start(self.documentoEventBox)
        
        self.label = gtk.Label("CPF: ")
        self.documentoEventBox.add(self.label)
        self.documentoEventBox.connect('button-press-event', self.labelClicked)
        
        self.documentoEntry = gtk.Entry()
        self.hbox.pack_start(self.documentoEntry)
        
        self.pontosCheckbox = gtk.CheckButton('Pontos ?')
        self.pontosCheckbox.set_active(True)
        self.hbox.pack_start(self.pontosCheckbox)
        
        self.button = gtk.Button('Gerar')
        self.button.connect('clicked', self.btnGerarDocumento)
        self.hbox.pack_start(self.button)      
        
        self.documentoEntry.set_text(self.gerarCpf())

        applet.show_all()
    
    def btnGerarDocumento(self, w, data = None):
        if self.cpf:
            documento = self.gerarCpf()
        else:
            documento = self.gerarCnpj()
            
        self.documentoEntry.set_text(documento)
        self.clipboard.set_text(documento, len(documento))
        self.clipboard.store()
        
    def labelClicked(self, w, data = None):
        if self.cpf:
            self.label.set_text('CNPJ: ')
            self.cpf = False
        else:
            self.label.set_text('CPF: ')
            self.cpf = True
        self.button.clicked()
        
    def randomiza(self, n):
        return round(random()*n)
        
    def gerarCnpj(self):
        n = 9
        n1 = self.randomiza(n)
        n2 = self.randomiza(n)
        n3 = self.randomiza(n)
        n4 = self.randomiza(n)
        n5 = self.randomiza(n)
        n6 = self.randomiza(n)
        n7 = self.randomiza(n)
        n8 = self.randomiza(n)
        n9 = 0
        n10 = 0
        n11 = 0
        n12 = 1
        d1 = n12 * 2 + n11 * 3 + n10 * 4 + n9 * 5 + n8 * 6 + n7 * 7 + n6 * 8 +n5 * 9 + n4 * 2 + n3 * 3 + n2 * 4 +n1 * 5
        d1 = 11 - (d1 % 11)
        if d1 >= 10:
            d1 = 0
        d2 = d1 * 2 + n12 * 3 + n11 * 4 + n10 * 5 + n9 * 6 + n8 * 7 + n7 * 8 + n6 * 9 + n5 * 2 + n4 * 3 + n3 * 4 + n2 * 5 + n1 * 6
        d2 = 11 - (d2 % 11)
        if d2 >= 10:
            d2 = 0
        if self.pontosCheckbox.get_active():
           return '%d%d.%d%d%d.%d%d%d/%d%d%d%d-%d%d' % (n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, d1, d2)
        else:
           return '%d%d%d%d%d%d%d%d%d%d%d%d%d%d' % (n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, d1, d2)
        
    def gerarCpf(self):
        n = 9
        n1 = self.randomiza(n)
        n2 = self.randomiza(n)
        n3 = self.randomiza(n)
        n4 = self.randomiza(n)
        n5 = self.randomiza(n)
        n6 = self.randomiza(n)
        n7 = self.randomiza(n)
        n8 = self.randomiza(n)
        n9 = self.randomiza(n)
        d1 = n9 * 2 + n8 *3 + n7 * 4 + n6 * 5 + n5 * 6 + n4 * 7 + n3 * 8 + n2 * 9 + n1 * 10
        d1 = 11 - (d1 % 11)
        if (d1>=10):
            d1 = 0
        d2 = d1 * 2 + n9 * 3 + n8 * 4 + n7 * 5 + n6 * 6 + n5 * 7 + n4 * 8 + n3 * 9 + n2 * 10 + n1 * 11
        d2 = 11 - (d2 % 11)
        if (d2>=10):
            d2 = 0
        if self.pontosCheckbox.get_active():
            return '%d%d%d.%d%d%d.%d%d%d-%d%d' % (n1, n2, n3, n4, n5, n6, n7, n8, n9, d1, d2)
        else:
            return '%d%d%d%d%d%d%d%d%d%d%d' % (n1, n2, n3, n4, n5, n6, n7, n8, n9, d1, d2)

def sample_factory(applet, iid):
    CpfApplet(applet)
    return True
    
if standalone:
    window = gtk.Window()
    window.connect('destroy', gtk.main_quit)
    CpfApplet(window)
    gtk.main()
else:
    gnomeapplet.bonobo_factory("OAFIID:GNOME_GeradorCpfApplet_Factory", 
                                 gnomeapplet.Applet.__gtype__, 
                                 "hello", "0", sample_factory)


