
    function hover(img) {
        var imageName = img.getAttribute('src').split('/').pop().split('.')[0];
        img.setAttribute('src', 'static/' + imageName + '_back.jpg');
    }

    function unHover(img) {
        var imageName = img.getAttribute('src').split('/').pop().split('.')[0];
        var newSrc = imageName.replace('_back', '');
        img.setAttribute('src', 'static/' + newSrc + '.jpg');
    }
