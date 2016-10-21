(function() {
  var app;

  app = angular.module('example.app.basic', []);

  app.controller('AppController', [
    '$scope', '$http', function($scope, $http) {
      $scope.employees = [];
      return $http.get('/api/employees').then(function(result) {
        return angular.forEach(result.data, function(item) {
          return $scope.employees.push(item);
        });
      });
    }
  ]);

}).call(this);

(function() {
  var app;

  app = angular.module('example.app.editor', ['example.api', 'example.app.photos']);

  app.controller('EditController', [
    '$scope', 'Employee', function($scope, Employee) {
      $scope.newEmployee = new Employee();
      return $scope.save = function() {
        return $scope.newEmployee.$save().then(function(result) {
          return $scope.employees.push(result);
        }).then(function() {
          return $scope.newEmployee = new Employee();
        }).then(function() {
          return $scope.errors = null;
        }, function(rejection) {
          return $scope.errors = rejection.data;
        });
      };
    }
  ]);

}).call(this);

(function() {
  var app;

  app = angular.module('example.app.manage', ['example.api', 'example.app.editor']);

  app.controller('DeleteController', [
    '$scope', 'AuthUser', function($scope, AuthUser) {
      $scope.canDelete = function(employee) {
        return employee.author.username === AuthUser.username;
      };
      return $scope["delete"] = function(employee) {
        return employee.$delete().then(function() {
          var idx;
          idx = $scope.employees.indexOf(employee);
          return $scope.employees.splice(idx, 1);
        });
      };
    }
  ]);

}).call(this);

(function() {
  var app;

  app = angular.module('example.app.photos', ['example.api']);

  app.controller('AppController', [
    '$scope', 'Employee', 'EmployeePhoto', function($scope, Employee, EmployeePhoto) {
      $scope.photos = {};
      $scope.employees = Employee.query();
      return $scope.employees.$promise.then(function(results) {
        return angular.forEach(results, function(employee) {
          return $scope.photos[employee.id] = EmployeePhoto.query({
            employee_id: employee.id
          });
        });
      });
    }
  ]);

}).call(this);

(function() {
  var app;

  app = angular.module('example.app.playground', ['example.api.playground']);

  app.controller('AppController', [
    '$scope', 'User', function($scope, User) {
      $scope.users = [];
      $scope.newUsername = "";
      $scope.loadUsers = function() {
        return User.query().$promise.then(function(results) {
          return $scope.users = results;
        });
      };
      $scope.addUser = function() {
        var user;
        user = new User({
          username: $scope.newUsername
        });
        $scope.newUsername = "";
        return user.$save().then($scope.loadUsers);
      };
      $scope.deleteUser = function(user) {
        return user.$delete().then($scope.loadUsers);
      };
      return $scope.loadUsers();
    }
  ]);

}).call(this);

(function() {
  var app;

  app = angular.module('example.app.resource', ['example.api']);

  app.controller('AppController', [
    '$scope', 'Employee', function($scope, Employee) {
      return $scope.employees = Employee.query();
    }
  ]);

}).call(this);

(function() {
  var app;

  app = angular.module('example.app.static', []);

  app.controller('AppController', [
    '$scope', '$http', function($scope, $http) {
      return $scope.employees = [
        {
          author: {
            username: 'Joe'
          },
          title: 'Sample employee #1',
          body: 'This is the first sample employee'
        }, {
          author: {
            username: 'Karen'
          },
          title: 'Sample employee #2',
          body: 'This is another sample employee'
        }
      ];
    }
  ]);

}).call(this);

(function() {
  var app;

  app = angular.module('example.app.update', ['example.api']);

  app.controller('AppController', [
    '$scope', 'User', function($scope, User) {
      $scope.users = [];
      $scope.newUsername = "";
      $scope.loadUsers = function() {
        return User.query().$promise.then(function(results) {
          return $scope.users = results;
        });
      };
      $scope.addUser = function() {
        var user;
        user = new User({
          username: $scope.newUsername
        });
        $scope.newUsername = "";
        return user.$save().then($scope.loadUsers);
      };
      $scope.deleteUser = function(user) {
        return user.$delete().then($scope.loadUsers);
      };
      return $scope.loadUsers();
    }
  ]);

}).call(this);

(function() {
  var app;

  app = angular.module('example.api', ['ngResource']);

  app.factory('User', [
    '$resource', function($resource) {
      return $resource('/api/users/:username', {
        username: '@username'
      });
    }
  ]);

  app.factory('Employee', [
    '$resource', function($resource) {
      return $resource('/api/employees/:id', {
        id: '@id'
      });
    }
  ]);

  app.factory('Photo', [
    '$resource', function($resource) {
      return $resource('/api/photos/:id', {
        id: '@id'
      });
    }
  ]);

  app.factory('UserEmployee', [
    '$resource', function($resource) {
      return $resource('/api/users/:username/employees/:id');
    }
  ]);

  app.factory('EmployeePhoto', [
    '$resource', function($resource) {
      return $resource('/api/employees/:employee_id/photos/:id');
    }
  ]);

}).call(this);

(function() {
  var app;

  app = angular.module('example.api.playground', []);

  app.factory('User', [
    '$q', function($q) {
      var MockUser, i, len, ref, storage, user, username;
      storage = {};
      MockUser = (function() {
        function MockUser(params) {
          var key, value;
          for (key in params) {
            value = params[key];
            this[key] = value;
          }
        }

        MockUser.query = function() {
          var dfr, key, val, values;
          dfr = $q.defer();
          values = (function() {
            var results;
            results = [];
            for (key in storage) {
              val = storage[key];
              results.push(val);
            }
            return results;
          })();
          dfr.resolve(values);
          values.$promise = dfr.promise;
          return values;
        };

        MockUser.save = function(params) {
          var user;
          user = new this(params);
          user.$save();
          return user;
        };

        MockUser.prototype.$save = function() {
          var dfr;
          storage[this.username] = this;
          dfr = $q.defer();
          dfr.resolve(this);
          return dfr.promise;
        };

        MockUser.prototype.$delete = function() {
          var dfr;
          delete storage[this.username];
          dfr = $q.defer();
          dfr.resolve();
          return dfr.promise;
        };

        return MockUser;

      })();
      ref = ['bob', 'sally', 'joe', 'rachel'];
      for (i = 0, len = ref.length; i < len; i++) {
        username = ref[i];
        user = new MockUser({
          username: username
        });
        storage[user.username] = user;
      }
      return MockUser;
    }
  ]);

}).call(this);
