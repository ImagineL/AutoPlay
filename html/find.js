//���ͼƬ �� ��ȡͼƬ�϶�Ӧ������,�������y���Ƿ��ŵģ�Ӧ���Ǹ�y������ʾ��������y
var JPos = {};
(function ($) {
    $.$getAbsPos = function (p) {
        var _x = 0;
        var _y = 0;
        while (p.offsetParent) {
            _x += p.offsetLeft;
            _y += p.offsetTop;
            p = p.offsetParent;
        }

        _x += p.offsetLeft;
        _y += p.offsetTop;

        return { x: _x, y: _y };
    };

    $.$getMousePos = function (evt) {
        var _x, _y;
        evt = evt || window.event;
        if (evt.pageX || evt.pageY) {
            _x = evt.pageX;
            _y = evt.pageY;
        } else if (evt.clientX || evt.clientY) {
            _x = evt.clientX + document.body.scrollLeft - document.body.clientLeft;
            _y = evt.clientY + document.body.scrollTop - document.body.clientTop;
        } else {
            return $.$getAbsPos(evt.target);

        }
        return { x: _x, y: _y };
    }
})(JPos);


function vControl(pChoice) {
    switch (pChoice) {
        case "GETMOUSEPOSINPIC":
            var mPos = JPos.$getMousePos();
            var iPos = JPos.$getAbsPos(arguments[1]);
            window.status = (mPos.x - iPos.x) + " " + (mPos.y - iPos.y);
            console.log(window.status);
            //window.location.href="convertToActualCoordinate.action?status="+window.status;
            break;
    }
}
