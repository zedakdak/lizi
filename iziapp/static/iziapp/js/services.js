// Services de l'application
var iziServices = angular.module('iziServices', ['ngResource']);

// Services pour le CRUD issus de $ressource
iziServices.factory('Customer', ['$resource',
   function($resource){
  return $resource('/customers/:id', {}, {
      query: {method:'GET', params:{id:''}, isArray:true},
      get: {method:'GET', params:{id:'@id'}},
      save: {method: 'POST', params:{id:'@id'}}
    });
}]);

iziServices.factory('CustomerDetail', ['$resource',
   function($resource){
  return $resource('/customers/:id', {}, {
      query: {method:'GET', params:{id:'@id'}}
       });
}]);
