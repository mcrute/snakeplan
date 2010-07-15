/*********************************************************************
 * Main SnakePlan Application                                        *
 *********************************************************************/
(function() {

var URLS = {
    project: "/api/project",
    projectStories: "/api/project/{0}/stories"
};

window.simpleTemplate = simpleTemplate;

$(document).ready(function()
{
    $.getJSON(URLS.project, loadProjectSelector);

    $("#project-select").change(function()
    {
        $.getJSON(URLS.projectStories.replace("{0}", getCurrentProjectId()), loadTaskList);
    });
});


function getCurrentProjectId()
{
    return $("#project-select").val();
}


function loadProjectSelector(json)
{
    $.each(json, function(i, item)
    {
        $("#project-select").append(new Option(item.name, item.id));
    });
}


function loadTaskList(json)
{
    var taskList = $("#task-table");
    taskList.empty();

    $.each(json, function(i, item)
    {
        $("<li/>").text(item.name).attr("class", "ui-state-default").appendTo(taskList);
    });

    $("#task-table").sortable({
        placeholder: 'ui-state-highlight'
    });
    $("#task-table").disableSelection();
}

})();


/*********************************************************************
 * Centering Plugin                                                  *
 *********************************************************************/
(function($){
 $.fn.extend({
    center: function (options) {
        var options =  $.extend({
            inside: window,
            transition:  0,
            minX: 0,
            minY: 0,
            withScrolling: true,
            vertical: true,
            horizontal: true
        }, options);

        return this.each(function() {
            var props = {position:'absolute'};
            if (options.vertical) {
                var top = ($(options.inside).height() - $(this).outerHeight()) / 3;
                if (options.withScrolling) {
                    top += $(options.inside).scrollTop() || 0;
                }
                top = (top > options.minY ? top : options.minY);
                $.extend(props, {top: top+'px'});
            }

            if (options.horizontal) {
                var left = ($(options.inside).width() - $(this).outerWidth()) / 3;
                if (options.withScrolling) {
                    left += $(options.inside).scrollLeft() || 0;
                }
                left = (left > options.minX ? left : options.minX);
                $.extend(props, {left: left+'px'});
            }

            if (options.transition > 0) {
                $(this).animate(props, options.transition);
            } else { 
                $(this).css(props);
            }

            return $(this);
        });
    }
});
})(jQuery);


/*********************************************************************
 * Hitch Plugin                                                      *
 *********************************************************************/
(function($) {
$.fn.hitch = function(ev, fn, scope) {
    return this.bind(ev, function() {
        return fn.apply(scope || this, Array.prototype.slice.call(arguments));
    });
};
})(jQuery);


/*********************************************************************
 * Overlay Plugin                                                    *
 *                                                                   *
 * WARNING: Here be dragons!                                         *
 *                                                                   *
 * This needs some love still. I really want to make this into a     *
 * decent overlay so that it can be used for async form loading but  *
 * don't yet know how to properly extend jQuery.                     *
 *                                                                   *
 *********************************************************************/
(function($) {
window.overlay = $("#overlay");
window.overlay.close = function() {
    $(this).fadeOut("slow");
};
window.overlay.show = function() {
    $(this).fadeIn("slow");
};

Overlay = function(height, width)
{
    this.height = height;
    this.width = width;

    this.overlayBox = $("#overlay-display-box").clone().attr("id", "");
    this.overlayBox.appendTo(overlay);
};
Overlay.prototype = {

    open: function() 
    {
        this.overlayBox.css({
            width: this.width + "px",
            height: this.height + "px",
        }).center().draggable();

        this.overlayBox.find(".overlay-background").css({
            width: this.width + "px",
            height: this.height + "px"
        });

        this.overlayBox.find(".overlay-foreground").css({
            width: (this.width - 22) + "px",
            height: (this.height - 22) + "px"
        });

        this.overlayBox.find(".overlay-close").hitch("click", function() {
            this.destroy();
        }, this);

        this.overlayBox.fadeIn("slow");
        overlay.show();
    },

    close: function() {
        this.overlayBox.fadeOut("slow");
        overlay.close();
    },

    destroy: function() {
        this.close();
        this.overlayBox.remove();
    }

};
})(jQuery);
