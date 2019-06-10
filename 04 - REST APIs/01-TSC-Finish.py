import tableauserverclient as TSC

#tableau REST API login
tableau_auth = TSC.TableauAuth('admin', 'admin')
server = TSC.Server('http://localhost', use_server_version = True) #use_server_version = True gives us the latest REST API version to work with

with server.auth.sign_in(tableau_auth):  #sign in to Tableau Server and do the things below
    #show REST API sevrer version
    tableau_server_version =  server.version
    print('\nTableau Server Version:', server.version,'\n') #3.4 is 2019.2

    # - 01 - show all the workbooks
    print('\nGET ALL THE WORKBOOKS >>>')
    for wb in TSC.Pager(server.workbooks):  #read all the workbooks in Tableau Server
        print('Workbook name:', wb.name, ', and LUID:', wb.id)

    # - 02 - show all views across all the workbooks
    print('\nGET ALL THE VIEWS ACROSS ALL THE WORKBOOKS >>>')
    print('All the Views (Pager): ')
    for view in TSC.Pager(server.views):
        print(view.name)  #this line repeats for every View available - thats why they are printed one after another

    # - 03 - same as above but in a list - shows all view from all workbooks
    print('\nGET ALL THE VIEWS ACROSS ALL THE WORKBOOKS >>>')
    all_views, pagination_item = server.views.get()
    print('All the Views: ',[view.name for view in all_views])

    # - 04 - get the workbook by ID and see the views of only that workbook
    print('\nGET THE WORKBOOK BY LUID and its VIEWS >>>')
    workbook = server.workbooks.get_by_id('5fba2c81-76b3-4b29-b24b-0f69eca3703f')
    server.workbooks.populate_views(workbook) #get only the views of that particular workbook
    print('Views of the Workbook uder ID: ',workbook.id, ' (name : ',workbook.name,')' ,' are: ',[view.name for view in workbook.views])

    # - 05 - get all usernames and LUIDs
    print('\nGET USERS NAMES AND LUIDs >>>')
    all_users, pagination_item = server.users.get()
    print('All the Users: ',[user.name for user in all_users])
    print('IDs of the Users: ',[user.id for user in all_users])

    # - 06 - get user by name
    print('\nGET USER BY NAME >>>')
    req_option = TSC.RequestOptions()
    req_option.filter.add(TSC.Filter(TSC.RequestOptions.Field.Name,
                                 TSC.RequestOptions.Operator.Equals,
                                 'User01'))
    matching_user, pagination_item = server.users.get(req_option)
    print('Username is: ',matching_user[0].name, 'and LUID of the user:',matching_user[0].id)


    # - 07 - get the workbooks for the specific user
    print('\nGET WORKBOOKS FOR THE SPECIFIC USER >>>')
    server.users.populate_workbooks(matching_user[0])
    print("The workbooks for",matching_user[0].name,"are :")
    for workbook in matching_user[0].workbooks :
        print(workbook.name)
