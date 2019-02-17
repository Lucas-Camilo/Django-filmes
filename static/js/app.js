var app = angular.module('plunker', []);

app.controller('Ctrl', function($scope) {
    $scope.func = 'cadastro';
    $scope.isShown = function(func) {
        return func === $scope.func;
    };
});

// http://stackoverflow.com/q/21400456/949476
