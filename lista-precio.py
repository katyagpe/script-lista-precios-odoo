#! /usr/bin/env python
# -*- coding: utf-8 -*-

#********************************************************#
# Creacion de productos                                  #
#********************************************************#

import os
import csv
import xmlrpclib
import re


HOST='demos.4toangulogestionintegral.com'
PORT=80
DB='Surtimex-Sept'
USER='katya.salas@4toangulo.com'
PASS='8+qnDM!;tN"6K7H'
url ='http://%s:%d/xmlrpc/' % (HOST,PORT)

common_proxy = xmlrpclib.ServerProxy(url+'common')
object_proxy = xmlrpclib.ServerProxy(url+'object')
uid = common_proxy.login(DB,USER,PASS)


def _create(estado):
    if estado is True:
        path_file = './precioPromo6.csv'
        archive = csv.DictReader(open(path_file))
        cont = 1

        for field in archive:
            print field
            vals = {'pricelist_id':field['base_id'],'fixed_price':field['tipo'],'applied_on':field['applied_on'],'product_tmpl_id':field['product_tmpl_id'],'compute_price':field['compute_price']}
            do_write = object_proxy.execute(DB,uid,PASS,'product.pricelist.item','create',vals)
            if do_write:
                cont = cont + 1
                print "Contador:",cont
            else:
                print "Error"

def __main__():
    print 'Ha comenzado el proceso'
    _create(True)
    print 'Ha finalizado la carga tabla'
__main__()