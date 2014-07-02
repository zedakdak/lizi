var customerControllers = angular.module('customerControllers', []);
/*
iziApp.controller('CustomerController', function($scope, $http){
 $http.get('/customers/').success(function(data) {
    $scope.customers = data
 });
})
*/
customerControllers.controller('CustomerListController',['$scope', 'Customer',
  function($scope, Customer){
     $scope.customers = Customer.query();
    }
]);


customerControllers.controller('CustomerDetailController',['$scope', '$routeParams', 'Customer',
  function($scope, $routeParams, Customer){
     $scope.customerId = $routeParams.customerId;
     //$scope.customer = Customer.query({id: $routeParams.customerId});
     $scope.customer = Customer.get({id: $routeParams.customerId});

     // creation
     $scope.create = function(newCustomerName) {
        var customer = new Customer();
        customer.name = newCustomerName;
        customer.email = 'testmail';
        customer.telephone = $scope.newCustomerTelephone;
        customer.$save();
        //$scope.customers.push(customer);
     }
     // modification
     $scope.update = function(customer) {
        console.log('modification');
        //console.log($scope);
        console.log(customer);
        customer.$update();
     }
     // suppression
     $scope.delete = function(customer) {
        console.log('suppression');
        //console.log($scope);
        console.log(customer);
        customer.$remove();
     }

 }]);

