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


//显示下拉框
function showDropdownList(ddl) {
    ddl = $(ddl);
    ddl.children('ul').slideDown('fast');
}

//隐藏下拉框
function hideDropdownList(ddl) {
    ddl = $(ddl);
    ddl.children('ul').slideUp('fast');
}

//显示/隐藏下拉框
function tolggleDropdownList(ddl) {
    ddl = $(ddl);
    ddl.children('ul').slideToggle('fast');
}

//初始化下拉框
function initDropdownList(ddl) {
    ddl = $(ddl);


    ddl.find('li').bind('click', selectedDropdownItem);

    var selected = ddl.find('ul li[item-selected]');
    if (selected.length > 0) {
        setDropdownListValue(ddl, selected);
    }
}

//选中值
function selectedDropdownItem() {
    var self = $(this);

    var dropdown = self.parent().parent();

    setDropdownListValue(dropdown, self);

    hideDropdownList(dropdown);

}

//设置下拉框的选中值
function setDropdownListValue(ddl, li) {
    ddl = $(ddl);
    li = $(li);

    var btn = ddl.children('.dropdown-btn');
    var txt = btn.find('.dropdown-text');

    btn.val(li.val());
    txt.text(li.text());

    li.attr('item-selected', 'true').siblings().removeAttr('item-selected');
}
$(function () {

    $('.dropdown').each(function (index, item) {
        initDropdownList(item);
    });

    $('.dropdown .dropdown-btn').click(function (e) {
        var self = $(this);
        tolggleDropdownList($(this).parent());
        e.stopPropagation();
    });

    $(document).click(function () {
        hideDropdownList($('.dropdown'));
    });

    $('.tablelist thead :checkbox').chkCheckAll($('.tablelist tbody :checkbox'));
});