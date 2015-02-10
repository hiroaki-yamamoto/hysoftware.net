/*global exports, require*/

(function (e, r) {
    "use strict";
    // Output CSS file generated by SCSS, and
    // it should be input of cssprefix
    var input = r("./scss.js").output_path;

    e.autoprefixer = {
        "dev": {
            "options": {
                "map": {
                    "prev": input + ".map",
                    "inline": false
                }
            },
            "src": input,
            "dest": input
        },
        "production": {
            "src": input,
            "dest": input
        }
    };
}(exports, require));
