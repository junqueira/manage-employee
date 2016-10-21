app = angular.module 'example.app.static', []

app.controller 'AppController', ['$scope', '$http', ($scope, $http) ->
    $scope.posts = [
        author:
            username: 'Joe'
        title: 'Sample Employee #1'
        body: 'This is the first sample employee'
    ,
        author:
            username: 'Karen'
        title: 'Sample Employee #2'
        body: 'This is another sample employee'
    ]
]
