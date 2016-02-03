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


(function ($) {
    var dropdown = (function () {

        //显示下拉框
        var showddl = function (ddl) {
            ddl.find('ul').slideDown('fast');
        };

        //隐藏下拉框
        var hideddl = function (ddl) {
            ddl.find('ul').slideUp('fast');
        };

        //显示/隐藏下拉框
        var toggleddl = function (ddl) {
            ddl.find('ul').slideToggle('fast');
        };

        //绑定下拉框事件
        var bindEvent = function (ddl) {
            ddl.find('.dropdown-btn').click(function (e) {
                toggleddl(ddl);
                e.stopPropagation();
            });

            ddl.find('li').click(function () {
                setddlvalue(ddl, $(this));
                hideddl(ddl);
            });
        };

        //给下拉框设置值
        var setddlvalue = function (ddl, li) {
            var btn = ddl.children('.dropdown-btn');
            var txt = btn.find('.dropdown-text');

            btn.val(li.val());
            txt.text(li.text());

            li.attr('item-selected', 'true').siblings().removeAttr('item-selected');
        };

        function dropdown(elem, options) {
            var valField = elem.attr('data-valField');
            var txtField = elem.attr('data-txtField');
            var settings = $.extend({}, $.fn.defaults, {valField: valField, txtField: txtField}, options || {});
            this.init(elem, settings);
        }

        dropdown.prototype = {
            init: function (elem, options) {
                var ddl = $('<div>');
                ddl.settings = options;
                ddl.addClass('dropdown').attr('name', elem.attr('name'));
                var dropdownBtn = $('<button>').attr('type', 'button').addClass('dropdown-btn').appendTo(ddl);
                dropdownBtn.append($('<span>').addClass('dropdown-text').text('请选择')).append($('<span>').addClass('triangle'));

                var container = $('<ul>').appendTo(ddl);

                $.each(elem.find('option'), function (index, item) {
                    var self = $(item);
                    var li = $('<li>').attr('value', self.attr('value')).text(self.text()).appendTo(container);

                    if (self.is(':selected')) {
                        li.attr('item-selected', true);
                        setddlvalue(ddl, li);
                    }
                });

                $(this).data('ddl', ddl);
                elem.after(ddl);
                elem.remove();

                bindEvent(ddl);

                $(document).click(function () {
                    hideddl($('.dropdown'));
                });
            },

            load: function (datas) {
                var self = $(this);
                var ddl = self.data('ddl');
                var settings = ddl.settings;

                var ul = ddl.find('ul');
                ul.empty();

                for (var i = 0; i < datas.length; i++) {
                    var data = datas[i];
                    $('<li>').text(data[settings.txtField]).val(data[settings.valField]).appendTo(ul);
                }
                ddl.find('.dropdown-btn').val('');
                ddl.find('.dropdown-text').text('请选择');
            },

            getSelectedVal: function () {
                var self = $(this);
                var ddl = self.data('ddl');
                return ddl.find('li[item-selected]').val();
            },
            getSelectedText: function () {
                var self = $(this);
                var ddl = self.data('ddl');
                return ddl.find('li[item-selected]').text();
            }
        };

        return dropdown;
    })();

    $.fn.dropdown = function (options) {
        return new dropdown($(this), options);
    };

    $.fn.dropdown.defaults = {
        valField: 'value',
        txtField: 'txt'
    };

    $('select[data-dropdown]').dropdown({});
})(window.jQuery);

$(function () {
    $('.tablelist thead :checkbox').chkCheckAll($('.tablelist tbody :checkbox'));
});