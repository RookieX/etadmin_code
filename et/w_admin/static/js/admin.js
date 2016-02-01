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

    //显示下拉框
    function showDropdownList(ddl) {
        ddl.children('ul').slideDown('fast');
    }

    //隐藏下拉框
    function hideDropdownList(ddl) {
        ddl.children('ul').slideUp('fast');
    }

    //显示/隐藏下拉框
    function tolggleDropdownList(ddl) {
        ddl.children('ul').slideToggle('fast');
    }

    //设置下拉框的选中值
    function setDropdownListValue(ddl, li) {
        var btn = ddl.children('.dropdown-btn');
        var txt = btn.find('.dropdown-text');

        btn.val(li.val());
        txt.text(li.text());

        li.attr('item-selected','true').siblings().removeAttr('item-selected');
    }

    $('.dropdown').each(function (index, item) {
        var self = $(item);
        var selected = self.find('ul li[item-selected]');
        if (selected.length > 0) {
            setDropdownListValue(self, selected);
        }
    });

    $('.dropdown .dropdown-btn').click(function (e) {
        var self = $(this);
        tolggleDropdownList($(this).parent());
        e.stopPropagation();
    });

    $('.dropdown ul li').click(function () {
        var self = $(this);

        var dropdown = self.parent().parent();

        setDropdownListValue(dropdown, self);

        hideDropdownList(dropdown);
    });

    $(document).click(function () {
        hideDropdownList($('.dropdown'));
    });

    $('.tablelist thead :checkbox').chkCheckAll($('.tablelist tbody :checkbox'));
});