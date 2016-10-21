app = angular.module 'example.api', ['ngResource']

app.factory 'User', ['$resource', ($resource) ->
    $resource '/api/users/:username', username: '@username'
]

app.factory 'Employee', ['$resource', ($resource) ->
    $resource '/api/employees/:id', id: '@id'
]

app.factory 'Photo', ['$resource', ($resource) ->
    $resource '/api/photos/:id', id: '@id'
]

# And the nested resources
app.factory 'UserEmployee', ['$resource', ($resource) ->
    $resource '/api/users/:username/posts/:id'
]

app.factory 'EmployeePhoto', ['$resource', ($resource) ->
    $resource '/api/employees/:employee_id/photos/:id'
]
