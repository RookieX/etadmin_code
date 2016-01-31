/**
 * Created by 徐鹏程 on 16-1-28.
 */

(function ($) {
    $.fn.extend({
        chkCheckAll: function (chks) {
            var self = $(this);
            self.change(function () {
                $.each(chks, function (index, item) {
                    $(item).prop('checked', self.is(':checked'));
                });
            })
        }
    });
})(window.jQuery);

$(function () {
    $(document).click(function () {
        $('.dropdown ul').slideUp('fast');
    });

    $('.tablelist thead :checkbox').chkCheckAll($('.tablelist tbody :checkbox'));

    $('.dropdown ul').hide();
    $('.dropdown .btn').click(function (e) {
        var self = $(this);
        $(this).parent().children('ul').slideToggle('fast');
        e.stopPropagation();
    });
});