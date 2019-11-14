$('#summary .head').on('click', function() {
    $(this)
        .next()
        .toggleClass('show');
});

$('#mkdocs-search-wrapper button').on('click', function() {
    console.log('Close button clicked');
    $('#mkdocs-search-wrapper').hide();
});

$('#mkdocs-search-query').on('keyup', function(ev) {
    console.log('changey changey');
    let t = setTimeout(function() {
        let $searchResultsArticles = $('#mkdocs-search-results article');
        console.log(2, $searchResultsArticles.length);
        let $makedocsSearchWrapper = $('#mkdocs-search-wrapper');
        let $searchInput = $('#mkdocs-search-query');
        if ($searchResultsArticles.length) {
            $makedocsSearchWrapper.css('display', 'flex');
            $searchInput.addClass('pop-over');
        } else {
            $makedocsSearchWrapper.hide();
            $searchInput.removeClass('pop-over');
        }
    }, 200); // Very hacky - I know!
    let $searchResultsArticles = $('#mkdocs-search-results article');
    console.log(1, $searchResultsArticles.length);
    return true;
});

console.log('Load');
