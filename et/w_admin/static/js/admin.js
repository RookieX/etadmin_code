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
    $('.tablelist thead :checkbox').chkCheckAll($('.tablelist tbody :checkbox'));
});