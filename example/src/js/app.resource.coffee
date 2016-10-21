app = angular.module 'example.app.resource', ['example.api']

app.controller 'AppController', ['$scope', 'Employee', ($scope, Employee) ->
    $scope.employees = Employee.query()
]
