app = angular.module 'example.app.manage', ['example.api', 'example.app.editor']

app.controller 'DeleteController', ['$scope', 'AuthUser', ($scope, AuthUser) ->
    $scope.canDelete = (employee) ->
        return employee.author.username == AuthUser.username
    
    $scope.delete = (employee) ->
        employee.$delete()
        .then ->
            # Remove it from the list on success
            idx = $scope.employees.indexOf(employee)
            $scope.employees.splice(idx, 1)
]
