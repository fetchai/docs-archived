$('#summary .head').on('click', function () {
    $(this)
        .next()
        .toggleClass('show');
});

$('#mkdocs-search-wrapper, #mkdocs-search-wrapper button').on('click', function () {
    $('#mkdocs-search-wrapper').hide();
    let $searchInput = $('#mkdocs-search-query');
    $searchInput.val('');
});
$('.search-results-container').on('click', function (e) {
    e.stopPropagation();
}).find('a').on('click', function (e) {
    e.stopPropagation();
})


$('#mkdocs-search-query').on('keyup', function (ev) {
    let t = setTimeout(function () {
        let $sq = $('#mkdocs-search-query');
        let v = $sq.val();
        let $stc = $('#search-text-copy');
        $stc.val(v);
        $stc.on('keyup', function () {
            $sq.val($stc.val());
            doSearch();
        })
        let $searchResultsArticles = $('#mkdocs-search-results article');
        let $makedocsSearchWrapper = $('#mkdocs-search-wrapper');
        if ($searchResultsArticles.length) {
            $makedocsSearchWrapper.css('display', 'flex');
            $stc.focus();
        } else if ($searchResultsArticles.length == 0 && $sq.val().length) {
            $makedocsSearchWrapper.css('display', 'flex');
            $stc.focus();
        } else {
            $makedocsSearchWrapper.hide();
        }
    }, 200); // Very hacky - I know!
    return true;
});

$(document).ready(function () {
    let t = setTimeout(function () {
        $('.book-summary').removeClass('not-loaded');
    }, 20); // Very hacky - I know!

    $('.year').innerHtml = new Date().getFullYear(); // Would rather do this in jinja if possible!

});

document.addEventListener('DOMContentLoaded', function () {
    const matchString = document.URL.replace(window.origin + '/', '').replace(
        new RegExp('/', 'g'),
        '-'
    );
    $('nav#nav a').each(function (index) {
        let id = $(this).attr('id');
        if ($(this).attr('id') == matchString) {
            $(this)
                .addClass('highlight')
                .parents('ul')
                .addClass('show');
        }
    });
    $('#hamburger, .book-summary').on('click', function (e) {
        // scroll to top 
        $('html, body').animate({
            scrollTop: 0
        }, 100);
        $('html').toggleClass('show-side-menu');
    })
    $('.book-summary>div').on('click', function (e) {
        e.stopPropagation();
    }).find('a').on('click', function (e) {
        $('html').toggleClass('show-side-menu');
        e.stopPropagation();
    })

});
