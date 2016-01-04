'use strict'

angular.module('ngDirectiveForms')
	.controller('mainController', function($scope, $q, $timeout, $http) {
		$scope.gifts = [{
			product: {
				type: 'A',
				minAmount: 10,
				maxAmount: 50
			},
			loginData: {

			}
		}, {
			product: {
				type: 'B',
				minAmount: 25,
				maxAmount: 500
			},
			giftData: {
				name: "Gift User B",
				amount: 50
			}
		}];

		$scope.formsValid = false;

		$scope.login = function() {
			console.log($scope.loginData);
			$http({
				method: 'POST',
				url: '/login',
				headers: {
					'Content-Type': 'application/json'
				},
				data: $scope.loginData
			}).then(function successCallback(response) {
				// this callback will be called asynchronously
				// when the response is available
				console.log(response.data);
			}, function errorCallback(response) {
				// called asynchronously if an error occurs
				// or server returns response with an error status.
				console.log(response);
			});
		};
	});