app = angular.module 'example.app.basic', []

app.controller 'AppController', ['$scope', '$http', ($scope, $http) ->
    $scope.employees = []
    $http.get('/api/employees').then (result) ->
        angular.forEach result.data, (item) ->
            $scope.employees.push item
]
