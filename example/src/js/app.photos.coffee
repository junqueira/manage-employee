app = angular.module 'example.app.photos', ['example.api']

app.controller 'AppController', ['$scope', 'Employee', 'PostPhoto', ($scope, Employee, EmployeePhoto) ->
    $scope.photos = {}
    $scope.posts = Employee.query()
    $scope.posts.$promise.then (results) ->
        # Load the photos
        angular.forEach results, (employee) ->
            $scope.photos[employee.id] = EmployeePhoto.query(employee_id: employee.id)
]
