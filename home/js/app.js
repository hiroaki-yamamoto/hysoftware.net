/*global angular*/

(function (a) {
    "use strict";
    a.module("hysoft", [
        "ui.router",
        "ngRoute",
        "hysoft.home.routes",
        "hysoft.about.routes",
        "hysoft.contact.route"
    ]).config([
        "$urlRouterProvider",
        "$locationProvider",
        "$compileProvider",
        "$httpProvider",
        function (urlRouterProvider, locationProvider, compileProvider, httpProvider) {
            compileProvider.aHrefSanitizationWhitelist(/^\s*(https?|data):/);
            urlRouterProvider.otherwise("/");
            locationProvider.html5Mode(true);
            httpProvider.defaults.headers.common["X-Requested-With"] = "XMLHttpRequest";
        }
    ]).run([
        "$rootScope",
        "$state",
        "$http",
        function (rootScope, state, httpProvider) {
            /*jslint sub:true*/
            rootScope["state"] = state;
            httpProvider["defaults"]["xsrfHeaderName"] = "X-CSRFToken";
        }
    ]);
}(angular));
