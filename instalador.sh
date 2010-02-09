#!/bin/bash
if [ $(whoami) != "root" ]
then
    echo "Executando o instalador como root"
    gksu "$(readlink -f "$0")"
    exit 0
fi

zenity --question --text="Você tem certeza que deseja instalar o applet de geração de documentos nacionais ?"
if [ $? -ne 0 ]
then
    zenity --info --text="Instalação abortada."
    exit 1
fi

cp $PWD/gerador-de-documentos-nacionais.py /usr/bin/ && chmod +x /usr/bin/gerador-de-documentos-nacionais.py
cp $PWD/GNOME_GeradorDeDocumentosNacionaisApplet.server /usr/lib/bonobo/servers/

if [ $? -eq 0 ]
then
    zenity --info --text="Applet instalado com sucesso"
    exit 0
fi
