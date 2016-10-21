app = angular.module 'example.app.editor', ['example.api', 'example.app.photos']

app.controller 'EditController', ['$scope', 'Employee', ($scope, Employee) ->
    
    $scope.newEmployee = new Employee()
    $scope.save = ->
        $scope.newEmployee.$save().then (result) ->
            $scope.employees.push result
        .then ->
            # Reset our editor to a new blank employee
            $scope.newEmployee = new Employee()
        .then ->
            # Clear any errors
            $scope.errors = null
        , (rejection) ->
            $scope.errors = rejection.data
]
