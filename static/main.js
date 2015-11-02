(function () {

  'use strict';

  angular.module('lcgtourney', [])
  .config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
  })
  .controller('TourneyController', ['$scope', '$log', function($scope, $log) {
    $scope.getResults = function() {
      $log.log("test");
    };
  }

  ]);

}());