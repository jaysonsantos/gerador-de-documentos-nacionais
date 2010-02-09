#!/bin/bash
gksu -c "cp $PWD/gerador-de-documentos-nacionais.py /usr/bin/ && chmod +x /usr/bin/gerador-de-documentos-nacionais.py"
gksu -c "cp $PWD/GNOME_GeradorDeDocumentosNacionaisApplet.server /usr/lib/bonobo/servers/"

