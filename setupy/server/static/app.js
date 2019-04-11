function _filterByPrefix(array, prefix) {
    return array.filter(function(i) {
        return i.startsWith(prefix)
    }).map(function(i) {
        return i.substring(prefix.length);
    })
}

function getFeatures(array) {
    return _filterByPrefix(array, "f:");
}

function getSettings(array) {
    return _filterByPrefix(array, "s:");
}

$(document).ready(function() {
    var $selectedFeaturesAndSettings = $("#setting-feature-select").selectize();
    $("#javascript-enabled-container").show();
    $("#create-setup").click(function() {
        var items = $selectedFeaturesAndSettings[0].selectize.items;
        var features = getFeatures(items).join(",");
        var settings = getSettings(items).join(",");

        var url = "/get";
        if (features.length || settings.length) {
            url += "?";
        }

        if (features.length) {
            url += "features=" + features;
        }

        if (features.length && settings.length) {
            url += "&";
        }

        if (settings.length) {
            url += "settings=" + settings;
        }

        window.location.href=url;
    })
});
