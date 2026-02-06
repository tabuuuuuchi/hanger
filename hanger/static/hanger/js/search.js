document.getElementById('search-button').addEventListener('click', function() {
    const hide = document.getElementById('search-hide');
    const block = document.getElementById('search-flex');

    hide.style.display = 'none';
    block.style.display = 'flex';
});

document.getElementById('return-button').addEventListener('click', function() {
    const hide = document.getElementById('search-hide');
    const block = document.getElementById('search-flex');

    hide.style.display = 'flex';
    block.style.display = 'none';
});

document.getElementById('search-result').addEventListener('click', function() {
    const hide = document.getElementById('search-hide');
    const block = document.getElementById('search-flex');

    hide.style.display = 'none';
    block.style.display = 'flex';
});
