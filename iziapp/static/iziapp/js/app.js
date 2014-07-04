var iziApp = angular.module('iziApp', [
  'ngRoute',
  'iziServices',
  'customerControllers',
  'customerFilters'
  ]);

// Configuration des routes
iziApp.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
      when('/customers', {
        templateUrl: 'partials/customer-list.html',
        controller: 'CustomerListController'
      }).
      when('/customers/:customerId', {
        templateUrl: 'partials/customer-detail.html',
        controller: 'CustomerDetailController'
      }).
      otherwise({
        redirectTo: '/customers'
      });
  }]);

// Configuration du service de la Ressource
 iziApp.config(['$resourceProvider',
  function ($resourceProvider) {
       // Don't strip trailing slashes from calculated URLs
       $resourceProvider.defaults.stripTrailingSlashes = true;
     }]);
