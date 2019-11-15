$('#summary .head').on('click', function() {
    $(this)
        .next()
        .toggleClass('show');
});

$('#mkdocs-search-wrapper button').on('click', function() {
    $('#mkdocs-search-wrapper').hide();
    let $searchInput = $('#mkdocs-search-query');
    $searchInput.val('');
    $searchInput.removeClass('pop-over');
});

$('#mkdocs-search-query').on('keyup', function(ev) {
    let $sq = $('#mkdocs-search-query');
    let t = setTimeout(function() {
        let $searchResultsArticles = $('#mkdocs-search-results article');
        let $makedocsSearchWrapper = $('#mkdocs-search-wrapper');
        let $searchInput = $('#mkdocs-search-query');
        if ($searchResultsArticles.length) {
            $makedocsSearchWrapper.css('display', 'flex');
            $searchInput.addClass('pop-over');
        } else if ($searchResultsArticles.length == 0 && $sq.val().length) {
            $makedocsSearchWrapper.css('display', 'flex');
            $searchInput.addClass('pop-over');
        } else {
            $makedocsSearchWrapper.hide();
            $searchInput.removeClass('pop-over');
        }
    }, 200); // Very hacky - I know!
    return true;
});

$(document).ready(function() {
    let t = setTimeout(function() {
        $('.book-summary').removeClass('not-loaded');
    }, 20); // Very hacky - I know!
    $('.year').innerHtml = new Date().getFullYear(); // Would rather do this in jinja if possible!
});

document.addEventListener('DOMContentLoaded', function() {
    const matchString = document.URL.replace(window.origin + '/', '').replace(
        new RegExp('/', 'g'),
        '-'
    );
    $('nav#nav a').each(function(index) {
        let id = $(this).attr('id');
        if ($(this).attr('id') == matchString) {
            $(this)
                .parents('ul')
                .addClass('show');
        }
    });
});
