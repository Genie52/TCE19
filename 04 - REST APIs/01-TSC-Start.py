import tableauserverclient as TSC

#tableau REST API login
tableau_auth = TSC.TableauAuth('admin', 'admin')
server = TSC.Server('http://localhost', use_server_version = True) #use_server_version = True gives us the latest REST API version to work with

with server.auth.sign_in(tableau_auth):  #sign in to Tableau Server and do the things below
    #show REST API sevrer version
    tableau_server_version =  server.version
    print('\nTableau Server Version:', server.version,'\n') #3.4 is 2019.2
